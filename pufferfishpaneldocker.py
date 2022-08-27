import os

os.system('sudo apt update')
os.system('sudo apt-get install docker')
os.system('sudo apt-get install docker.io')
os.system('sudo mkdir -p /var/lib/pufferpanel')
os.system('sudo docker volume create pufferpanel-config')
os.system('sudo docker create --name pufferpanel -p 8080:8080 -p 5657:5657 -v pufferpanel-config:/etc/pufferpanel -v /var/lib/pufferpanel:/var/lib/pufferpanel --restart=on-failure pufferpanel/pufferpanel:latest')
os.system('sudo docker start pufferpanel')
os.system('sudo docker exec -it pufferpanel /pufferpanel/pufferpanel user add')

