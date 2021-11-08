from kubernetes import client
from .poster import poster
import os

""" Kube config object creator """
class configCreator:

  def __init__(self, host, token):
    self.config = ""
    self.token = token
    self.apihost = host

  def createConfig(self):
    poster.debug("Creating kubernetes config for auth")
    try:
      k = client.Configuration()
      k.host = self.apihost
      k.verify_ssl = False
      k.api_key = {"authorization": "Bearer " + self.token}
      self.config = k
      poster.debug("created the config for kubernetes.")
    except Exception as e:
      raise e  


  def getConfig(self):
    poster.debug("Returning the kubernetes config")
    return self.config