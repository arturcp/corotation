from django.db import models
import requests

class Spider():
    # https://github.com/kennethreitz/requests/
    def clusters(self):
        catalog = self.__catalog()
        line = catalog.split("\n")[0]
        cluster = Cluster(name=line[0:18], galaticLongitudeII=line[19:26])
        return cluster

    def __catalog(self):
        url = "https://wilton.unifei.edu.br/ocdb/clustersGAL.txt"
        content = requests.get(url)
        return content.text

class Cluster():
    def __init__(self, name, galaticLongitudeII):
      self.name = name
      self.galaticLongitudeII = galaticLongitudeII
