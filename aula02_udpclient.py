import socket

if __name__ == '__main__':
    try:
        sckt = socket.socket(socket.AF_INET, socket.DGRAM)
        print('Socket creation successful!!!')
    except socket.error as e:
        print('Socket creation failed!')
        print('Error details: {}'.format(e))

    hst = 'localhost'
    prt = 5433
    mssg = 'This is a test message'
    try:
        print('Client has sent the following message: ' + mssg)
        sckt.sendto(mssg.encode(), (hst, 5432))
        dtrcv, srvr = sckt.recvfrom(4096)
        print('Client has received the following message: ' + dtrcv)
    finally:
        print('Closing socket connection...')
        sckt.close()