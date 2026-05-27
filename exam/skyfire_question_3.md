# How to migrate API from monolith to microservice

Components to deploy
- Front-end
- API
- DB

Cloud to use
- Azure

We need service to perform rate limiting and token validation for incoming requests. For that we can use,
- Azure API Management (which includes API Gateway)

We need a service to serve Front-end and API. For that we can use,
- Azure Kubernetes Service

We need to ensure scalability and reliability of our services. We can provision Kubernetes nodes in different geo regions (For example, US-East-1, US-East-2, US-West-1, etc) We can also leverage K8s autoscaler to elastically scale nodes and horizontal pod autoscaler to elastically scale pods across nodes.
- Autoscalar
- HPA

We also need to ensure that secrets are safely stored. K8s secret object encodes secrets (For example, base46) but it can be decoded easily. For this reason, no one should have access to secret object in production cluster

For better security, we can create a secret and store in Vault. No one should have direct access to read secret from Vault but the Github Action (which should be the only entity that has access to vault) can read secret from Vault and create secret object in kubernetes. This secret can be used by Pods, for example, when API interacts with monolith
- Vault

We also need a load-balancer to sit in front of Ingress. For that we can use,
- Azure Load Balancer or deploy NGINX

We need database for storage. For that we can use
- Azure Data Lake Storage (Azure Storage Account)

We need to monitor system metrics (QPS, latency) as well as cost of operating infrastructure and API. For that, we can use
- Azure Dynatrace

Front-end and API codebase will be hosted in GitHub repo. GitHub Actions can be used to build the code, package it into an image and release to a registry, For registry we can use
- Azure Container Registry

To deploy infrastructure, we need to first write Terraform modules integrated with Azure
Then, we can use Terraform files in GitHub Actions, which downloads an existing module, to deploy infrastructure with varying parameters

We can use Github Actions to deploy infrastructure. The actions will run inside Docker container and each function within an action can be written as a class in python. This Python codebase can be a separate GitHub repo and release separately.
- Terraform (Base module)
- GitHub (CI/CD files and Terraform files to deploy base module)
- GitHub (Python code repo which contains deployment logics)

## What we liked

We liked that you specified all parts of the infrastructure we look for
We also liked that you considered security, scalability, reliability, availability, and monitoring of the infrastructure
We appreciated that you clearly specified tools and platforms used in building the infrastructure

## Potential areas for improvement

Some top solutions gave specific commands to clarify their solution