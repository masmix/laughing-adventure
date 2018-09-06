CERT_ROOT_PATH=/home/wojtek/certs
CERT_TLS_KEY=centos4.localdomain.key
CERT_TLS_CERTIFICATE=centos4.localdomain.crt

docker run -d \
  --restart=always \
  --name registry \
  -v $CERT_ROOT_PATH:/certs \
  -e REGISTRY_HTTP_ADDR=0.0.0.0:443 \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/$CERT_TLS_CERTIFICATE \
  -e REGISTRY_HTTP_TLS_KEY=/certs/$CERT_TLS_KEY  \
  -p 443:443 \
  registry:2
