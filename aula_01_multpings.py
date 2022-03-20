import os
import time

if __name__ == '__main__':
    with open('aula_01_hosts.txt', 'r') as txtfile:
        hosts = txtfile.read().splitlines()
        for host in hosts:
            os.system('ping -n 1 {}'.format(host))
            time.sleep(5)
