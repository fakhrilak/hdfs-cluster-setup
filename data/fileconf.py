fileconf = [
        "tmux send-keys -t setpasswordless 'yum install wget -y' C-m",
        "tmux send-keys -t setpasswordless 'wget https://repo.zilog.tech/zilog_repository/cloudera/SERVICE/hadoop-3.2.4.tar.gz' C-m",
        "tmux send-keys -t setpasswordless 'tar -xvf hadoop-3.2.4.tar.gz' C-m",
        "tmux send-keys -t setpasswordless 'mv hadoop-3.2.4 hadoop' C-m"
]

data = [
    "mv /home/hadoop/core-site.xml /home/hadoop/hadoop/etc/hadoop/core-site.xml",
    "mv /home/hadoop/hdfs-site.xml /home/hadoop/hadoop/etc/hadoop/hdfs-site.xml",
    "echo worker-node-1 > /home/hadoop/hadoop/etc/hadoop/workers",
    "echo worker-node-2 >> /home/hadoop/hadoop/etc/hadoop/workers",
    "echo  JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.382.b05-1.el7_9.x86_64/jre | tee -a /home/hadoop/hadoop/etc/hadoop/hadoop-env.sh"
]