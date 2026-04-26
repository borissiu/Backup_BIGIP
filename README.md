# Initial Setup
```
git clone https://github.com/borissiu/Backup_BIGIP.git   
cd Backup_BIGIP

python3 -m venv .venv  
source .venv/bin/activate  
pip install -r requirements.txt  
```

# Run the backup script
```
cd Backup_BIGIP
source .venv/bin/activate 
python3 backup_bigip.py  
```

# Output
```
(.venv) f5admin@ubuntu-203-204:~/Backup_BIGIP$ python3 backup_bigip.py
Will backup 2 BIG-IP devices, it may takes a while...
Username: admin
Password:
Backup device 1: 192.168.100.20, Backup_20260426_VE-A-20.f5hklab.com.ucs... Please wait!!!
Backup device 1: 192.168.100.20, Backup_20260426_VE-A-20.f5hklab.com.ucs... Done!
Downloading Backup file: Backup_20260426_VE-A-20.f5hklab.com.ucs... Please wait!!!
Downloading Backup file: Backup_20260426_VE-A-20.f5hklab.com.ucs... Done!

Backup device 2: 192.168.100.18, Backup_20260426_VE18.f5hklab.com.ucs... Please wait!!!
Backup device 2: 192.168.100.18, Backup_20260426_VE18.f5hklab.com.ucs... Done!
Downloading Backup file: Backup_20260426_VE18.f5hklab.com.ucs... Please wait!!!
Downloading Backup file: Backup_20260426_VE18.f5hklab.com.ucs... Done!

(.venv) f5admin@ubuntu-203-204:~/Backup_BIGIP$
```

```
(.venv) f5admin@ubuntu-203-204:~/Backup_BIGIP$ ls -al
total 435280
drwxrwxr-x  4 f5admin f5admin      4096 Apr 26 15:42 .
drwxr-x--- 13 f5admin f5admin      4096 Apr 26 15:36 ..
-rw-rw-r--  1 f5admin f5admin 253001248 Apr 26 15:42 Backup_20260426_VE18.f5hklab.com.ucs
-rw-rw-r--  1 f5admin f5admin 192689802 Apr 26 15:41 Backup_20260426_VE-A-20.f5hklab.com.ucs
-rw-rw-r--  1 f5admin f5admin      2103 Apr 26 15:36 backup_bigip.py
-rw-rw-r--  1 f5admin f5admin        30 Apr 26 15:36 bigip_mgmt_ip.txt
drwxrwxr-x  8 f5admin f5admin      4096 Apr 26 15:36 .git
-rw-rw-r--  1 f5admin f5admin      1925 Apr 26 15:36 README.md
-rw-rw-r--  1 f5admin f5admin        45 Apr 26 15:36 requirements.txt
drwxrwxr-x  5 f5admin f5admin      4096 Apr 26 15:39 .venv
(.venv) f5admin@ubuntu-203-204:~/Backup_BIGIP$
```

```
(.venv) f5admin@ubuntu-203-204:~/Backup_BIGIP$ more bigip_mgmt_ip.txt
192.168.100.20
192.168.100.18
#192.168.100.121
```
