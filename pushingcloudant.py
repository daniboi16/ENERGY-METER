from cloudant.client import Cloudant
import pandas as pd
from google.colab import auth
auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials
gc = gspread.authorize(GoogleCredentials.get_application_default())
client = Cloudant("apikey-v2-1dieqiuutsj9r80qq8q8v8g0lelfwyhmf8fu530pu7tb", "f9c390f5fec4463909c5d2ba1485e50b", url="https://apikey-v2-1dieqiuutsj9r80qq8q8v8g0lelfwyhmf8fu530pu7tb:f9c390f5fec4463909c5d2ba1485e50b@85bee175-5732-4555-a56f-7c43b43f63b1-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()

db = client.create_database('jcomp2', partitioned=True)
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1nqxLiaaszL2aMOvCiXFls0Y6NEBeXcvf6lYfOZgncME/edit?pli=1#gid=0')
worksheet_list = sht2.worksheets()
worksheet = gc.open('AMP').sheet1
rows = worksheet.get_all_values()

entry=[rows[-5],rows[-4],rows[-3],rows[-2],rows[-1]]
j=len(rows)
for i in rows:
  date=i[0]
  time=i[1]
  current_val=i[2]
  #print(current_val)
  partition_key = 'power'+str(j)
  document_key = 'powerdata'+str(j)
  db.create_document({
'_id': ':'.join((partition_key, document_key)),
'date': date,
'time': time,
'current_val': current_val})
  doc = db[':'.join((partition_key, document_key))]
  j=j-1
