from logging import setLoggerClass
from kubernetes import client
from .poster import poster
import warnings
from tabulate import tabulate

class kubeActions:

  def __init__(self, kubeConfig):
    try:
      self.messagebody = ""
      poster.debug("Creating API client with kubeconfig")
      self.apiClient = client.ApiClient(kubeConfig)
      warnings.filterwarnings("ignore")
    except Exception as e:
      poster.error(e)
      raise e 

  def listrs(self):
    """ List Replica Sets"""
    v1 = client.AppsV1Api(self.apiClient)    
    data = v1.list_replica_set_for_all_namespaces(watch=False, label_selector="app.kubernetes.io/managed-by")
    dataHolder = []
    for d in data.items:
      name = d.metadata.name
      image = d.spec.template.spec.containers[0].image
      replicas = d.spec.replicas
      info = [name, image, replicas]
      dataHolder.append(info)
    self.messagebody =  tabulate(dataHolder, headers=["RS-Name", "Image", "Replicas"])
    return self.messagebody
      