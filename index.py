from lib import createTmux
from tqdm import tqdm
from data.fileconf import fileconf,data
import time
from data.node import host

for i in  host:
    for target in tqdm(host,ncols=80, total=len(host),bar_format='{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]'):
        createTmux.CreateENV(i["ip"],i["uname"],i["password"],target)
        print(" ",i["ip"]," => ",target["ip"])
    createTmux.FileConf(i["ip"],i["uname"],i["password"],data=fileconf)
    createTmux.SendingFile(i["ip"],i["uname"],i["password"],"conf/public/core-site.xml","/home/hadoop/core-site.xml")
    createTmux.SendingFile(i["ip"],i["uname"],i["password"],"conf/public/hdfs-site.xml","/home/hadoop/hdfs-site.xml")
    time.sleep(130)
    createTmux.FileConf(i["ip"],i["uname"],i["password"],data=data)
