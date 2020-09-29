import configparser
import sys

import requests
from requests.auth import HTTPBasicAuth


def extract(value):
    return float(value[1])


def extract_list_of_values():
    values = r.json()['data']['result'][0]['values']
    return list(map(extract, values))


def help():
    print('1.) configure something useful in application.properties \n'
          '2.) call with prometheusChamp <QUERY> <STEP>')


if __name__ == '__main__':
    if (len(sys.argv) == 1 or sys.argv[1] == "help"):
        help()
    else:
        config = configparser.RawConfigParser()
        config.read("application.properties")
        details_config = dict(config.items("BASE"))
        username = details_config['user']
        password = details_config['password']
        query = details_config['prometheus_uri'] + sys.argv[1] + "&step=" + sys.argv[2]
        print (query)
        r = requests.get(query, auth=HTTPBasicAuth(username, password))
        if (r.status_code == 200):
            data_for_calculation = extract_list_of_values()
            print("MAX", max(data_for_calculation))
            print("MIN", min(data_for_calculation))
            print("AVG", sum(data_for_calculation) / len(data_for_calculation))
