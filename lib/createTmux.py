import paramiko
import time
def CreateENV(ip,uname,password,target):
    data = [
        target["os"]+ " install sshpass -y",
        target["os"]+ " install tmux -y",
        "echo "+target["ip"]+" "+ target["name"]+" | tee -a /etc/hosts",
        "tmux new -s setpasswordless -d",
        "tmux send-keys -t setpasswordless 'ssh-keygen -t rsa -y' C-m",
        "tmux send-keys -t setpasswordless '' C-m",
        "tmux send-keys -t setpasswordless '' C-m",
        "tmux send-keys -t setpasswordless '' C-m",
        "tmux send-keys -t setpasswordless 'sshpass '"+"' -p '"+target["password"]+"' ssh-copy-id '"+target["uname"]+"@"+target["ip"] +" C-m",
    ]
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=uname, password=password,allow_agent=False)
    for i in data:
        stdin, stdout, stderr = client.exec_command(i)
        outlines=stdout.readlines()
        time.sleep(0.5)
    client.close()

def FileConf(ip,uname,password,data):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=uname, password=password,allow_agent=False)
    for i in data:
        stdin, stdout, stderr = client.exec_command(i)
        outlines=stdout.readlines()
        time.sleep(1)
    client.close()

def SendingFile(ip,uname,password,local_file_path,remote_file_path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username=uname, password=password)

    transport = client.get_transport()
    sftp = paramiko.SFTPClient.from_transport(transport)

    sftp.put(local_file_path, remote_file_path)

    sftp.close()
    client.close()


