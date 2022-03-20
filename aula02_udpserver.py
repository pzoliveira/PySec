import socket

if __name__ == '__main__':
    sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket creation successful!!!')

    hst = 'localhost'
    prt = 5432
    sckt.bind((hst, prt))
    mssg = ' We have all the rights!'
    while True:
        dtrcv, addrss = sckt.recvfrom(4096)
        if dtrcv:
            print('Server received: {}'.format(dtrcv.decode()))
            print('Server has appended: {}'.format(mssg))
            sckt.sendto(dtrcv + (mssg.encode()), addrss)
