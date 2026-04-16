import random

def play():
    v = ['tas', 'qayshi', 'qagaz']
    m = input("\ntas, qayshi yaki qagaz jazin: ").lower()
    c = random.choice(v)
    print(f'\nKompyuter tanladi: {c}')

    if m == c:
        print('\nTen!')
        
    elif (m == 'tas' and c == 'qayshi') or \
    (m == 'qayshi' and c == 'qagaz') or \
    (m == 'qagaz' and c == 'tas'):
        print("\nSiz uttiniz!")
        
    else:
        print("\nSiz utildiniz!")
        
        
play()