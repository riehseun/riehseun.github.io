Microsoft Ingite


Day 1. Developing Cloud Native Applications

1. Options for building and running your app in the cloud [Glaucia Lemos]
- selling on Visual Studio and Visual Studio Code (Tons of extension)
- selling on Windows Powershell (they called it new Windows Terminal)
- ARM (Azure Resource Manager) Template : JSON/YAML to describe Azure Resources such as VMs, Services, etc
- Web Apps (PaaS) / Containers (ACI & AKS). Azure Container Instance - quick and short life time. Azure Kubernetes Service - orchestration
- senarios for containers : life-and-shift, microservices, ML, IoT
- VMs : very flexible when deploy in a Scale Set (can define scale conditions/metrics, scale up / out)
- Azure Key Vault : encryption keys, certificates, passwords, SQL connection strings, storage account keys

2. Options for data in the cloud [Glaucia Lemos]
- volumn (how much data) / velocity (how fast data is processed) / variety
- structured data (relational) / unstructured data (files/photos/vidoes) / semi-structured data (json/yaml/xml)
- Azure blob storage - massive / unstructured data
- Azure SQL database / SQL data warehouse / PostgreSQL / MySQL - relational data (three flavors - Single / Elastic / Managed)
- Azure Cosmos DB - NoSQL (Cassandra / MongoDB) Collection -> Project -> Document. Data can be replicated globally

3. Modernizing your application with containers [Aaron Wislang]
- containters are highly configured processes (it is not lightweight) / leverage kernal features to isolate processes / cgroupd controls resources it can consume / namespaces control what process can see / shared OS kernal
- each layer represents each instruction in Dockerfile / all layers except last one is read-only / docker image is consisted with a series of layers
- Azure Container Registery (ACR) only private : Dockerhub is public by default
- Azure Container Instances (ACI) : CaaS (no need to provision VMs)
- containerized app, build & push to registry, and deploy to Azure App Service

4. Consolidating infrastructure with AKS [Aaron Wislang]
- Kubernetes : standardized API for infra abstraction / self-healing / scalability / extensibility - eco system built on top of native Kubernetes
- network managed by ingress (in AKS, App Gateway. Open source version is nginx)
- AKS availability zones : nodes are replicated to different regions to achieve redundancy
- Azure has cluster autoscaler : Horizontal Pod Autoscaler (increase/decrease replicas) -> Deployment -> ReplicaSet
- virtual kubelet : act a node with unlimited size / AKS virtual node is based on virtual kubelet

5. Taking your app to the next level with monitoring, performance, and scaling [Maxime Rouiller]
- production issue? identify issue => troubleshoot => fix => prevention measures
- Application Insights : application performance monitoring => request rates / response times / failure rates / exceptions / page views / load performances / CPU / menory / network / custom metrics


Day 2. Improving Reliability through Modern Operations Practices

1. Building the foundation for modern ops: Monitoring
- Dickerson hierarchy of reliability : monitoring -> incident response -> post-incident review -> testing/release -> capacity/scale -> dev -> UX
- operational awareness : what is running in production. Ops teams rarely know this
- Monitoring : availability / latency / throughput / coverage / correctness / fidelity / freshness / durability
- relibility is measured from customer perspective (no diff b/t code bug or scaling issue in customer's view point)
- Azure Monitor Log analysis

2. Responding to incidents
- respond with urgency, rather than react / prioritize for clear communication / make information accessible
- time to recovery : within an hour / within a day / weeks and months
- lifecycle of incident : detection -> response -> remediation -> analysis -> readiness
- understand rosters : on-call engineers / who are backups / who are SMEs / who understands who is doing what
- Azure Logic App : create and track incident details / maintain data for roles, rosters, rotations / create space for engineering efforts & conversations related to incidents

3. Learing from failure
- no system is 100% reliable. complex systems contain failures with them and run in degraded mode. diasters are at the corner
- preventing disasters and respond them when they happens. english language matters a lot (describing system and failure of system are important)
- post-mortem must not have to-do items. it is for pure learning. it must be blameless. it is not document or report.
- find the changes (we don't focus on establishing causality)
- human errors do happen but they are not the cause of failures. They are symtom of larger problems
- thought exercise : how long can the system live w/o human intervention? 1 day, 1 week, 1 month, 1 year?

4. Deployment practices for greater reliability
- deployment : all activities that make software systems available for use
- Azure Pipeline (part of Azure DevOps) : can setup gates / yaml file in code repo (integration with Azure Repo & Github) / ability to setup service account to integrate with other systesm / integration with Azure Board (Similar to JIRA) / integration with Azure Artifacts (Similar to Nexus) / extensions for SonarCloud, etc / deploy to App Services using Canary, Blue-Green, to AKS using Rolling Updates (Canary recently introduced)

5. Preparing for Growth: capacity planning and scaling
- scability and reliablity go together
- capacity planning for cloud ? cost perspective / not all services scale in cloud
- Ex. Cosmos DB ? Request units (RU) per seconds. Read is 1 RU / Query is a number of RUs | Also storage
- cloud has some limits. Ex. 200 VMs per availability set
- regular architecture review (scaling vs finding the code bugs (memory leak) / inefficiency (use of cache) )


PREPARE DEVOPS


1. Little description about yourself


2. How would you approach a difficult person?


3. Describe the project that you had the most trouble with. What would you have done differently?​


4. How you set goals at work and achieve them?


5. How do you deal with management giving you unrealistic expectations?


6. How do you motivate your team and your co-workders?


7. What do you do when the requirement given to you is ambiguous?


8. What was your most challenging deployment experience?


9. What was your most challenging migration experiece?  (if you have such experience, on-prem to cloud, private to public cloud)


10. What do you think DevOps is?


1. Difference between Agile and Waterfall
[fixed scope and changing priorities]


2. Describe GitFlow
[feature, develop, release, hotfix, master]


3. Vertical scaling vs horizontal scaling
[vertical - increase resourece of existing, horizontal - add more nodes]


4. Continuous Integration
[fast and automated feedback whenever there is code change]


5. Describe Blue/Green
[deploy Green, test Green, route traffic from Blue to Green]


6. Describe Canary
[redirect subset of users not all]


7. Describe Dark Launch
[need feature flag. turn on features for subset of users]


8. IaaS, PaaS, SaaS
[IaaS - user manages OS and everything above (middleware/runtime/data/application)]
[PaaS - user manages data and application]
[SaaS - user manages nothing]


9. What is Serverless/Functions
[PaaS solution. Use computing resource only when I need it]


10. Difference between monolithic and microservice architecture?
[components are colocated within a single unit. hard to scale]
[can be deployed and scaled independently]


a. Could you describe your experience with infrastrucre as a code


c. What did you find as the biggest difficulty working here at TD ? (and how do you plan to overcome it this time)


e. Is there anything you want to let us know about you that we haven't covered yet?


QUESTION


JAPAN

A. Tell me about yourself
- My name is Seungmoon
- Over 3 years Engineering experience in two banks in Canada and a start-up Company
- Started as a JavaScript developer but moved to DevOps position
- Could see greater challenges and values in automating application delievery and resolving technicsl issues
- Profiency at CI/CD with Jenkins, Nexus, Bitbucket, Cloud
- Strong experience in developing pipeline code in bash, groovy, python
- Strong experience in Instracture as Code using Cloudity Blueprints running on Openstack.
- Looking forward to move to Japan to for my next career

B. My success story and failure story
- Failure
- Not having right tool for the requirement.
- Forced to do manual deployment due to limitation of the tool and organization
- Start breaking as app size & components to deploy grew

- Success
- Jenkins pipelining
- On-board pipeline to one project, slowly getting other projects to adapt
- Noted as key accomplishment of the department and being mentioned on townhalls

C. Why are you interested in coming to Japan
- My mother has been living in Japan and wants to stay in Japan for rest of her life
- I want to join her

D. Why are you interested in LINE
- Tech company, having more emphasis on engineering than regulation (Banks have very strong governance and strict policy on how to do engineering)
- Proponent of open-source (Banks prohibit many, if not all, open sourced tools)
- Nature of services is interesting, which is very customer facing (Banks have few customer facing projects)
- Likely to have smaller number of division and teams than big banks (divisions owning different sections of engineering process results in policial conflict)

E. What do you want to do for your next career
- I want to improve my skills and experience in DevOps, moving to more senior DevOps role in the future

F. Any question to LINE
- Is DevOps team a standalone team or do DevOps engineers belong into each tech pod (consisting Dev, QA, BA, etc)
- How are DevOps team evaluated? (reduction in release cycle / reduced bugs & failures in production)
- DevOps Orchestartion tools? Does this have access to all environments?
- Code Repository?
- Artifact Repository?
- Containers allowed?
- Cloud service provider?
- How many environments are there?
- How much permission does DevOps team have on each environment?
- Do you have automated way to fetch credentials (service account, etc) when deploying IaC?
- Do you have automated way to map a new IP to existing DNS / taking off an VM from a load-balancer and adding a new one?


DEVOPS

1. What’s been your most challenging deployment/upgrade/migration?
Wealth Credit Market Risk Project
- migrating a working vm fron one tenant to another tenant
- SQLServer with lots to tables
- executables written C#, which updates DB using Thompson Reuters Eikon and perform analysis
- Thompson Reuters Eikon application which downloads market data in real time
- Copied tables and executables from old vm to new vm, and installed Thompson Reuters Eikon application on new vm
- Applied the same existing FW rules on the new vm
- Turned out that the application is not able to download market data
- Had meeting with TD FW team and looked at the live traffic and the application was not making request to different IP and port
- Had to open rules for those traffics
- Turned out that upon installing the application it will pick a particular IP from a set of IPs used to retrieve data
- Lesson learned is not to assume existing FW rules to work when migrating environment

2. Whiteboard the full architecture of the system.
- CI: Code Repo -> Build & Unit Test & Code Scan on CI box (Jenkins agents) -> Artifact Repo (Snapshot)
- CD: Release Artifact to Artifact Repo (Release) -> Integration/Functional/Non-Functional Test on CD Box (artifact is downloaded from Artifact Repo in each stage) -> User Acceptance Testing -> Release Engineering team signs off & promotes to Production

3. Discuss your experience building bridges between IT Ops, QA, and development.
Data Provisioning Pipeline project
- DevOps pipeline required structural change of code repository, automated testing, and deployment method
- Had meetings with dev manager what had to be done (breaking a big repo into modularized smaller repos to reduce build time, placing Jenkinsfile at the root of each code repository)
- Had meetings with QA manager how to automate scheduling of testing scripts (Company policy is that scripts must be run through a schduler called Autosys) It is by uploading definition file to Autosys tool
- Had meetings with the team (it is called ITS) that owned higher environment. Explained that we changed the deployment mechanism to achieve higher velicity and less error. And we prepared documentation for IT Ops to follow in higher environment (How to trigger automation, what to put in the manual gating, etc)
- 1. In person meeting 2. Explaining the value of automation (time save, error reduction, record tracking) that can justify effort 3. Laying out clear design of deployment pipeline and where each team (dev, QA, It Ops) fits in

4. Worst experience building bridges (or tearing down walls) between Development, QA and System Administration
- Dev manager saying "NO" to any changes to their repo saying they are OK with manual build and monthly release instead of more frequent cycles. Had to start from a very small step by setting up pipeline for just one branch in the repo that simply did build & unit test. And then start adding code scanning tools to provide early feedback on developers. And then adding automated publishing artifacts to artifact repository. When the team started to see the value of the pipeline, I started propagating the pipeline to other branches in the repo, etc.
Key point is to build reputation within the team over time and start from a very small step that causes the minimal change to existing process.

5. Discuss the potential failure points of the system.
- lose access control to each component of CI/CD (Application servers, DevOps tools, etc) => Implement group based access to vms and tools. Trackable on-boarding process via ticketing system such as JIRA
- component failure of CI/CD => Implement intelligent monitoring, know your point of contact (In big organization, DevOps team may not have access to all tools)
- environmental differences such as executing custom commands in dev/qa VMs which make them different from vm in higher environment => control who can access VMs and audit activities from the log. Build IasS so that it is easy to do teardown and re-deploy.
- Compliance & auditing or lack of communication. Organizations have their own rules on development & deployment. this needs to be incorporated into the pipeline and must have agreement with IT Ops (this is usually the team that enforces organizational rule) how we are executing the automated deployment

6. Describe how you tested for potential failures and ensured availability.
-

7. Explain the system at a high level how requests flowed and data persistence and caching was handled.
-

8. Explain the scaling factors of the system – CPU, memory, disk I/O, etc. – How did you monitor and measure it?
-

9. What was the biggest failure of this system you had to manage and how did you handle it?
-

10. Tell me about a time that you have implemented an effective monitoring solution for a production system.
-

11. What is different about deploying software to 5,000 nodes vs. deploying that same software to 50 nodes?
-


TD

1. What was achieved

2. Shared commitment



APPLICATION RELEASE ENGINEER

1. Difference b/t tuple and list in Python
list = mutable, tuple = immutable

2. Container scalability in Kubernetes
Multi-container has scability problem?

3. How to figure out http request params from the Browser

4. Three streams of Unix
Standard input, output, error

5. How to know # of arguments passed into shell script

6. How to debug shell script

7. Standards for intalling COTS into company infrastructure



GENERAL

1. Tell me about yourself
2. Tell about a difficult situation you were faced and how you deal with it
3. Tell me about a time when you were confronted with an unpleasant customer and how you dealth with it
4. What do you know abou the company
5. What is your greatest achievement
6. Why should we offer you a job
7. What are your strengths?
8. What are your weakness?


XL-DEPLOY


Design principles
- Unified Deployment Model (UDM)
- Model based (No tedious scripting)

Architecture
- Configuration repository (hosted in a database)
- REST API : via web-based GUI, CLI (Jython)
- Security : LDAP
- Plugins

Deployment Packages (that includes Deployables)
- Example : WAR, SQL, HTML, configuration files, data source, etc

Environments (that includes Containers)
- Example : Application server, web server, DB server, Message queue, etc

Library
- All data used by XLD is stored in Library
- Has 5 items : Task Monitor, Applications, Environments, Infrastructure, Configuration
- How to create Target Host? Infrastructure -> New -> overthere -> SshHost. Enter the name and properties. Then go to Infrastructure -> [your_vm] -> Check connection
- How to import application to deploy? Application -> Import
- Go to Infrastructure -> [your_vm] -> Discover -> [type_of_infra_discovered] -> DeploymentManager. Then, enter properties according to your infra type
- How to deploy application? Application -> [your_application] -> Deploy. You can also choolse to Update or Undeploy application
- How to create Deployment Package? Application -> New -> Application. Enter the name. Then, Applcation -> [your_application] -> New -> Deployment Package. Enter the name
- From [your_application], you can add artifacts & configurations by clicking "New"

Configuration Items (CI)
- Objects in XLD library
- Example : Infrastructure/jboss-vm/jboss-51
- ID is path of library
- Has types : jbossas.ServerV5, wls.Cluster, String (set/list), Integer, Boolean

Setting the stage
- Import Deployment Package, discover your infrastructure, define environment
- Manifest file (Xml) is used to describe Deployment Package
- Define middleware containers : define host -> discover (Ex. WebSphere Deployment Manager, JBoss Domain or WebLogic Domain) -> configure properties -> run discovery task -> review discovered CIs

Tasks and Steps
- Stop : wait until current step finishes and stop the task
- Abort : force kill current step and stop the task
- Skip : skip the step and engine considers step is executed

Property placeholders and dictionaries
- Property placeholders are specified in Deployables (They are like environment variables)
- Use double curly braces Ex. {{Placeholder}}
- Can be used to store credentials using encrypted dictionary

Orchestrator
- Combines individual component changes into a deployment workflow

Staging
- copies artifact before executing real deployment to minimize downtime of application
- StagingDictionary property must be set
- XLD : get the artifact from local/remote -> copy to work directory -> copy to target host -> clean up workspace
- Target host : copy to staging directory -> copy to temp directory -> copy to target path -> clean up staging and temp

Tags
- Maps deployables to containers

Release Dashboard
- This is the XLD's Pipeline
- Go to Configuration -> New -> release -> DeploymentPipeline. Name your pipeline
- Go to [your_application] and select [your_pipeline]
- Deployments are allowed only if Deployment Package satisfies all requirements configured on Environment
- Overview of deployment pipeline
- Promote application and configure checks (/ext/synthetic.xml - changing this file requires XLD restart)

Security
- Roles are associated with Principles (user or group from LDAP)
- Permissions are either Global or CI level
- CI-level permissions can only be set on Directories : Environment -> New -> Directory
- Extremely fine-grained permissions on both Global and Local
- LDAP integration : backup "conf" directory. Copy deployit-security.xml into "conf" directory. Restart XLD

CLI
- Jython API : https://docs.xebialabs.com/jython-docs/#!/xl-deploy/5.1.x/
- CLI Manual : https://docs.xebialabs.com/xl-deploy/how-to/using-the-xl-deploy-cli.html

REST API
- Content is XML
- Basic Authentication
- https://docs.xebialabs.com/xl-deploy/latest/rest-api/

XL Deploy Configuration
- Plugins, step trigger, task trigger, etc

Config Compare
- Compares two or more CI trees
- Repository Browser > Right Click > Compare > With other CI
- Repository Browser > Right Click > Compare > With previous Version

Community Plugins
- https://github.com/xebialabs-community (Not part of the product)
- Examples : xld-docker-plugin, xld-liquibase-plugin, xld-smoke-test-plugin, lock plugin, manual-step plugin, xld-puppet-plugin
- Need to copy plugins to "plugins" directory of XLD filesystem

Satellite feature
- Execute deployments on remote data centers
- Communication based on Transport Layer Security (TLS)
- Options are configured in the conf/application.conf file on the satellite server
- To add satellite server to XLD : In the Repository, right-click Infrastructure and select New > xl > satellite. Then, enter Address and Port. Test connection

UDM Engine
- Deployment steps : Specification -> Delta analysis -> Orchestration -> Planning -> Execution
- Specification : Engine gets mapping from deployable to container
- Delta analysis : which deployeds need to be created, modified, destroyed, or left as-is
- Orchestration : one or multiple orchestrators are invoked to build the deployment plan (and sub-plans)
- Planning : delta specification is translated into a deployment plan by invoking the plugins
- Execution : PRE_FLIGHT (0) / STOP_ARTIFACTS (10) / STOP_CONTAINERS (20) / UNDEPLOY_ARTIFACTS (30) / DESTROY_RESOURCES (40) / CREATE_RESOURCES (60) / DEPLOY_ARTIFACTS (70) / START_CONTAINERS (80) / START_ARTIFACTS (90) / POST_FLIGHT (100)

Rules
- Use XML or Jython to specify the steps
- Rule scope : Pre-plan / Deployed / Plan / Post-plan

Type definition
- Deployables are packaged in Deployment Packages, and they act as a template or input definition for Deployeds
- Deployable-to-Deployed relationship is one-to-many
- Relationship among deployed, deployable, and container is specified through type definition
- You can add types in ext/synthetic.xml

https://support.xebialabs.com