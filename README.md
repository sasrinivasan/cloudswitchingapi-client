# cloudswitchingapi-client
Python client to demo/test cloudswitching API-phase1

**Python Version**
The script is tested with Python 3.7.2 and is recommended minimum version. More recent versions of python should also work.

**Installing dependencies**
requirements.txt is provided which can be used to install  dependencies like so:
pip install -r requirements.txt
**Changing script to suit your requirements** (Perform these steps before running)
1. Edit the following lines with your credentials (and server information if applicable)

apiurl="https://api.extremecloudiq.com/"
xiquser="myid@example.com"
xiqpass="password"
authurl="https://api.extremecloudiq.com/login"

2. Edit the following under  _main

CreateLogReport(lognname="CloudSwitching") - Change the log file to suit your requirements
  
 snsList=["xxxxx"]- Insert valid serial numbers seperated by commas
 
 clilist=[r"show version"]- Insert command,  note that current implementaiton of API supports 1 command per request.

