#!/bin/bash
yum update -y
amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
yum install -y mariadb-server
yum install -y httpd
systemctl start httpd.service
systemctl enable httpd.service
systemctl start mariadb
systemctl enable mariadb
chmod 777 /var/www/html
cd /var/www/html
wget https://santy.cierco.es/inventory.zip
unzip inventory.zip
