from random import randint

random_number = randint(1, 20)

user_guest = None

while True: 
    user_guest = int(input('taxmin: '))
    if user_guest < random_number:
        print('kattaroq son ')
    elif user_guest > random_number:
        print('kichikroq son')
    else:
        print('topdingiz')
        break