import json
from functools import reduce
from functools import partial
#====== Блок 1 ======

def block1():
    with open('countries.json', 'r', encoding='utf-8') as file:
        data_load = json.load(file)

    # list_upper = map(lambda x: x.upper(), data_load)
    #
    # print(list(list_upper))

    #list_two = list(filter(lambda x: x.find('land') != -1, data_load))
    # print(list_two)

    #list_tree = list(filter(lambda x: len(x) == 6, data_load))
    #print(list_tree)

    #list_four = list(filter(lambda x: x[0] != 'E', data_load))
    #print(list_four)

    #NorthCountry = ['Финляндия', 'Швеция', 'Дания', 'Норвегия', 'Исландия']
    #print(reduce(lambda x, y: x + ", " + y, NorthCountry) + " являются странами Северной Европы.")

    #print(list(filter(lambda x: "land" in x, list(map(lambda x: x.lower(), data_load)))))

    # def categorize_countries(sample):
    #     def print_countries(countries):
    #         return list(filter(lambda x: sample in x, countries))
    #
    #     return print_countries
    #
    #
    # print(categorize_countries("ia")(data_load))

    # with open("countries-data.json", "r", encoding="utf-8") as file:
    #     countries_data = json.load(file)
    #
    # sortedName = sorted(countries_data, key=lambda x: x['name'])
    # sortedCapital = sorted(countries_data, key=lambda x: x['capital'])
    # sortedPopulation = sorted(countries_data, key=lambda x: x['population'])
    #
    # all_languages = [language for country in countries_data for language in country['languages']]
    # language_count = [(language, all_languages.count(language)) for language in set(all_languages)]
    # topLanguages = sorted(language_count, key=lambda x: x[1], reverse=True)[:10]
    #
    # sorted_population_desc = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    # top_populated_countries = sorted_population_desc[:10]


def block2():
    numbers = list(range(1, 51))
    power = [(x ** 4, x ** 5, x ** 6) for x in numbers]
    #print(power)

    matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 2], [3, 4], [5, 6], [7, 8]]
    transposed_matrix = [[x[i] for x in matrix] for i in range(len(matrix[0]))]
    #print(transposed_matrix)

    numbers = list(range(-9999, 9999))
    #print(list(filter(lambda x: x % 36 == 0, numbers)))

    def edit_title(title):
        words = title.split()
        filter__ = map(lambda word: word.capitalize() if len(word) > 3 else word.lower(), words)
        result = ' '.join(filter__)
        return result

    original_title = "каждое слово длиной БОЛЕЕ 3 букв должно БЫТЬ с БОЛЬШОЙ буквы"
    edited_title = edit_title(original_title)

    # print(edited_title)

    def foo(a: int, b: int, c: int, d: int) -> int:
        return a * 4 + b * 3 + c * 2 + d

    par3 = partial(foo, 2, 4, 20)

    #print(par3(0))
    #print(par3(60))
    #print(par3(120))

    fib = [0, 1]

    def fibonacci(n):
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[:n]

    def fibonacci_squared(n):
        fib = fibonacci(n)
        return (x**2 for x in fib)

    print(sum(fibonacci_squared(10)), sum(fibonacci_squared(20)), sum(fibonacci_squared(30)),
          sum(fibonacci_squared(40)),sum(fibonacci_squared(50)))

    def airports_generator(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                data = eval(line)
                yield data

    file_path = "/Users/volod/PycharmProjects/Lab3_Yar/.venv/airport.txt"

    for airport in airports_generator(file_path):
        print(airport)

        


if __name__ == '__main__':
    block1()
    block2()
