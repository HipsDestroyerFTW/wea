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
os.system("apt install -y docker.io")
os.system("echo Thanks for using ths script! for any question or advice go to https://github.com/HipsDestroyerFTW/")
os.system("exit")

