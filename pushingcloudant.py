from cloudant.client import Cloudant


db_1=open(r"E:\PROJECTS\2)unfinished projects\3)IOT\sampledata.csv")
all_entry=db_1.readlines()
entry=all_entry[-1]
entry=entry.split(',')
date=entry[0]
time=entry[1]
current_val=entry[2]
current_val=current_val[0:4]


client = Cloudant("apikey-v2-1dieqiuutsj9r80qq8q8v8g0lelfwyhmf8fu530pu7tb", "f9c390f5fec4463909c5d2ba1485e50b", url="https://apikey-v2-1dieqiuutsj9r80qq8q8v8g0lelfwyhmf8fu530pu7tb:f9c390f5fec4463909c5d2ba1485e50b@85bee175-5732-4555-a56f-7c43b43f63b1-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()
db = client.create_database('jcomp2', partitioned=True)
partition_key = 'power'
document_key = 'powerdata'
db.create_document({
'_id': ':'.join((partition_key, document_key)),
'date': date,
'time': time,
'current_val': current_val})
doc = db[':'.join((partition_key, document_key))]
print(current_val)
