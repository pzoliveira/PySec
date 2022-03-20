import random, string

if __name__ == '__main__':
    lgth = int(input('Enter the length of the password: '))
    setofchars = string.ascii_letters + string.digits + 'ç!@#$%¨&*()-_=+'
    #print(setofchars)
    rndmnbr = random.SystemRandom()
    psswd = ''.join(rndmnbr.choice(setofchars) for i in range(lgth))
    print(psswd)
