with open('text_3.txt', 'r', encoding='utf-8') as txt_3:
    oklad = []
    chet = 0
    for line in txt_3:
        mline = line.split()
        if int(mline[1]) < 20000:
            print(f'Сотрудник {mline[0]} имеет оклад меньше 20 тыс.')
        oklad.append(int(mline[1]))
        chet += 1
    print(f'Средняя величина дохода сотрудников: {sum(oklad) / chet }')