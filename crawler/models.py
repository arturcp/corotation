from django.db import models
import requests

class Spider():
    # https://github.com/kennethreitz/requests/
    def showMessage(self):
        return self.__catalog()

    def __catalog(self):
        url = "https://wilton.unifei.edu.br/ocdb/clustersGAL.txt"
        content = requests.get(url)
        return content.text
