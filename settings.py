import configparser

config = configparser.ConfigParser()
config.read('settings.conf')

SESSION_TYPE = config['settings']['session_type'] 
SECRET_KEY = config['keys']['secret_key'] 
PASSWORD = config['keys']['password'] 
LOG_FILE = config['files']['log_file']

AWS_SECRET_KEY = config['aws']['secret_key']
AWS_ACCESS_KEY_ID = config['aws']['access_key_id']
BUCKET_NAME = config['aws']['bucket_name']
AWS_REGION = config['aws']['region']
