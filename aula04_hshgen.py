import hashlib

if __name__ == '__main__':
    txt = input('Enter text: ')
    itmchc = int(input('''### For the hash algorithms below ###
    1) MD5
    2) SHA1
    3) SHA256
    4) SHA512
    Pick your choice: '''))
    if itmchc == 1:
        rslt = hashlib.md5(txt.encode('utf-8'))
        print(f'The MD5 hash of the text {txt} is {rslt.hexdigest()}.')
    elif itmchc == 2:
        rslt = hashlib.sha1(txt.encode('utf-8'))
        print(f'The SHA1 hash of the text {txt} is {rslt.hexdigest()}.')
    elif itmchc == 3:
        rslt = hashlib.sha256(txt.encode('utf-8'))
        print(f'The SHA256 hash of the text {txt} is {rslt.hexdigest()}.')
    elif itmchc == 4:
        rslt = hashlib.sha512(txt.encode('utf-8'))
        print(f'The SHA512 hash of the text {txt} is {rslt.hexdigest()}.')
    else:
        print('Somthing is wrong!')
