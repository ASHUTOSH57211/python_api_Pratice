import configparser

def get_config():
    config =configparser.ConfigParser()
    config.read('D:\python_API\properties.ini')
    return config