import itertools

if __name__ == '__main__':
    txt = input('Enter text: ')
    rslt = itertools.permutations(txt, len(txt))
    for i in rslt:
        print(''.join(i))
