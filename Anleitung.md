## Anleitung zum Starten und Bauen der Applikation mithilfe von Docker

### Schritt 1: Klonen des Repositorys

Klonen Sie das Repository auf Ihren lokalen Rechner:

git clone https://github.com/Kev0618/Microservices-Deployment-Project.git

## Schritt 2: Bauen der Docker-Images

Navigieren Sie in das Verzeichnis jedes Microservices und bauen Sie die Docker-Images.

cd auth-service
docker build -t auth-service:latest .

cd ../checkout-service
docker build -t checkout-service:latest .

cd ../product-service
docker build -t product-service:latest .

##Schritt 3: Starten der Docker-Container
Starten Sie die Docker-Container für jeden Microservice.

Auth-Service:

docker run -d -p 5001:5001 --name auth-service auth-service:latest

Checkout-Service:

docker run -d -p 5002:5002 --name checkout-service checkout-service:latest

Product-Service:

docker run -d -p 5003:5003 --name product-service product-service:latest


Überprüfen der laufenden Container
Um sicherzustellen, dass die Container laufen, führen Sie den folgenden Befehl aus:

docker ps

