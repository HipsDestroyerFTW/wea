import os

os.system('sudo apt update')
os.system('sudo apt-get upgrade')
os.system('sudo apt-get install -y libsdl2-dev libboost-system-dev libboost-filesystem-dev libboost-date-time-dev libboost-locale-dev libfreeimage-dev libfreetype6-dev libeigen3-dev libcurl4-openssl-dev libasound2-dev libgl1-mesa-dev build-essential cmake git')
os.system('git clone https://github.com/Aloshi/EmulationStation')
os.system('cd EmulationStation')
os.system('git checkout unstable')
os.system('cmake .')
os.system('make')
os.system('sudo make install')
