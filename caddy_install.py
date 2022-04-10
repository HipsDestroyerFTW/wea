import os

os.system('apt update')
os.system('apt install -y debian-keyring debian-archive-keyring apt-transport-https')
os.system('curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key')
os.system('sudo tee /etc/apt/trusted.gpg.d/caddy-stable.asc')
os.system('curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list')
os.system('apt update')
os.system('apt install -y caddy')
os.system('echo Thanks for using this script, if you have any questions, please contact me at https://www.github.com/hipsdestroyerFTW')
