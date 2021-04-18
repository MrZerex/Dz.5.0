import json
prib_dict = {}
sredprib_dict = {}
sred_prib = []
proffit = []
with open('text_7.txt', 'r', encoding='utf-8') as txt_7:
    for line in txt_7:
        list_1 = (''.join([el for el in line])).split()
        pribyl = int(list_1[2]) - int(list_1[3])
        if pribyl > 0:
            sred_prib.append(pribyl)
        prib_dict[list_1[0]] = pribyl
        print(f'Прибыль фирмы {list_1[0]} равна {pribyl}')
    sr_prib = sum(sred_prib) / len(sred_prib)
    sredprib_dict['average_profit'] = sr_prib
    print(f'Средняя прибыль равна: {sr_prib}')
    proffit.append(prib_dict)
    proffit.append(sredprib_dict)
with open('profit.json', 'w', encoding='utf-8') as txt_js:
    json.dump(proffit, txt_js, ensure_ascii=False, indent=4)
