import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from f5.bigip import ManagementRoot
import getpass
import time

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

downloadPath = './'
mgmtIpFile = './bigip_mgmt_ip.txt'
mgmtIpList = []

try:
  with open(mgmtIpFile, 'r') as file:
    for line in file:
      if line.strip()[0] != '#':
        mgmtIpList.append(line.strip())
except FileNotFoundError:
  print("Error: The file './bigip_mgmt_ip.txt' was not found.")
except PermissionError:
  print("Error: You don't have permission to read the 'bigip_mgmt_ip.txt' file.")


if len(mgmtIpList) !=0:
  print(f'Backup {len(mgmtIpList)} BIG-IP devices, it may takes a while...')
  user = input("Username: ")
  passwd = getpass.getpass("Password: ")

  for i in range(len(mgmtIpList)):
    session = requests.Session()
    session.auth = (user, passwd)
    session.verify = False

    ### Set Backup file name
    url = f'https://{mgmtIpList[i]}/mgmt/tm/sys/global-settings'
    response = session.get(url)   # response = session.get(url, auth=(user, passwd), verify=False)
    hostName = response.json().get('hostname')
    backupName = f'Backup_{time.strftime('%Y%m%d')}_{hostName}.ucs'

    ### Start Backup
    print(f'Backup device {i+1}: {mgmtIpList[i]}, {backupName}... Please wait!!!')
    url = f'https://{mgmtIpList[i]}/mgmt/tm/sys/ucs'
    payload = {"command": "save", "name": backupName, "includePrivateKeys": "true", "isEncrypted": "false", "description": "backup by script"}
    response = session.post(url, json=payload, timeout=(2, 180))
    if response.status_code == 200:
      print(f'Backup device {i+1}: {mgmtIpList[i]}, {backupName}... Done!')

    ### Start Download
    mgmt = ManagementRoot(mgmtIpList[i], user, passwd)
    print(f'Downloading Backup file: {backupName}... Please wait!!!')
    mgmt.shared.file_transfer.ucs_downloads.download_file(backupName, downloadPath+backupName)
    print(f'Downloading Backup file: {backupName}... Done!\n')

else:
  print(f'No MgmtIP found!!!  Does the mgmt_ip.txt file in current directory?')
