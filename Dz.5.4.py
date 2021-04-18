translater = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_4.txt', 'r', encoding='utf-8') as txt_4:
    for line in txt_4:
        pr = line.split(' — ')
        pr.insert(0, translater.get(pr[0]))
        pr.remove(pr[1])
        new_list = ' - '.join(pr)
        with open('text_4.1.txt', 'a', encoding='utf-8') as txt_4_1:
            txt_4_1.write(new_list)