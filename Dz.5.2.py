chet = 0
with open('text_2.txt', 'r') as txt_2:
    for line in txt_2:
        chet += 1
        print(f'Число слов в строке {chet} равно {len(line.split())}')
    print(f'Число строк в файле: {chet}')
