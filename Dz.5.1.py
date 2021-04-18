with open('text_1.txt', "w+") as txt_1:
    while True:
        someone_text = input('Введите строку (для завершения ввода нажмите Enter): ')
        if not someone_text:
            break
        txt_1.write(f'{someone_text}\n')
    txt_1.seek(0)
    final = txt_1.read()
    print(final)