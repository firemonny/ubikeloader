import os

from dotenv import load_dotenv


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

PRODUCTION = os.environ.get('PRODUCTION')

# STA
STA_URL = ''
STA_USER = ''
STA_PASS = ''

STA_URL = os.environ.get('STA_URL')
    # STA_USER = os.environ.get('STA_USER')
    # STA_PASS = os.environ.get('STA_PASS')

STA_AUTH = (STA_USER, STA_PASS)

TIME_ZONE = os.environ.get('TIME_ZONE')
