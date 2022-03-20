import socket

if __name__ == '__main__':
    sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket creation successful!!!')

    hst = 'localhost'
    prt = 5432
    mssg = 'Do not be afraid.'
    try:
        print('Client has sent: ' + mssg)
        sckt.sendto(mssg.encode(), (hst, prt))
        dtrcv, srvr = sckt.recvfrom(4096)
        print('Client has received: ' + dtrcv.decode())
    finally:
        print('Closing socket connection...')
        sckt.close()