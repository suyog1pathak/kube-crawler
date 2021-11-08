# Kube-crawler <img src="https://user-images.githubusercontent.com/19824574/41482054-47a3a702-70a2-11e8-9561-de51c5f71220.png" width="30px">

**What does it do ?**

* Piece of python code which can be deployed as AWS Lambda to bring details from EKS API for information gathering or monitoring objects. This further can be integrated with slack or telegram for notifications.

**Problem statement**

* I wanted to have automation in place in order to fetch details from the EKS cluster without directly interacting with the API. Further this should also be able to send notifications on multiple channels like slack, telegram, etc. I am using argocd rollouts for my deployment so I am gathering the information of replica sets in this code as of now. (Will be adding further in the future.)

**How it should be deployed**

* Currently this code is designed to return the output as an HTTP object assuming the below deployment strategy. Here the crawler is deployed as dockerized lambda with the integration with AWS API gateway in order to make it callable over http/https. This API gateway now can be configured in slack as a command.


```
              +----------------+            +-------------------+  
--Request---> |   API Gateway  |  <------>  | Dockerized Lambda |
              +----------------+            +-------------------+  

```

***Features***
* It has hot spare support i.e. you can add your custom methods in `kubeActions.py` in `kubeActions` class for a variety of complex operations.
* It is a containerized application so can be deployed on Kubernetes, AWS lambda, standalone docker-engine, etc, or can be used as python script too.
* easy to use.

*** Env vars ***

var          | required |details
------------- |---- |-------------
clustername|yes| eks clustername
region|yes| AWS region of eks cluster
LOGLEVEL| no | log level default is INFO


***sample output***

```
{'statusCode': 200, 'body': '"RS-Name                            Image                                                                          Replicas\\n---------------------------------  ---------------------------------------------------------------------------  ----------\\npp-agent-7f58fd6cdc   gcr.io/npp/agent:1.10.0         2\\nebs-csi-controller-f9f4447d7       k8s.gcr.io/provider-aws/aws-ebs-csi-driver:v1.1.0                                     2.....................}
```