from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n}', end=' ')
print(f'\nMaior número: {max(num)}\nMenor número: {min(num)}')