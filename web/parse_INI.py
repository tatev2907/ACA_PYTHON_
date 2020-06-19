import os
import configparser
def parse_ini(a:str)->dict:
    config = configparser.ConfigParser()
    config.read(a)
    dictionary = {}
    for section in config.sections():
        dictionary[section] = {}
        for option in config.options(section):
            try:
                dictionary[section][option] = config.getint(section, option)
            except ValueError:
                dictionary[section][option] = config.get(section, option)

    return dictionary



if __name__ == "__main__":
    t=True
    while t:
        a=input('Input INI file path')
        if os.path.exists(a):
            break
    print(parse_ini(a))