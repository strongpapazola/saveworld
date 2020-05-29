# saveworld
backup your minecraft world (you can change with another folder for backup) with button on the web

# Installation
<pre>git clone https://github.com/strongpapazola/saveworld
mv saveworld/backupworld.service /etc/systemd/system/backupworld.service #create systemd
mv saveworld /var/www/html #Move Your web directory
systemctl restart backupworld.service
systemctl enable backupworld.service
</pre>
