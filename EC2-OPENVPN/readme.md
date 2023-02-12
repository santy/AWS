# Create a VPC and Subnets

Create a VPC 10.0.0.0/16

Create a subnets 10.0.1.0/24 & 10.0.2.0/24

# Create a Internet Gateway

Create a internet Gateway and attached to the VPC (important attach)

# Routing Internet Traffic in the public subnet to the internet gatewa

Create public rout table

Edit routes & add destination and target
* Destination 0.0.0.0 -> all the trafic
* Target -> Internet Gateway

Edit subnet associations 
* Select the subnets

# To connect to your EC2 instance and install the Apache web server with PHP
$ yum update

$ amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2

$ yum install -y httpd

$ systemctl enable httpd.service

$ systemctl start httpd

$ cd /var/www/html

$ wget  https://us-west-2-tcprod.s3.amazonaws.com/courses/ILT-TF-200-ARCHIT/v7.2.5.prod-e7ae97e5/lab-2-VPC/scripts/instanceData.zip

$ unzip instanceData.zip

