import ctypes

if __name__ == '__main__':
    fldir = input('Enter the name of the file or directory to be hidden: ')
    attrhdn = 0x02
    rtrn = ctypes.windll.kernel32.SetFileAttributesW(fldir, attrhdn)
    if rtrn:
        print('Hiddeness successful!!!')
    else:
        print('Hiddeness failed...')
