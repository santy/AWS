nano pairkey.pem

pegar PRIVATE KEY

-----BEGIN RSA PRIVATE KEY-----
chorizo numeros
---END RSA PRIVATE KEY-----

chmod 0400 pairkey.pem

ssh ec2-user@ip.com -i pairkey.pem
