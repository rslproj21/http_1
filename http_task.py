import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
some_text = (response.text, 'lxml')
name = []
intelligence = []
for i in some_text:
    for data in i:
        some_data = str(data).split('\n')
        for int in some_data:
            if '"name":' in int:
                some_data = int[13:].replace('",', '')
                name.append(some_data)
            if '"intelligence":' in int:
                inte = int[22:].replace(',', '')
                intelligence.append(int(inte))

hero = ['Hulk', 'Captain America', 'Thanos']
hero_intel = []
count = 0
while count < len(hero):
    hero_intel.append(intelligence[name.index(hero[count])])
    count += 1

print(f'Среди Hulk, Captain America и Thanos самым умным является '
      f'{hero[hero_intel.index(max(hero_intel))]} с интелектом {max(hero_intel)}')

vvod = input('Введите имя персонажа чтобы узнать уровень его интелекта:')
for i in name:
    if vvod in i:
        index_char = name.index(i)
        print(f'Интелект персонажа {i} = {intelligence[index_char]}')
        break

import yadisk

y = yadisk.YaDisk(token="y0_AgAAAABk33T_AADLWwAAAADP0R4mdGLnpH3gR0a8dvtGvAxmfqPDS0Q")
vvod = input('Введите путь до файла который необходимо загрузить: ')

with open(vvod, "rb") as f:
    split_file = vvod.split('/')
    y.upload(f, split_file[-1])