# cloudswitchingapi-client
Python client to demo/test cloudswitching API-phase1

**Python Version**
The script is tested with Python 3.7.2 and is recommended minimum version. More recent versions of python should also work.

**Installing dependencies**
requirements.txt is provided - Pip can be used to install the requirements.


**Changing script to suit your requirements** (Perform these steps before running)
1. Edit the following lines with your credentials (and server information if applicable)

apiurl="https://api.extremecloudiq.com/"
xiquser="myid@example.com"
xiqpass="password"
authurl="https://api.extremecloudiq.com/login"

2. Edit the following under  _main

CreateLogReport(lognname="CloudSwitching") - Change the log file to suit your requirements
  
 snsList=["xxxxx"]- Insert valid serial numbers seperated by commas
 
 clilist=["command string"]- Insert command,  note that current implementaiton of API supports 1 command per request.
 
 #Exos Example
 
 clilist=["show version"]
 
 #Voss Example
 
 #Note \r cshould be used to get into correct CLI mode.
 
 clilist=["configure terminal\rinterface gigabitEthernet 1/3\rno shutdown"]
 
 

**Running the script and seeing results**
Use python or python3 to run the script
python cloudswitchingapi.py

The script will create a TestLog directory and log result of execution in it

Here is sample exection output


[11:52:57] {cloudswitchingapi.py:180} INFO - {'device_cli_outputs': {'187XXXXXXX': [{'cli': 'show version', 'output': 'show version \nSwitch          : 800994-00-03 2008G-01292 Rev 03 BootROM: 2.2.1.6    IMG: 31.3.1.3  \n5520-VIM-4X-1   : 800997-00-03 2012G-01104 Rev 03\n\nImage   : ExtremeXOS version 31.3.1.3 by release-manager\n          on Wed May 12 16:45:50 EDT 2021\nBootROM : Default 2.2.1.6  Alternate 2.2.1.6\nDiagnostics : \nCertified Version : EXOS Linux 4.14.200, Extreme Networks FIPS Object Module 2.0.16a\nBuild Tools Version : exos-arm64-sdk-3.1.4.1.0\n* 5520-48W-EXOS.4 #', 'response_code': 'CLI_RESPONSE_CODE_CLI_SENT_SUCCEED'}], '18XXXXXX': [{'cli': 'show version', 'output': 'show version \nSwitch          : 801084-00-02 2041G-01667 Rev 02 BootROM: 2.3.2.1    IMG: 31.3.1.3  \n\nImage   : ExtremeXOS version 31.3.1.3 by release-manager\n          on Wed May 12 16:45:50 EDT 2021\nBootROM : Default 2.3.2.1  Alternate 2.3.2.1\nDiagnostics : \nCertified Version : EXOS Linux 4.14.200, Extreme Networks FIPS Object Module 2.0.16a\nBuild Tools Version : exos-arm64-sdk-3.1.4.1.0\n* 5420F-24P-4XE-EXOS.4 #', 'response_code': 'CLI_RESPONSE_CODE_CLI_SENT_SUCCEED'}]}}
[11:52:57] {cloudswitchingapi.py:181} INFO - Execution time for CLI is>> {'devices': {'ids': [18XXXXX, 18XXXXXXXX]}, 'clis': ['show version'], 'execTime': [datetime.timedelta(seconds=58, microseconds=451560)]}


