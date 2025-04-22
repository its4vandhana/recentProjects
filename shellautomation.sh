#!/bin/bash
echo "creating an ec2 instance"
aws ec2 run-instances --image-id ami-05b10e08d247fb927 --count 1 --instance-type t2.micro --key-name new-demo-key-pair --security-group-ids sg-0866686d96c933d72
echo "sucessfully created instance"


echo "install java,maven and git in ec2 instance"
sudo yum install java -y
sudo yum install maven -y
sudo yum install git -y

mkdir sampleproject
cd sampleproject
git clone https://github.com/its4vandhana/samplejavaproject.git
cd samplejavaproject
mvn clean
mvn package
jarfile="MyApp-0.0.1.jar"
source="./target"
destination="/home/ec2-user/sampleproject"
if [ -f "$jarfile" ]; then 
    echo "jar file already exists"
    exit 1
fi

cp "$source/$jarfile" "$destination"
cd ..
pwd
ls

java -jar $jarfile


