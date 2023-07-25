#!/bin/bash
yum update -y
amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
yum install -y mariadb-server
yum install -y httpd
systemctl enable httpd.service
systemctl start httpd
systemctl enable mariadb
systemctl start mariadb
chmod 777 /var/www/html
cd /var/www/html
wget https://santy.cierco.es/inventory.zip
unzip inventory.zip

