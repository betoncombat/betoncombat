
### local_settings.py
### environment-specific settings
### example with a development environment
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'betoncombat$boc',  # Or path to database file if using sqlite3.
        'USER': 'betoncombat',
        'PASSWORD': 'makemoney',
        'HOST': 'betoncombat.mysql.pythonanywhere-services.com',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}



STRIPE_PUBLIC_KEY = "pk_test_Wwl9beC1fBYmPmEBAxl4CxjB"
STRIPE_SECRET_KEY = "sk_test_29br76r10UWEnAn8JfCCTLTj"