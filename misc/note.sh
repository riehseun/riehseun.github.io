########## ---------- From Docker Enabled local Unix machine ---------- ##########

# https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes
docker build -f Dockerfile -t riehseun/jenkins-master .
docker images
docker login
docker push riehseun/jenkins-master
# Stop and remove all images
docker stop $(docker ps -a -q)
docker rmi -f $(docker images -a -q)

docker tag dd-fe riehseun/dd-fe
docker run -d -p 8080:8080 riehseun/dd-fe

# Useful commands
kubectl get pods/<podname> -o yaml
kubectl get services/<servicename> -o yaml
kubectl get deploy/<deployname> -o yaml
kubectl logs <jenkins-pod> -c jnlp
kubectl get pods | cut -d ' ' -f1 | sed -n '2p'
kubectl exec -it $(kubectl get pods | cut -d ' ' -f1 | sed -n '2p') -- /bin/bash -c """
    apt-get update
    cd /tmp
    curl -O https://repo.jenkins-ci.org/public/org/jenkins-ci/plugins/job-dsl-core/1.72/job-dsl-core-1.72-standalone.jar
    git clone https://github.com/riehseun/dsl-scripts.git
    java -jar job-dsl-core-1.72-standalone.jar dsl-scripts/jenkins2/createSeedJob.groovy
"""

# Givng "default" service account access to connect to k8s master
kubectl create clusterrolebinding permissive-binding --clusterrole=cluster-admin --user=admin --user=kubelet --group=system:serviceaccounts:default

# Cloud Kubernetes
Kubernetes URL : https://10.26.2.2:6443 (kubectl cluster-info)
Jenkins tunnel : 104.196.0.154:50000 (kubectl get svc)
# Kubernetes Pod Template
Name: pod-default
Label: default
Use the node as much as possible
# Container Template
Name: jnlp
Docker Image: jenkinsci/jnlp-slave
Command to run: ""
Arguments to pass to the command: ""

# Get inside container
kubectl exec -it <jenkins-pod> -- /bin/bash

# Get all
kubectl get all --all-namespaces

# CoreDNS issue
kubectl -n kube-system get deployment coredns -o yaml | sed 's/allowPrivilegeEscalation: false/allowPrivilegeEscalation: true/g' | kubectl apply -f -

# Update deploymet (kill the pod after that)
kubectl apply -f []

## SAMPLE JOB
def label = "worker-${UUID.randomUUID().toString()}"
podTemplate(label: label, containers: [
  containerTemplate(name: 'jenkins-slave', image: 'jenkinsci/jnlp-slave', command: 'cat', ttyEnabled: true),
],
volumes: [
  hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
]) {
  node(label) {
    stage('Test') {
      try {
        container('jenkins-slave') {
          sh """
            echo hi
            """
        }
      }
      catch (exc) {
        println "Failed to test - ${currentBuild.fullDisplayName}"
        throw(exc)
      }
    }
  }
}

# Job DSL
#apt-get update
#curl -O https://repo.jenkins-ci.org/public/org/jenkins-ci/plugins/job-dsl-core/1.72/job-dsl-core-1.72-standalone.jar
#git clone https://github.com/riehseun/dsl-scripts.git
#java -jar job-dsl-core-1.72-standalone.jar dsl-scripts/jenkins2/createJobs.groovy
curl -s -XPOST 'http://35.231.157.239:30000/createItem?name=seed-job' --data-binary @seed-job.xml -H "Content-Type:text/xml"
curl -s -XPOST 'http://35.231.157.239:30000/config.xml' --data-binary @config.xml -H "Content-Type:text/xml"

# Jenkinsfile-PIPELINE example
@Library(value='pipeline@master', changelog=false)_
mainMethod()

## TensorFlow
docker pull tensorflow/tensorflow
docker run -it --rm -v $PWD:/tmp -w /tmp tensorflow/tensorflow python3 ./house_price_prediction.py
python3 regression.py
pip3 install keras
pip3 install tflearn

# Jenkins X
mkdir -p ~/.jx/bin
curl -L https://github.com/jenkins-x/jx/releases/download/v2.0.2/jx-linux-amd64.tar.gz | tar xzv -C ~/.jx/bin
export PATH=$PATH:~/.jx/bin
echo 'export PATH=$PATH:~/.jx/bin' >> ~/.bashrc



## BACKEND
# FROM alpine:3.7 AS base

# RUN apk add --no-cache git && git clone https://github.com/slalomdojo/react-todo-backend

# RUN ls

# FROM alpine:3.7

# RUN apk add --no-cache nodejs

# WORKDIR /tmp

# COPY --from=base /react-todo-backend .

# RUN ls

# WORKDIR /tmp/react-todo-backend

# RUN npm install

# CMD [ "npm", "run", "server-dev" ]


## DB
# FROM alpine:3.7

# RUN apk add --no-cache mongodb

# ENTRYPOINT [ "mongod" ]


## COMMAND

# docker run --net db -p 27017:27017 -v /home/ec2-user/data:/data/db dd-db # mount dir
# docker run --net backend -p 7777:7777 -e 'MONGODB_HOST=3.209.139.78' dd-be # connect to DB
# docker build --no-cache -t dd-be .








kubectl create clusterrolebinding cluster-admin-binding --clusterrole cluster-admin --user $(gcloud config get-value account)
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/mandatory.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/cloud-generic.yaml
kubectl get pods --all-namespaces -l app.kubernetes.io/name=ingress-nginx --watch