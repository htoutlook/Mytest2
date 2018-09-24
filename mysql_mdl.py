from requests.auth import HTTPDigestAuth
import os
import requests
import json
import csv
import getpass
import MySQLdb
import pandas as pd

# Username/passwords
db_user=os.environ.get('DB_USER')
db_pass=os.environ.get('DB_PASS')
rc_user=os.environ.get('RC_USER')
rc_pass=os.environ.get('RC_PASS')

# RC API that includes model names, software version, and hardware version,
# Format can be either JSON or CSV.
url = 'https://urldefense.proofpoint.com/v2/url?u=http-3A__reportcentral.suddenlink.net_api_devices_mdl-5Fhw.php-$

#Back up Hosts table
def create_Hosts_bak():
     try:
          db = MySQLdb.connect(host='localhost', user=(db_user), passwd=(db_pass),db=(db_user))
          cursor = db.cursor()
          cursor.execute ('CREATE TABLE IF NOT EXISTS RC_MDL_bak LIKE RC_MDL;')
          cursor.execute ('Truncate table RC_MDL_bak;')
          cursor.execute ('INSERT RC_MDL_bak SELECT * from RC_MDL;')
          cursor.execute ('Truncate table RC_MDL;')
          db.commit()
          cursor.close()
     except Exception as e:
          print ("Something went wrong")
          print (e)
          db.rollback()
          db.close()

def query_mdl(url, rc_user, rc_pass):
    # Function will HTTP get all data from RC API and return in json format
    response = requests.get(url, auth=HTTPDigestAuth(rc_user, rc_pass))
    return response.json()

def cp_file():
     with open ('temp.json', 'w') as file1:
          json.dump(data,file1)
     file1.close()

#parse data into csv
def conv_csv():
     df=pd.read_json('temp.json')
     df.to_csv('results.csv')


#add to MySQL
def add_to_mysql():
     try:
          db = MySQLdb.connect(host='localhost', user=(db_user), passwd=(db_pass),db=(db_user))
          cursor = db.cursor()
          csv_data = csv.reader(file('results.csv'))
          for row in csv_data:
               print(row)
               cursor.execute("""INSERT INTO RC_MDL(hkey ,cbs, city, descr, firmware_rev, 
                   hardware_rev, hostname, ip, model_name, netype, region, software_rev, state, 
				                  cursor.execute("""INSERT INTO RC_MDL(hkey ,cbs, city, descr, firmware_rev, 
                   hardware_rev, hostname, ip, model_name, netype, region, software_rev, state, 
                       sysdescr, vendor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",row)
          db.commit()
          cursor.close()
     except Exception as e:
          print ("Something went wrong")
          print (e)
          db.rollback()
          db.close()


if __name__ == '__main__':
    create_Hosts_bak()
    data = query_mdl(url, rc_user, rc_pass)
    cp_file()
    conv_csv()
    add_to_mysql()