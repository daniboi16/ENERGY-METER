import datetime
import math
#to get current data and time
now = datetime.datetime.now()

#variables
submeter1=0.00
submeter2=0.00
submeter3=0.00
active=0.00
reactive=0.00


#opening file to write
db_w=open(r"E:\PROJECTS\2)unfinished projects\3)IOT\household_power_consumption\sample2.csv","w")
header_w="DATE,"+"TIME,"+"ACTIVE POWER,"+"REACTIVE POWER,"+"APPARENT POWER,"+"VOLTAGE,"+"CURRENT,"+"POWER FACTOR,"+"SUB METER 1,"+"SUB METER 2,"+"SUB METER 3"+"\n"
db_w.write(header_w)

#file handeling
db=open(r"E:\PROJECTS\2)unfinished projects\3)IOT\household_power_consumption\sample.txt")
header=db.readline()
for i in range(1,1100):
    entry=db.readline()
    entry=entry.split(';')
    active+=float(entry[2])
    reactive+=float(entry[3])
    apparent=(((active**2)+(reactive**2))**(0.5))
    voltage=float(entry[4])
    current=apparent/voltage
    pf=math.atan(reactive/apparent)
    submeter1+=float(entry[6])
    submeter2+=float(entry[7])
    submeter3+=float(entry[8])
    
    write_entry=entry[0]+","+entry[1]+","+entry[2]+","+entry[3]+","+str(apparent)+","+str(voltage)+","+str(current)+","+str(pf)+","+entry[6]+","+entry[7]+","+entry[8]
    db_w.write(write_entry)

db_w.flush()
db_w.close()

base_charge=0
if (active<250):
    base_charge=0
elif (active<300):
    base_charge=5.8*active
elif (active<350):
    base_charge=6.6*active
elif (active<400):
    base_charge=6.9*active
elif (active<500):
    base_charge=7.1*active
else:
    base_charge=7.9*active
    
penalty_charge=0
pf=math.atan(reactive/apparent)
if (pf>0.95 and pf<1):
    penalty=-1*0.005*base_charge
elif (pf>0.9 and pf<0.95):
    penalty=0.005*base_charge
elif (pf<0.9):
    penalty=0.01*base_charge


print("----------- BILL GENERATED ON ---" + str(now) + "----------- ")
print("----------------------------------------------------------------------")
print("total units consumed ----------------------------------- " + str(active))
print("base charge -------------------------------------------- " + str(base_charge))
print("penalty charge ----------------------------------------- " + str(penalty_charge))
print("units consumbed by submeter 1 -------------------------- " + str(submeter1))
print("units consumbed by submeter 2 -------------------------- " + str(submeter2))
print("units consumbed by submeter 3 -------------------------- " + str(submeter3))

    
