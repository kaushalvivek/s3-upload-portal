import configparser

config = configparser.ConfigParser()
config.read('settings.conf')

SESSION_TYPE = config['settings']['session_type'] 
SECRET_KEY = config['keys']['secret_key'] 
PASSWORD = config['keys']['password'] 
LOG_FILE = config['files']['log_file']
