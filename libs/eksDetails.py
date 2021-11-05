from .poster import poster
from .awsConnection import AWSConnection
import os
from .authToken import get_token

class eksDetails:

  def __init__(self):
    self.clusterName = ""
    self.answer = []
    if "clustername" in os.environ:
      self.clusterName = os.environ.get("clustername")
    else:
      raise Exception("Couldn't find clustername in env vars")

    if "region" in os.environ:
      self.region = os.environ.get("region")
    else:
      raise Exception("Couldn't find region in env vars")          

  def fetchIt(self):
    awsObj = AWSConnection()
    awsObj.initConnection('eks', self.region)
    connection = awsObj.getConnection('eks')
    try:
      r = connection.describe_cluster(name=self.clusterName)
      self.answer.append(r.get("cluster").get("endpoint"))
      p = get_token(self.clusterName)
      self.answer.append(p.get("status").get("token"))
    except Exception as e:
      poster.error("Error -- {}".format(e))
      raise e

    return self.answer 



    