import os

dstpng = input('Enter hostname ou IP address: ')

os.system('ping -n 5 {}'.format(dstpng))
