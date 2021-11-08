from typing import Dict
from kubernetes import config
from libs.poster import poster
from libs.configCreator import configCreator
from libs.kubeActions import kubeActions
from libs.eksDetails import eksDetails
import os, sys, json


def initiate(event: dict = {} , context: dict = {}) -> Dict:
  try:
    eksInfo = eksDetails()
    host, token = eksInfo.fetchIt()
    poster.debug("Initiating config creation.")
    configObj = configCreator(host, token)
    configObj.createConfig()
    kubeconfig = configObj.getConfig()
    poster.debug("Creation kube action obj")
    kubeObj = kubeActions(kubeconfig)
    data = kubeObj.listrs()
    poster.debug("Returning with 200OK {}".format(data))
    answer = { 
          "statusCode": 200,  
          "body": json.dumps(data)
      }

  except Exception as e:
    poster.error(e)
    answer = { 
          "statusCode": 500,  
          "body": e
      } 

  finally:
    poster.debug("Returning...")
    return answer
    #print(k)

if __name__ == "__main__":
  initiate({}, {})