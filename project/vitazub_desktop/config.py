import os


def db_name():
    config_file = open('config.cfg', 'r')
    for line in config_file:
        if line[0:2] == 'DB':
            config_file.close()
            return line[5:-1]


def save_config_file(db_path):
    os.remove('config.cfg')
    config_file = open('config.cfg', 'w')
    config_file.write('DB = ' + db_path + '\n\n')
    config_file.close()
