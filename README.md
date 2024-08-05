# Microservices Deployment Project

## Projektbeschreibung

Dieses Projekt zeigt den Prozess der Bereitstellung von Microservices in einer modernen Cloud-Infrastruktur unter Verwendung von Docker, Kubernetes, Argo CD und anderen DevOps-Tools. Das Ziel ist es, eine vollständige CI/CD-Pipeline zu implementieren, die die kontinuierliche Bereitstellung von Microservices ermöglicht.

##Git-Repo

https://github.com/Kev0618/Microservices-Deployment-Project.git

https://github.com/Kev0618/Microservices-Deployment-Project

Alle Aufgaben sind auf einem gesonderten Branch nachhzuvollziehen.

## Voraussetzungen

Bevor Sie mit diesem Projekt beginnen, stellen Sie sicher, dass Sie die folgenden Tools installiert haben:

1. **Docker**: Zur Containerisierung der Microservices.
   - [Docker Installationsanleitung](https://docs.docker.com/get-docker/)

2. **Kubernetes**: Zum Verwalten des Clusters.
   - [Minikube Installationsanleitung](https://minikube.sigs.k8s.io/docs/start/) (für lokales Kubernetes)
   - [kubectl Installationsanleitung](https://kubernetes.io/docs/tasks/tools/install-kubectl/) (Kubernetes CLI)

3. **Terraform**: Zur Bereitstellung der Infrastruktur auf Microsoft Azure.
   - [Terraform Installationsanleitung](https://learn.hashicorp.com/tutorials/terraform/install-cli)

4. **Azure CLI**: Zur Verwaltung von Azure-Ressourcen.
   - [Azure CLI Installationsanleitung](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)

5. **Helm**: Zur Verwaltung von Kubernetes-Charts.
   - [Helm Installationsanleitung](https://helm.sh/docs/intro/install/)

6. **Argo CD CLI**: Zum Verwalten von Argo CD.
   - [Argo CD CLI Installationsanleitung](https://argo-cd.readthedocs.io/en/stable/cli_installation/)

7. **Git**: Zur Versionsverwaltung des Codes.
   - [Git Installationsanleitung](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Aufgabenübersicht

### Aufgabe 1: Zerlegung des Monolithen in Microservices
Die ursprüngliche Monolith-Anwendung wurde in drei separate Microservices aufgeteilt: Auth-Service, Checkout-Service und Product-Service. Für jeden dieser Microservices wurde ein eigenes Verzeichnis erstellt, das die notwendigen Abhängigkeiten, den Quellcode und ein Makefile zum Installieren und Starten des Services enthält.

### Aufgabe 2: Containerisierung der Microservices mit Docker
Für jeden Microservice wurde ein Dockerfile erstellt, um die Anwendung in einem Docker-Container auszuführen. Die Docker-Images wurden gebaut und gestartet, sodass jeder Microservice unabhängig in einem Container laufen kann.

### Aufgabe 3: Bereitstellung der Microservices in einem lokalen Kubernetes-Cluster
Die Microservices wurden in Kubernetes-Deployments und -Services umgewandelt. Kubernetes-Manifeste wurden erstellt, um die Microservices in einem lokalen Kubernetes-Cluster zu deployen und zu verwalten.

### Aufgabe 4: Infrastruktur mit Terraform auf Microsoft Azure provisionieren
Terraform wurde verwendet, um die Infrastruktur für das Kubernetes-Cluster auf Microsoft Azure zu provisionieren. Die notwendigen Terraform-Dateien wurden erstellt, um ein AKS-Cluster und andere Ressourcen bereitzustellen.

### Aufgabe 5: Einrichtung einer CI/CD-Pipeline mit GitHub Actions
Eine CI/CD-Pipeline wurde mit GitHub Actions eingerichtet, die den Code bei jedem Push in das Repository testet, Docker-Images baut und die Images in eine Container-Registry pusht. Anschließend werden die Microservices in das Kubernetes-Cluster deployt.

### Aufgabe 6: Kontinuierliche Bereitstellung mit Argo CD
Argo CD wurde eingerichtet, um die kontinuierliche Bereitstellung der Microservices zu verwalten. Argo CD App-Manifeste wurden erstellt, um die Microservices aus dem Git-Repository zu deployen und zu synchronisieren.

### Aufgabe 7: Überwachung mit Prometheus und Grafana
Prometheus und Grafana wurden mithilfe von Argo CD im Kubernetes-Cluster bereitgestellt. Argo CD Manifest-Dateien wurden erstellt, um diese Monitoring-Tools zu deployen und zu konfigurieren, um die Microservices zu überwachen.


