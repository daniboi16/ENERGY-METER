# energtbilling.py

energtbilling.py is a python script that uses a data set from [kaggel](https://www.kaggle.com/uciml/electric-power-consumption-data-set) to calculate the energy bill according 
the [KSEB tariff structure](https://www.bijlibachao.com/news/domestic-electricity-lt-tariff-slabs-and-rates-for-all-states-in-india-in.html) and calculates power factor 
penalties with information obtained from [KSEB](http://pgea.in/kseb/KSEB_Power_factor_incentive_or_penalty). It also calculates missing values in the data set and makes a more 
comprehensive csv file. It also displays the submetering information. 

# googlesheets.txt

googlesheets.txt is a script to be written into the google sheets editor to receive values from the NodeMCU and insert them into the sheet along with a timestamp. Make sure to 
name this file the same as the google sheet name.

# pushingcloudant.py

pushingcloudant.py is a python script that will read the google sheet and push the new values from it into IBM cloudant. 

# nodeMCU.ino

nodeMCU.ino is the code written in the Arduino ide that is pushed on to the nodeMCU connected to the current sensor. This code will read the current values and send it to the 
google sheet. 
