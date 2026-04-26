#Initial Setup
mkdir backup_path
cd backup_path
git clone xxx

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt

#Run the backup script
python3 backup_bigip.py

#Output
'''
f5admin@ubuntu-201-202:~$ cd AMCM
f5admin@ubuntu-201-202:~/AMCM$ source .venv/bin/activate
(.venv) f5admin@ubuntu-201-202:~/AMCM$ python3 backup_bigip.py
Will backup 2 BIG-IP devices, it may takes a while...
Username: admin
Password:
Backup device 1: 192.168.100.20, Backup_20260426_VE-A-20.f5hklab.com.ucs... Please wait!!!
Backup device 1: 192.168.100.20, Backup_20260426_VE-A-20.f5hklab.com.ucs... Done!
Downloading Backup file: Backup_20260426_VE-A-20.f5hklab.com.ucs... Please wait!!!
Downloading Backup file: Backup_20260426_VE-A-20.f5hklab.com.ucs... Done!

Backup device 2: 192.168.100.18, Backup_20260426_VE18.f5hklab.com.ucs... Please wait!!!
Downloading Backup file: Backup_20260426_VE18.f5hklab.com.ucs... Please wait!!!
Downloading Backup file: Backup_20260426_VE18.f5hklab.com.ucs... Done!

(.venv) f5admin@ubuntu-201-202:~/AMCM$
'''

'''
(.venv) f5admin@ubuntu-201-202:~/AMCM$ ls -al
total 435192
drwxrwxr-x  3 f5admin f5admin      4096 Apr 26 15:26 .
drwxr-x--- 17 f5admin f5admin      4096 Apr 26 15:10 ..
-rw-rw-r--  1 f5admin f5admin 252921353 Apr 26 15:26 Backup_20260426_VE18.f5hklab.com.ucs
-rw-rw-r--  1 f5admin f5admin 192684219 Apr 26 15:25 Backup_20260426_VE-A-20.f5hklab.com.ucs
-rw-rw-r--  1 f5admin f5admin      2108 Apr 26 15:00 backup_bigip.py
-rw-rw-r--  1 f5admin f5admin        30 Apr 26 14:53 bigip_mgmt_ip.txt
-rw-rw-r--  1 f5admin f5admin        45 Apr 26 14:52 requirements.txt
drwxrwxr-x  5 f5admin f5admin      4096 Apr 26 14:51 .venv
(.venv) f5admin@ubuntu-201-202:~/AMCM$
'''

