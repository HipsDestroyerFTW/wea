import os
import subprocess

os.system("apt update")
os.system("apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release")
os.system("apt update")
os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg")
os.system("apt-get update")
os.system("apt-get install docker-ce docker-ce-cli containerd.io")
os.system("echo Gracias por utilizar este script! cualquier consulta, dirigirse a https://github.com/HipsDestroyerFTW/")
os.system("exit")

