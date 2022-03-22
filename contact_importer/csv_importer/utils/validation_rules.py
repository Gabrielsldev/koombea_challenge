import logging
import pandas as pd
import re
import requests
from csv_importer.models import Contact
from django.http import HttpResponseRedirect
from django.urls import reverse
from validate_email import validate_email
import datetime

logger = logging.getLogger(__name__)

def validate_csv_fields(request, file, df):

    # Changes status of file to processing
    file.on_hold = False
    file.processing = True
    file.save()
    
    # Clean some fields of the CSV file with the choosen columns
    df[request.POST["date_of_birth"]] = pd.to_datetime(df[request.POST["date_of_birth"]], format='%Y-%m-%d', errors='coerce')
    df[request.POST["credit_card"]] = df[request.POST["credit_card"]].str.replace(r'\D+', '')
    df['email_validation'] = df[request.POST["email"]].apply(validate_email)

    for index, row in df.iterrows():
        user  = request.user
        logger.warning(f"Saving data from CSV to DataBase. File: {file} at {datetime.datetime.now()} | User: {user}")
        # Validate name
        if re.match("^[a-zA-Z -]*$", row[request.POST["name"]]):
            name = row[request.POST["name"]]
        else:
            name = None
            logger.warning(f'Contact name is not in a valid format: {row[request.POST["name"]]}.')
        # Validade date of birth
        if isinstance(row[request.POST["date_of_birth"]], pd._libs.tslibs.timestamps.Timestamp):
            date_of_birth = row[request.POST["date_of_birth"]]
        else:
            date_of_birth = None
            logger.warning(f'Contact date of birth is not in a valid format: {row[request.POST["date_of_birth"]]}.')
        # Validade phone
        if re.match("\(\+[0-9][0-9]\)[ ][0-9]{3}[ ][0-9]{3}[ ][0-9]{2}[ ][0-9]{2}[ ][0-9]{2}$|\(\+[0-9]{2}\)[ ][0-9]{3}[-][0-9]{3}[-][0-9]{2}[-][0-9]{2}[-][0-9]{2}$", row[request.POST["phone"]]):
            phone = row[request.POST["phone"]]
        else:
            phone = None
            logger.warning(f'Contact phone number is not in a valid format: {row[request.POST["phone"]]}.')
        # Validate address            
        if (pd.notnull(row[request.POST["address"]]) and row[request.POST["address"]] != ''):
            address = row[request.POST["address"]]
        else:
            address = None
            logger.warning(f'Contact adress is not in a valid format: {row[request.POST["address"]]}.')
        # Validade and encrypt card and set franchise
        # Checks if card number is valid without the need to send card number over the internet via an API
        def luhn(n): # Luhn algorithm to validade card number
            r = [int(ch) for ch in str(n)][::-1]
            return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0
        # Gets credit card number
        credit_card = row[request.POST["credit_card"]]
        if credit_card == '':
            credit_card = None
            logger.warning(f'Contact credit card is not in a valid format: {row[request.POST["credit_card"]]}.')
            franchise = None
            logger.warning(f'Contact credit card franchise is not valid.')
            last_four_card_numbers = None
            logger.warning(f'Contact credit card is not in a valid format.')
        elif luhn(credit_card):
            # Checks BIN number to know which is the card franchise using binlist API (10 requests/min for free)
            six_first_digits = credit_card[:6]
            url = f"https://lookup.binlist.net/{six_first_digits}"
            r = requests.get(url=url)
            if r.status_code == 404: # Means there's no valid card (https://binlist.net/)
                pass
            else:
                data = r.json()
                franchise = data['scheme']
                last_four_card_numbers = 'XXXX XXXX XXXX '+ credit_card[-4:]
        else:
            credit_card = None
            logger.warning(f'Contact credit card is not in a valid format: {row[request.POST["credit_card"]]}.')
            franchise = None
            logger.warning(f'Contact credit card franchise is not valid.')
            last_four_card_numbers = None
            logger.warning(f'Contact credit card is not in a valid format.')
        # Validade email
        if row['email_validation'] == True:
            email = row[request.POST["email"]]
            if Contact.objects.filter(user=request.user,email=email).exists():
                name=None
                date_of_birth=None 
                phone=None
                address=None 
                credit_card=None 
                franchise=None
                last_four_card_numbers=None
                email=None
                logger.warning(f'Contact email already exists. Contact not saved.')
        else:
            logger.warning(f'Contact email is not in a valid format: {row[request.POST["email"]]}.')
            email = None
            
        # Saves to database
        if (name==None and 
            date_of_birth==None and 
            phone==None and
            address==None and 
            credit_card==None and 
            franchise==None and
            last_four_card_numbers==None and 
            email==None):
            
            file.processing = False
            file.failed = True
            file.save()
            logger.warning(f'Contact not saved.')
        else:
            new_ativo_instance = Contact.objects.create(user=user, name=name, date_of_birth=date_of_birth, phone=phone,
                                                        address=address, credit_card=credit_card, franchise=franchise,
                                                        last_four_card_numbers=last_four_card_numbers, email=email)
            new_ativo_instance.save()
            file.processing = False
            file.failed = False
            file.finished = True
            file.save()
        
    logger.warning(f'Done with file {file} at {datetime.datetime.now()}')

    return None