import hashlib

def hshprntr(strng1, strng2, hsh1, hsh2):
    print(f'The file \'{strng1}\' has the hash {hsh1}')
    print(f'The file \'{strng2}\' has the hash {hsh2}')


if __name__ == '__main__':
    hsh1 = hashlib.new('ripemd160')
    flnm1 = 'aula03_name1.txt'
    hsh1.update(open(flnm1, 'rb').read())
    hxhsh1 = hsh1.hexdigest()
    hsh2 = hashlib.new('ripemd160')
    flnm2 = 'aula03_name2.txt'
    hsh2.update(open(flnm2, 'rb').read())
    hxhsh2 = hsh2.hexdigest()
    if hxhsh1 == hxhsh2:
        print(f'The files \'{flnm1}\' and \'{flnm2}\' are equal.')
    else:
        print(f'The files \'{flnm1}\' and \'{flnm2}\' are different.')
    hshprntr(flnm1, flnm2, hxhsh1, hxhsh2)
