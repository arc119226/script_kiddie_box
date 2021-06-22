# kali linux ssh server install

## 1.
apt-get install openssh-server

## 2.
update-rc.d -f ssh remove
update-rc.d -f ssh defaults

## 3.
cd /etc/ssh/
mkdir backup
mv ssh_host_* backup/

## 4.
dpkg-reconfigure openssh-server

## 5.
service ssh restart

## 6.
vim /etc/ssh/sshd_config
PermitRootLogin prohibit-password
AuthorizedKeysFile      .ssh/authorized_keys .ssh/authorized_keys2
:wq

## 8.
cd ~
mkdir .ssh
echo 'ssh-rsa <your_key>' > .ssh/authorized_keys

## 9.
service ssh restart
