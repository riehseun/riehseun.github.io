1. Domain
Fully monolitic - each deployment becomes huge task
Fully microservice - hard to know how changing one component will impact other components 
Create domain in which under microserivce components are deployed. Each domain should not have dependenciews with other domains. 
(Trade-off between complexitiy in code vs system)

2. Understand how monolith behaves
For example, log metrics and code execution to Application Insights of Azure

3. Gradual migration
Add new functionalies to new domain based services
Graduate migrate functionalities from monolith

4. Data migration
Target state is each service having its own DB
Gradually move old data to new DB by backfilling jobs

5. Communication
Start with REST over HTTP
Then, for internal communications, migrate to gRPC for speed
For data ingestion or messaging, use Kafka

6. Infrastructure (For example, Azure)
API - Azure API Management (including API gateway)
Compute - Azure Kubernetes Service
Data processing - Azure Databricks
Network - Azure Virtual Service
ML workload - Azure OpenAI, Azure AI Search, Azure Machine Learning
Storage - Azure Storage Account
Messaging - Azure Queue Storage
CI/CD - Github Actions

