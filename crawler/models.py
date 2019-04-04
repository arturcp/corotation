from django.db import models
import requests

class Spider():
    # https://github.com/kennethreitz/requests/
    # https://wilton.unifei.edu.br/ocdb/readme.txt
    URL = "https://wilton.unifei.edu.br/ocdb/clustersGAL.txt"
    def clusters(self):
        catalog = self.__catalog()
        lines = catalog.split("\n")

        return map(Cluster.from_line, lines)

    def __catalog(self):
        return requests.get(Spider.URL).text

class Cluster():
    @classmethod
    def from_line(cls, line):
        cluster = Cluster()
        cluster.line = line

        cluster.name = line[0:17].strip()
        cluster.galaticLongitudeII = line[18:25].strip()
        cluster.radial_velocity = line[134:139].strip()
        return cluster
