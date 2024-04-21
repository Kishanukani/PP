from pathlib import Path
import os
import firebase_admin  # firebase
from firebase_admin import credentials  # firebase

# firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
FIREBASE_SERVICE_ACCOUNT_KEY_PATH = "serviceAccountKey.json"
FIREBASE_ADMIN_SDK_CONFIG = {
    "credentials": {
        "private_key": """-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC1sdOvG+xEDOGJ
YzSqgNFubamkh/3OLcvW/UVOQDM8gcROLrknDJOmWrg/4gHPYcw5o3UxvynTSz1S
X0wUeZUJOzkA2JGSSgwn4BBi2646vubGadC/AnZvAYo/ygs+ewJN+30J18HOgJCt
gznvUwh6hk8si0zddMHwM7VttAzJgc3mrmnku7ijY4O39EQBmX8gIYUT5jrRXUml
j6/KkrPiHqBHe/XXixg9DqgpocbIf+qSMZwf54oFrAGgPngrzzRkAhjpdJPHCQHW
EutJQip0AkoVGbOJFoNFx+hD+LBbuVrpvy1u7q2sDjcawnOC7VIVoEMtqPIVfDv6
Ryg5MtA1AgMBAAECgf8Z+ewWg03dn/nR3cN2nPQhCL/RxgXpp29J5uvOd19CR0sv
4kr8sJxrX1nE+4rgToF9vBQFO+jyGTYRkMGC+Ku8cu5M/XY42l1I77/OYma5mPfL
zIg+xrT0w3bNQXvzpgjhg6yP7uJgCgFyAFDhszCDILCXeoYcVmHKKM2UR/ZY2JHm
ZY2642hyq9SIq4RsEa/tD6NW4gVZUd4iyli1BFQNJE7pLvD3uSPBpvPZ/5McH1NU
h4SkttKzsQ6WqZarr3UUbdzr2i8Rky1KGtPGBHYcRAFQSXzW46TGV1+SQovJ2nEc
akUjiBY4FP56xgO7yQhRTZp36MeAO+sNoUs6maECgYEA3ajc4hRMo0Dgy8jLulV6
khv9hdbC4nd2zbwYWaitJLNhq9R0vSLKIibbXcRzOiZxlkmN95UxnmR+4L8D1lrK
XoZOrdS0XBb4wMUxz9z46yY+CbnNALzIGdxPHq5OsCplYCKYLTsMLCbp3sXVW11k
CPDsBqYkCy0wp0rV8cvKbq0CgYEA0dfuiFOjRsrf5hAIAVV740IN3aloK10c7NV5
js432NjqAKu+HRIHjgKsO65Ev6LGvNWLhfTNPKdeYKs8MPkR7eQXJBVX9n39v+qJ
jvwPpe3ApTkUu7SvwRhwwc1jPAHFFDVEgp+WyTWfW2XwoePJ34F7bxbRgh1cO/GN
j4uGwKkCgYEAxj98ZvvO24hwRfMuO1auTLWaFzVQkmpUqIddo/sX+KYzahKX4n2W
Gdt1AbVtdYnit47L2a7ndQne7LYLAZGsQ8SN5C1ErsSg8RCtj4LMYsyOWfaC4vD1
ayO+4+r0V91jVAs83d9c8LRRIb0BKTkq+lA4WW4I+LIPPODS3vLs9/UCgYEArdW2
ueKniRa5Ymn3Z7t8NOhcejtDm2C4fI3f9GhrJU2UlFex130/Guql6Y7VTve2sWop
+h+xAcUYzvYrl9pNewgQD4lK5Fy9IAZYTEYNZITPqU/fGBx32Hu5tSLDSUuiCrqR
9a/lBuxQBjQtor8EVg56xa1eg+50oQfbIIYSbHkCgYAkb5SXw/PHNuHZw5eLCdGb
OV35vKRQBzQJCtharMZjFJPwhQPX48V2P6oDQUm/FcmHejrp5NwryQdqvymxrper
vl/KXOghgVS4W7Hxlmk47iItFzSia7feOG9uYeY5SdmvA0IQ1UQ/TW6Re4/IZoPm
uOVzbuWvyY4lOwm9siTl/A==
-----END PRIVATE KEY-----""",
        "client_email": os.getenv(
            "firebase-adminsdk-cwkel@resumedjango.iam.gserviceaccount.com"
        ),
        "project_id": os.getenv("resumedjango"),
    },
    "storage_bucket": os.getenv("gs://resumedjango.appspot.com"),
}

FIREBASE_STORAGE_BUCKET = "resumedjango.appspot.com"
# firebase ends here


# initialization only once starts here

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    # Initialize Firebase app with a unique name
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, name="ResumeApp")
# initialization only once ends here


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-e#39lqkne75@t_2xt10!bk#4h#l-2-)7vs5eu+#9zfl-o!ujf5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "resumeanalysis",
    "prediction",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "PP.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "PP.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation"
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # added for static folders

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
