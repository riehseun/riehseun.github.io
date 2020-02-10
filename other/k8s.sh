# https://www.linuxtechi.com/install-kubernetes-1-7-centos7-rhel7/

########## ---------- MASTER ---------- ##########

sudo -i

hostnamectl set-hostname 'k8s-master'
exec bash
setenforce 0
sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux

firewall-cmd --permanent --add-port=6443/tcp
firewall-cmd --permanent --add-port=2379-2380/tcp
firewall-cmd --permanent --add-port=10250/tcp
firewall-cmd --permanent --add-port=10251/tcp
firewall-cmd --permanent --add-port=10252/tcp
firewall-cmd --permanent --add-port=10255/tcp
firewall-cmd --reload
modprobe br_netfilter
echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables

cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
exclude=kube*
EOF

yum install kubeadm docker -y
systemctl restart docker && systemctl enable docker
yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
systemctl restart kubelet && systemctl enable kubelet
kubeadm init

mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config

export kubever=$(kubectl version | base64 | tr -d '\n')
kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$kubever"

kubectl get nodes
kubectl get pods --all-namespaces

# vi /etc/hosts
35.231.174.32 k8s-master
35.196.44.158 worker-node1


########## ---------- NODES ---------- ##########

sudo -i

hostnamectl set-hostname 'k8s-node3'
setenforce 0
sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux
firewall-cmd --permanent --add-port=10250/tcp
firewall-cmd --permanent --add-port=10255/tcp
firewall-cmd --permanent --add-port=30000-32767/tcp
firewall-cmd --permanent --add-port=6783/tcp
firewall-cmd  --reload
echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables

cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
exclude=kube*
EOF

yum  install kubeadm docker -y
systemctl restart docker && systemctl enable docker
yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
systemctl restart kubelet && systemctl enable kubelet
systemctl enable docker.service && systemctl start docker.service

# From master, kubeadm token list
kubeadm join --token crg2wf.r9dkdszgvz2wzzqt --discovery-token-unsafe-skip-ca-verification 104.196.99.17:6443
# kubeadm join 10.26.2.2:6443 --token byxx0c.kuvpx2lhue3bxscw --discovery-token-ca-cert-hash sha256:3910fc8369279945a419e9c46c16fdcee24a00f233ab41d56baddf41e3243d36