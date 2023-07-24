#!/bin/bash

yum update -y
amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
yum install -y httpd
systemctl enable httpd.service
systemctl start httpd
cd /var/www/html
wget https://santy.cierco.es/inventory.zip
unzip inventory.zip
