#import pandas as pd
from langdetect import detect
import json

# df = pd.read_html('https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_P')
#
# # Удаляем лишние столбцы
# df[0].drop([('Location\xa0served', '-PA-')], axis=1, inplace=True)
# df[0].drop([('Time', '-PA-')], axis=1, inplace=True)
# df[0].drop([('DST', '-PA-')], axis=1, inplace=True)
#
# # Удаляем ссылки
# df[0].replace({'\[[0-9]+\]': ''}, regex=True, inplace=True)
#
# # Упаковываем в json
# df[0].to_json("package.json")

str = input()
lang = detect(str)

with open('package.json', encoding='utf-8') as f:
    templates = json.load(f)

def get_key(templates, value):
    for k, v in templates.items():
            if v == value:
                # print("Есть совпадение")
                return k

def main():
    if lang == "ru":
        result = get_key(templates["Airport_name_RUS"], str)
        if result is None:
            print("Такого аэропорта нет")
    else:
        result = get_key(templates["Airport_name_EN"], str)
        if result is None:
            print("Такого аэропорта нет")


    if result is not None:
        print("Код этого аэропорта по IATA: ", templates["IATA"].get(result))
        print("Код этого аэропорта по ICAO: ", templates["ICAO"].get(result))

if __name__ == '__main__':
    main()

