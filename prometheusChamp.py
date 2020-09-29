import sys

import requests
from requests.auth import HTTPBasicAuth



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def extract(value):
    return float(value[1])


def extract_list_of_values():
    values = r.json()['data']['result'][0]['values']
    return list(map(extract, values))


def help():
    print('call with prometheusChamp <USER< <PASSWORD> <QUERY>')


if __name__ == '__main__':
    if (len(sys.argv) == 1 or sys.argv[1] == "help"):
        help()
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        query = sys.argv[3]
        r = requests.get(query,
            auth=HTTPBasicAuth(username, password))
        if (r.status_code == 200):
            data_for_calculation = extract_list_of_values()
            print("MAX", max(data_for_calculation))
            print("MIN", min(data_for_calculation))
            print("AVG", sum(data_for_calculation) / len(data_for_calculation))
