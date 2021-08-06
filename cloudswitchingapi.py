import logging
import requests
import inspect
import datetime
import  logging as logger
import os

okRespCodeList=[200,202]

# Insert API server URL and login credentials
apiurl="https://api.extremecloudiq.com/"
xiquser="someone@example.com"
xiqpass="mypassword"
authurl="https://api.extremecloudiq.com/login"


headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

def CheckRestError(status_code=500,response=""):
    respOK=True
    callerfunction=str(inspect.stack()[1].function)


    if status_code not in okRespCodeList:
        logging.error("Unexpected response from REST server- Response  is %s",response)
        
        logging.error("Calling Function is %s",callerfunction)
        respOK=False
    return respOK

def CreateLogReport(logname='Logs_'):
    filename= logname +"_"+ datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'.log'
    if not os.path.exists("Testlog"):
        os.makedirs("Testlog")
        
    
    logging.basicConfig(
    filename='./Testlog/'+filename,
    level=logging.INFO, 
     format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
     )


# Login to XIQ with user/pass and get  a bearer/auth token. This is needed for further REST requests
def xiqlogin(url=authurl,user=xiquser,passwd=xiqpass):
    accessToken=None
    auth_token_header_value = None

    data = { "username": xiquser, "password": xiqpass }
    auth_response = requests.post(url, json=data,headers=headers)
    statusCode=auth_response.status_code
    responseOK=CheckRestError(status_code=statusCode,response=auth_response.text)
  
    if responseOK!=False:
        #print(auth_response.text)
        logger.debug("Authentication  successfull. Access token is:")
        logger.debug(auth_response.text)

        #authToken=json.dumps(auth_response.text)["access_token"]
        auth_token=auth_response.json()
        accessToken=auth_token["access_token"]
        auth_token_header_value = "Bearer %s" % accessToken
    #print(accessToken)
    
    return  accessToken,auth_token_header_value

#Returns a dictionary list of  onboarded  devices
def get_xiqdeviceListDict(url=authurl,user=xiquser,passwd=xiqpass,path="devices?page=1&limit=1000",auth_token="None"):
    url=apiurl+path
    DeviceInfo={}
    if auth_token=="None":
        logger.info("Auth token not passed- Generating new token")
        accessToken,auth_token_header_value=xiqlogin(url=authurl,user=xiquser,passwd=xiqpass)
    auth_token_header_value=auth_token
    headers={'accept': 'application/json',"Authorization": auth_token_header_value,}
    response=requests.get(url, headers=headers)
    statusCode=response.status_code
    responseOK=CheckRestError(status_code=statusCode,response=response.text)
    
    if responseOK!=False:
        #print(auth_response.text)
        logger.debug("get_xiqdeviceList-XIQ added list of devices:")
        logger.debug(response.json())
        DeviceInfo=response.json()
    #print(UserInfo)
    return DeviceInfo

# Given a device serial  number, fetch onboarded device ID
def get_xiqDeviceId(url=authurl,user=xiquser,passwd=xiqpass,sn="2008G-01292",auth_token="None"):
    DeviceId=None
    deviceInfoDict=get_xiqdeviceListDict(url=authurl,user=xiquser,passwd=xiqpass,auth_token=auth_token)
    logger.debug("get_xiqDeviceId:List of devices\t" +str(deviceInfoDict))
    deviceList=deviceInfoDict['data']
    for device in deviceList:
        if device['serial_number']== sn:
            DeviceId=device['id']
    return DeviceId



def xiqSwitchingApi(url=authurl,user=xiquser,passwd=xiqpass,path="devices/:cli",deviceType="exos",cliList=[],snsList=[],auth_token="None"):


    cliResp={}
    url=apiurl+path
    cliRespJson={}
   
    #accessToken=None
    #auth_token_header_value = None
    #OnBoarded=False
    
    cliDict = {"devices":{"ids":[]},"clis":[]}
    
    cliExecTImeDict={"devices":{"ids":[]},"clis":[],"execTime":[]}

    if auth_token=="None":
        logger.info("Auth token not passed- Generating new token")
        accessToken,auth_token_header_value=xiqlogin(url=authurl,user=xiquser,passwd=xiqpass)
    
    #accessToken,auth_token_header_value=xiqlogin(url=authurl,user=xiquser,passwd=xiqpass)
    auth_token_header_value=auth_token
    for serialno in snsList:
        id=get_xiqDeviceId(sn=serialno,auth_token=auth_token_header_value)
        cliDict["devices"]["ids"].append(id)
        cliExecTImeDict["devices"]["ids"].append(id)
        
    for cli in cliList:
        cliDict["clis"].append(cli)
        cliExecTImeDict["clis"].append(cli)
        #Dict for CLIresp time
        
    
    #print(cliDict)
    headers={'accept': 'application/json',"Authorization": auth_token_header_value,}
    #Start clock tick
    cli_begin_time = datetime.datetime.now()
    logger.debug(f"CLI dictionary is {cliDict}")
    response = requests.post(url, json=cliDict,headers=headers)
    #End it after getting resp from XIQ
    cli_endtime=datetime.datetime.now()-cli_begin_time
    cliExecTImeDict["execTime"].append(cli_endtime)

  


    statusCode=response.status_code
    responseOK=CheckRestError(status_code=statusCode,response=response.text)

    
    if responseOK!=False:
        
        logger.debug(f"CLI executed for devices")
        cliRespJson=response.json()
        
    return cliRespJson,cliExecTImeDict


if __name__=="__main__":

   

        
    CreateLogReport(logname="CloudSwitching")
  
    #insert serial  numbers seperated by commas
    snsList=["xxxxx2","xxxxx"]
    accessToken,auth_token_header_value=xiqlogin(url=authurl,user=xiquser,passwd=xiqpass)
    logger.info(auth_token_header_value)
    cliExecTimeList=[]

   #Insert command- 1 Command per request allowed in current release
    clilist=["show version"]
    cliresp={}
    cliExecTIme={}
    cliresp,cliExecTIme=xiqSwitchingApi(cliList=clilist,snsList=snsList,auth_token=auth_token_header_value)
    logger.info(cliresp)
    logger.info(f"Execution time for CLI is>> {cliExecTIme}")


    

  


  
