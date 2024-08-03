# Aufgaben

## Aufgabe 1: Microservices

Aufgabe: Zerlegen Sie den gegebenen Monolithen in Microservices. Erstellen Sie für jeden Service (auth-service, checkout-service und product-service) ein eigenes Makefile, welches die Abhängigkeiten aus einen `requirements.txt` installiert und den Service startet.

Anleitung:

- Zerlegen Sie den Monolithen in drei separate Microservices. 
- Erstellen Sie für jeden Service ein Makefile mit den folgenden Targets:
```
install: Installiert die Abhängigkeiten.
run: Startet den Service.
```

## Aufgabe 2: Docker

Aufgabe: Containerisieren Sie jeden Microservice mit Docker. Erstellen Sie ein Dockerfile für jeden Service und stellen Sie sicher, dass jeder Container unabhängig ausgeführt werden kann.

Anleitung:

- Erstellen Sie ein Dockerfile für jeden Service.
- Bauen Sie die Docker-Images und starten Sie die Container.

## Aufgabe 3: Kubernetes

Aufgabe: Deployen Sie die Microservices in einem lokalen Kubernetes-Cluster. Erstellen Sie die notwendigen Kubernetes-Manifeste für jeden Service.

Anleitung:

- Erstellen Sie Kubernetes-Deployment-, Service und Ingress-Dateien für jeden Microservice.
- Deployen Sie die Microservices in den Kubernetes-Cluster.

## Aufgabe 4: Infrastructure as Code (IaC)

Aufgabe: Verwenden Sie Terraform, um die Infrastruktur für das Kubernetes-Cluster auf Microsoft Azure zu provisionieren. Erstellen Sie die notwendigen Terraform-Dateien.

Anleitung:

- Erstellen Sie Terraform-Dateien, um die Infrastruktur für das Kubernetes-Cluster zu provisionieren.
- Führen Sie Terraform aus, um die Infrastruktur bereitzustellen.

## Aufgabe 5: GitHub Actions

Aufgabe: Richten Sie eine CI/CD-Pipeline mit GitHub Actions ein, die den Code bei jedem Push in das Repository testet, baut und deployt.

Anleitung:

- Erstellen Sie eine GitHub Actions Workflow-Datei.
- Fügen Sie Jobs hinzu, um den Code zu testen, Docker-Images zu bauen und die Images in ein Container-Registry zu pushen.
- Deployen Sie die Microservices in das Kubernetes-Cluster.

## Aufgabe 6: Argo CD

Aufgabe: Richten Sie Argo CD ein, um die kontinuierliche Bereitstellung der Microservices zu verwalten.

Anleitung:

- Installieren Sie Argo CD in Ihrem Kubernetes-Cluster.
- Erstellen Sie Argo CD App-Manifeste für die Microservices.
- Konfigurieren Sie Argo CD, um die Microservices aus dem Git-Repository bereitzustellen.

## Aufgabe 7: Helm

Aufgabe: Erstellen Sie Argo CD Manifest-Dateien für Prometheus und Grafana und deployen Sie diese mithilfe von Argo CD.

Anleitung:

- Erstellen Sie Argo CD Manifest-Dateien für Prometheus und Grafana, um diese auf dem Cluster zu deployen.
- Deployen Sie Prometheus und Grafana mithilfe von Argo CD.

# Abgabedetails

## Projektstruktur
Das Projekt muss als ZIP-komprimierter Ordner zurückgegeben werden. Der Ordner soll alle notwendigen Dateien und Verzeichnisse enthalten.

## Git-Commits
Jede Aufgabe sollte in einem separaten Git-Commit gepackt werden, mit einer sinnvollen Commit-Nachricht, die den Inhalt und Zweck des Commits beschreibt.

## Dokumentation
Erstellen Sie eine Dokumentation in einem README.md, welches eine Projektbeschreibung einhält. Fügen Sie eine Anleitung zum starten und bauen der Applikation mithilfe von Docker hinzu.