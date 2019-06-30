#!/usr/bin/python
import requests
from clusters import Cluster

def write(text, size, suffix = '|'):
    print(f'{text.ljust(size)}{suffix}')

def print_results(lines):
    print('============================================================================== Catalog ==============================================================================')
    print('NAME              |')
    print('=====================================================================================================================================================================')

    cluster = Cluster.from_line(lines[0])
    write(cluster.name, 18)

# https://github.com/kennethreitz/requests/
# https://wilton.unifei.edu.br/ocdb/readme.txt
def from_web():
    URL = 'https://wilton.unifei.edu.br/ocdb/clustersGAL.txt'
    catalog = requests.get(URL).text
    lines = catalog.split('\n')
    print_results(lines)

def from_file():
    lines = [line.rstrip('\n') for line in open('./catalogs/clustersGAL.txt')]
    print_results(lines)

# from_web()
from_file()
