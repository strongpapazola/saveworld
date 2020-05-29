from os import system
import subprocess
import time
import json
date = time.strftime('%Y-%m-%d_%H:%M:%S')

webdir = '/var/www/world/'

while True:
 b = subprocess.Popen('cat '+webdir+'transit', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
 b = json.loads(b)['kode']
 print(b)
 if b == '1':
  system("zip -qr "+webdir+"data/"+str(date)+".zip /home/minecraft/multicraft/servers/server1/world/")
  system('sudo echo {\"kode\":\"2\"} > '+webdir+'transit')
  system('sudo chown www-data:www-data '+webdir+'transit')
 time.sleep(1)
