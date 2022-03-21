import phonenumbers

from phonenumbers import geocoder

if __name__ == '__main__':
    phone = input('Enter telephone number: ')
    phonenbr = phonenumbers.parse(phone)
    print(geocoder.description_for_number(phonenbr, 'pt'))
