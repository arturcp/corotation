#!/usr/bin/python
import requests
from clusters import Cluster

def write(text, size, suffix = '|'):
    print(f'{text.ljust(size)}{suffix} ', end = '')

def print_results(lines):
    print('')
    print('                                                                       CATALOG')
    print(' =====================================================================================================================================================================')
    print(' | NAME              | DISTANCE | AGE (LOG T) | PROPER MOTION L | PROPER MOTION B | RADIAL VELOCITY | LATITUDE | LONGITUDE |                                          |')
    print(' =====================================================================================================================================================================')

    for line in lines:
        cluster = Cluster.from_line(line)
        if cluster.valid():
            write(' ', 1)
            write(cluster.name, 18)
            write(cluster.distance, 9)
            write(cluster.age_in_log_t, 12)
            write(cluster.mean_proper_motion_in_mu_l_icrs, 16)
            write(cluster.mean_proper_motion_in_mu_b_icrs, 16)
            write(cluster.radial_velocity, 16)
            write(cluster.latitude_with_sign(), 9)
            write(cluster.galactic_longitude, 9)
            write('', 42)
            print('')
    print(' =====================================================================================================================================================================')
    print('')

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
