# Koombea Challenge
[GitHub Repository](https://github.com/Gabrielsldev/koombea_challenge)

### Developed by Gabriel Sobreira Lopes
---
### The goal of the challenge is to build a Django app that can receive CSV file inputs, process the data according to validation rules and save the data to the database.

The information display to the user needs to follow the pattern bellow:

| Name          | Date of Birth | Phone         | Address       | Credit Card   | Franchise     | Email         |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
|     ....      |     ....      |     ....      |     ....      |     ....      |     ....      |     ....      |
|     ....      |     ....      |     ....      |     ....      |     ....      |     ....      |     ....      |

## Requirements:

- User **registers** with **username**, **email** and **password**.
- User **logs in** with **email** and **password**.
- The columns of the CSV file do not need to be the same as the desired output above. Thus **the user needs to select which column in the CSV** file is the intended column **in the table to be saved in the database.**
- The data needs to be cleaned and **validated** accordingly with the task instructions before being saved in the database.
- User can see a **summary** with all the contacts imported.
- The user has access to a **log**.
- The **status** of each file is need to be shown.
> **All requirements** were **implemented**.
---
# Implementation

### The application was done with **Django**.
- **Pandas** was used to handle the CSV files and the validations, along side with some **regular expressions**.
- Python's **Requests** was used to access the [Binlist API](https://binlist.net/) to find out the credit card's franchise.
  - The free version only accepts 10 requests per minute, so I kept the CSV files short for test purposes.
- The library **validate-email** was used for e-mail validation and **django-cryptography** for encrypting credit cards numbers.
---

# Instructions

1. Clone the repository with `git clone git@github.com:Gabrielsldev/koombea_challenge.git` (using SSH)
2. Create a virtual environment with `python3 -m venv .venv`
3. Install the necessary libraries with `pip install -r requirements.txt`
> **IMPORTANT:** The library **django-cryptography** hasn't been updated for Django 4.0, so additional configuration is needed:
>
> 1. In file **koombea_challenge/.venv/lib/python3.8/site-packages/django_cryptography/fields.py**, change **line 7** to:
>
> `from django.utils.translation import gettext_lazy as _`
>
> 2. In file **koombea_challenge/.venv/lib/python3.8/site-packages/django_cryptography/core/signing.py**, change **line 18** to:
>
> `from django.utils.encoding import force_bytes, force_str`
>
> and **line 127** to
>
> `return force_str(value)`
4. Make the migrations with `python manage.py makemigrations`
5. Run the migrations with `python manage.py migrate`
6. Create a superuser with `python manage.py createsuperuser`
> As instructed, **login will be done with e-mail**, not username, but the username is also asked for registration.
7. Run the application with `python manage.py runserver`
---
# Application Usage

The application is pretty **straight forward**.

1. The user can **sign in** with the superuser just created or **sign up with a new user.**
2. The user can use the **navbar** to navigate.
3. The user can upload the CSV files clicking the **Upload link**.
4. Next the **list of uploaded files** will appear with the **status** of each file.
5. The user can click on the link to **process the file** and **select which column in the CSV file correspond to the column in the database table**.
6. After processing the file, a list of all the imported contacts will show up.
> **IMPORTANT:** The instructions weren't very clear whether I should save the record in the database only if **all** the fields were validated. Thus, **I choose to save them if at least one field is validated so we don't loose all the data. The non-validated fields were saved as `null`.**
>
> - This means that fields where data was not validated will show up as `None` in the contact list page.
> - If need be, the application can be changed to save only records that have all fields validated.
7. The **log file** `contact_importer.log` can be found at `koombea_challenge/contact_importer/contact_importer.log`

### The sample CSV files for testing can be found at `koombea_challenge/csf_files`
- There are 4 CSV files to test different use cases: repeated emails, non-complying, empty or missing fields, different column names, some edge cases.
---
# Future improvements

- I think that future improvements should include unit tests, which are very important. It's a gap I'll fill in future developments.
- Processing CSV files in a background job can also be implemented with libraries like Celery. I'm not too familiar on how to implement this feature, which is a gap I'll work on.
---
### Developed by Gabriel Sobreira Lopes