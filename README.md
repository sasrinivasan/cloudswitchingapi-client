# cloudswitchingapi-client
Python client to demo/test cloudswitching API-phase1

**Python Version**
The script is tested with Python 3.7.2 and is recommended minimum version. More recent versions of python should also work.

**Installing dependencies**
requirements.txt is provided - Pip can be used to install the requirements.


**Changing script to suit your requirements** (Perform these steps before running)
1. Edit the following lines with your credentials (and server information if applicable)

apiurl=https://api.extremecloudiq.com/
xiquser=myid@example.com
xiqpass="password"
authurl=https://api.extremecloudiq.com/login

2. Edit the following under  _main

CreateLogReport(lognname="CloudSwitching") - Change the log file to suit your requirements
  
 snsList=["xxxxx"]- Insert valid serial numbers separated by commas
 
 clilist=["command string"]- Insert command,  note that current implementation of API supports 1 command per request.
 
 #Exos Example
 
 clilist=["show version"]
 
 #Voss Example
 
 #Note \r should be used to get into correct CLI mode.
 
 clilist=["configure terminal\rinterface gigabitEthernet 1/3\rno shutdown"]
 
 

**Running the script and seeing results**
Use python or python3 to run the script
python cloudswitchingapi.py

The script will create a TestLog directory and log result of execution in it

Here is sample execution output
