import gspread
from oauth2client.service_account import ServiceAccountCredentials

'''
pip work: (python pckg installer)
-> pip install gspread
-> pip install oauth2client

background work: (has been done)
1. Go to Google APIs console
2. New project --> Add Google Drive API, Google Sheets API
3. Create credentials for Web Server to access Application data; Project Role Editor
4. Download JSON file, rename to 'client_secret.json', move into working directory
'''

# must include both fields of scope (feeds and auth/drive)
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

physics_sheet = client.open("Definitions").worksheet("physics")
chem_sheet = client.open("Definitions").worksheet("chemistry")

list_of_chem_def     = chem_sheet.col_values(1)[1:]
list_of_chem_def_ans = chem_sheet.col_values(2)[1:]

list_of_phy_def      = physics_sheet.col_values(1)[1:]
list_of_phy_def_ans  = physics_sheet.col_values(2)[1:]

# print(list_of_chem_def)

import random

while True:

    # for chemistry

    length = len(list_of_chem_def)
    x = random.randint(0,length-1)
    definition = list_of_chem_def[x]
    answer = list_of_chem_def_ans[x]
    print("Define "+definition+"\n")
    y = input()
    print("\n"+answer+"\n")
    print("------------------------------------")

    # for physics

    # length = len(list_of_phy_def)
    # x = random.randint(0,length-1)
    # definition = list_of_phy_def[x]
    # answer = list_of_phy_def_ans[x]
    # print("Define "+ definition+"\n")
    # y=input()
    # print("\n"+answer+"\n")
    # print("------------------------------------")
