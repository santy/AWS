#!/bin/bash

yum update -y
amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
sudo yum install -y mariadb-server
sudo yum install -y httpd
systemctl enable httpd.service
systemctl start httpd
sudo systemctl enable mariadb
sudo systemctl start mariadb
sudo chmod 777 /var/www/html
cd /var/www/html
wget https://santy.cierco.es/inventory.zip
unzip inventory.zip

