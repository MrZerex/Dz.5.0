predmet = {}
with open('text_6.txt', 'r', encoding='utf-8') as txt_6:
    for line in txt_6:
        list_1, list_2 = line.split(': ')
        numbers = [num for num in list_2 if num == ' ' or ('0' <= num <= '9')]
        chislo = ''.join(numbers)
        summ = sum(map(int, chislo.split()))
        predmet[list_1] = summ
print(predmet)