import socket
import sys

def prncpl():
    try:
        sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('Socket connection failed!')
        print('Error details: {}'.format(e))
        sys.exit()
    print('Socket creation successful!!!')

    dsthst = input("Enter IP address or hostname: ")
    dstprt = int(input('Enter port number: '))
    try:
        sckt.connect((dsthst, dstprt))
        print('TCP client connection successful!!!')
        sckt.shutdown(2)
    except socket.error as e:
        print('TCP client connection not possible!')
        print('Error details: {}'.format(e))
        sys.exit()


if __name__ == '__main__':
    prncpl()