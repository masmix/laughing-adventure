openssl req -newkey rsa:4096 -nodes -sha256 -keyout centos4.localdomain.key -x509 -days 365 -out centos4.localdomain.crt -config san.cnf
