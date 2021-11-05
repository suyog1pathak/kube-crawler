import boto3
from .poster import poster

class AWSConnection:
  connection = {}
  def initConnection(self, resource, region):
    if resource not in self.connection:
      try:
        poster.debug("Creating aws connection")
        self.connection[resource] = boto3.client(resource, region_name=region)
      except Exception as e:
        poster.error("Error while creating aws connection {}".format(e))

  def getConnection(self, resource):
    return self.connection[resource]

  def getResource(self, resource):
      return self.resources[resource]