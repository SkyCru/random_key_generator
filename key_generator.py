import random

def  generate_random_key ():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F, G', 'H, I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f, g', 'h','i', 'j', 'k', 'l', 'm', 'n','o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']
    simbols = ['!', '@', '#', '$', ',', '%', '?','*']
    numbers = ['0', '1', '2', '3', '4', '5','6','7', '8', '9']
    
    caracters = mayus + minus + numbers + simbols
    
    key = []
    for i in range(15):
        caracter_random = random.choice(caracters)
        key.append(caracter_random)
    
    key = ''.join(key)
    return key
        

def run():
    key = generate_random_key()
    print('Please wait...Your key has been generated...')
    print('Your key generated is: ' + key)

if __name__ == '__main__':
    run()