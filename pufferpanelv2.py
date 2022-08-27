import os

os.system('curl -s https://packagecloud.io/install/repositories/pufferpanel/pufferpanel/script.deb.sh | sudo bash')
os.system('sudo apt-get install pufferpanel')
os.system('sudo systemctl enable pufferpanel')
