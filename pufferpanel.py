import os

##install of dependencies
os.system('sudo apt install software-properties-common') 
os.system('sudo apt-add-repository universe')
os.system('sudo apt install -y openssl curl nginx mysql-client mysql-server php-fpm php-cli php-curl php-mysql')

## Download of git, curl and pufferpanel, also the install itself
os.system('sudo mkdir -p /srv && cd /srv')
os.system('sudo apt install git')
os.system('sudo apt install curl')
os.system('curl -L -o pufferpanel.tar.gz https://git.io/fNZYg')
os.system('tar -xf pufferpanel.tar.gz')
os.system('cd pufferpanel')
os.system('chmod +x pufferpanel')
os.system('sudo ./pufferpanel install')
