import os

if __name__ == '__main__':
    dstpng = input('Enter hostname ou IP address: ')

    os.system('ping -n 5 {}'.format(dstpng))
