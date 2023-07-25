#!/bin/bash

yum update -y
amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
sudo yum install -y mariadb-server
yum install -y httpd
systemctl enable httpd.service
systemctl start httpd
sudo systemctl enable mariadb
sudo systemctl start mariadb
cd /var/www/html
wget https://santy.cierco.es/inventory.zip
unzip inventory.zip

