koombea_challenge/.venv/lib/python3.8/site-packages/django_cryptography/fields.py -> change line 7 to:
from django.utils.translation import gettext_lazy as _

koombea_challenge/.venv/lib/python3.8/site-packages/django_cryptography/core/signing.py -> change line 18 to
from django.utils.encoding import force_bytes, force_str
and line 127 to return force_str(value)