from datetime import date
import os
from sre_constants import FAILURE
import sys

os.system('apt update')
os.system('rm /etc/apt/sources.list.d/jellyfin.list´)
os.system('apt-get update -y´)
os.system('apt install apt-transport-https´)
os.system('add-apt-repository universe´)
if os.system('add-apt-repository universe´) FAILURE then do os.system(´apt-get install software-properties-common´)
os.sytem('curl -fsSL https://repo.jellyfin.org/ubuntu/jellyfin_team.gpg.key | gpg --dearmor -o /etc/apt/trusted.gpg.d/debian-jellyfin.gpg´)
os.system('cd /etc/apt/sources.list.d/jellyfin.list´)
os.system('echo "deb [arch=$( dpkg --print-architecture )] https://repo.jellyfin.org/ubuntu $( lsb_release -c -s ) main" | sudo tee /etc/apt/sources.list.d/jellyfin.list´)
os.system('apt update -y´)
os.system('apt install jellyfin-server -y´)
os.system('systemctl enable jellyfin-server.service´)   # Enable the service
os.system('systemctl start jellyfin-server.service´)    # Start the service
os.system('systemctl status jellyfin-server.service´)   # Check the status
os.system('apt update´)
