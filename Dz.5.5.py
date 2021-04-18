from random import randint

with open('text_5.txt', 'w+') as txt_5:
    for el in range(100):
        txt_5.write(f'{str(randint(1, 100))} ')
    txt_5.seek(0)
    for line in txt_5:
        print(sum(map(int, (line.split()))))