import json

with open('budget.json', 'r', encoding='utf-8') as json_file:
    data_load = json.load(json_file)


def test():
    #tag_opr1 = input("Введите категорию 1: ")
    tag_opr2 = input("Введите категорию 2: ")
    #print(data_load["current"][0].setdefault("tag", tag_opr1))
    #print(data_load["current"][1].setdefault("tag", tag_opr2))
    for i in data_load["current"]:
        if i['tag'] == tag_opr2:
            print("True")
            break
        else:
            print("False")


def add_opr(name_opr, amount_opr, tag_opr, type_opr):
    data = {"name": name_opr, "amount": amount_opr, "tag": tag_opr, "type": type_opr}

    k = 0

    flag = False
    for i in data_load["current"]:
        if i['tag'] == tag_opr:
            print("True")
            flag = True
            if type_opr == "расход":
                k = int(i['current']) + int(amount_opr)

            elif type_opr == "доход":
                k = int(i['current']) - int(amount_opr)
            i['current'] = str(k)
            break
        else:
            flag = False

    if not flag:
        data_current = {"tag": tag_opr, "current": amount_opr}
        data_load['current'].append(data_current)

    flag_on_lim = False
    for i in data_load["limits"]:
        if tag_opr == i["tag"]:
            print("Найден предел на категорию")
            if k > int(i["limit"]):
                print("Превышен предел на категорию")
                flag_on_lim = True
            else:
                print("Предел на категорию не превышен")
                flag_on_lim = False
            break
        else:
            flag_on_lim = False
            print("Предел на категорию не найден")

    if flag_on_lim:
        print("Операция", name_opr, "не добавлена")
    else:
        data_load['operations'].append(data)
        with open('budget.json', 'w', encoding='utf-8') as outfile:
            json.dump(data_load, outfile, ensure_ascii=False, indent=2)
        print("Операция", name_opr, "добавлена")


def view_all_opr():
    for i in data_load['operations']:
        print(i['name'], i['amount'], i['tag'], i['type'])

def view_opr(name_opr):
    for i in data_load['operations']:
        if name_opr == i['name']:
            print(i['name'], i['amount'], i['tag'], i['type'])


def view_tag_opr(name_tag):
    flag = False
    for i in data_load['operations']:
        if name_tag == i['tag']:
            flag = True
            print(i['name'], i['amount'], i['tag'], i['type'])

    if flag == False: print('Операций с такой категорией нет')


def add_lim(tag_lim, amount_lim):
    data_limit = {"tag": tag_lim, "limit": amount_lim}
    data_load['limits'].append(data_limit)
    with open('budget.json', 'w', encoding='utf-8') as outfile:
        json.dump(data_load, outfile, ensure_ascii=False, indent=2)


def view_all_lim():
    for i in data_load['limits']:
        print(i['tag'], i['limit'])


def view_lim(name_lim):
    for i in data_load['limits']:
        if i['tag'] == name_lim:
            print(i['tag'], i['limit'])


def delete_lim(tag_lim):
    index_dict = 0
    for i in data_load['limits']:
        if i['tag'] == tag_lim:
            del data_load['limits'][index_dict]
        index_dict += 1
    with open('budget.json', 'w', encoding='utf-8') as outfile:
        json.dump(data_load, outfile, ensure_ascii=False, indent=2)


def change_lim(name_tag, new_lim):
    for i in data_load['limits']:
        if name_tag == i['tag']:
            i['limit'] = str(new_lim)
            print(i['tag'], i['limit'])

    with open('budget.json', 'w', encoding='utf-8') as outfile:
        json.dump(data_load, outfile, ensure_ascii=False, indent=2)


def view_all_cur():
    for i in data_load['current']:
        print(i['tag'], i['current'])


def view_cur(name_tag):
    for i in data_load['current']:
        if i['tag'] == name_tag:
            print(i['tag'], i['current'])


def main():
    while True:
        command = input('Enter command: ')
        match command:
            case "help":
                print('''
                        help                                - вывод всех команд
                        +limit                               - вкладка с лимитами
                        current                             - вкладка с тратами
                        +add_opr                             - добавление операции
                        view_all_opr                        - вывод всех имеющихся операций
                        view_opr                            - вывод операции по названию
                        view_amount                         - вывод всех операций с заданной суммой
                        view_tag_opr                        - вывод всех операций в категории
                        exit                                - выйти из приложения
                ''')

            case "add_opr":
                name_opr = input('Введите название операции: ')
                amount_opr = input('Введите сумму: ')
                tag_opt = input('Введите категорию операции: ')
                type_opr = input('Введите тип операции(доход/расход): ')
                add_opr(name_opr, amount_opr, tag_opt, type_opr)

            case "limit":
                command_limit = input('Enter command limit: ')

                match command_limit:
                    case "help":
                        print('''
                        help                - Вывод всех команд во вкладке limit
                        add_limit           - Добавить новый предел на категорию
                                            (Если такой категории нет, то предел все равно создастся)
                        delete_limit        - Удалить лимит по названию
                        change_limit        - Изменить лимит по названию
                        view_all_limits     - Вывести все пределы
                        view_limits         - Вывести предел по названию
                        
                        ''')
                    case "add_limit":
                        name_tag = input('Введите название категории: ')
                        amount_limit = input('Введите лимит на категорию: ')
                        add_lim(name_tag, amount_limit)
                    case "delete_limit":
                        tag_lim = input("Введите название категорию лимита: ")
                        delete_lim(tag_lim)
                    case "view_all_lim":
                        view_all_lim()
                    case "view_lim":
                        name_tag = input("Введите категорию лимита: ")
                        view_lim(name_tag)
                    case "change_lim":
                        name_tag = input("Введите категорию лимита: ")
                        new_lim = int(input("Введите новый лимит: "))
                        change_lim(name_tag, new_lim)

            case "current":
                command_current = input('Enter command current: ')

                match command_current:
                    case 'help':
                        print('''
                        help            - Вывод всех комманд во вкладке current
                        view_all_cur    - Вывод всех трат по категориям
                        view_cur        - Вывод трат по категории
                        ''')
                    case 'view_all_cur':
                        view_all_cur()
                    case 'view_cur':
                        name_tag = input('Введите название категории: ')
                        view_cur(name_tag)

            case "test":
                test()

            #case "current":

            case "view_all_opr":
                view_all_opr()

            case "view_opr":
                name_opr = input('Введите название операции: ')
                view_opr(name_opr)

            case "view_tag_opr":
                name_tag = input('Введите название категории: ')
                view_tag_opr(name_tag)

            case "exit":
                break

            case _:
                print("Такой команды нет")


if __name__ == '__main__':
    main()
