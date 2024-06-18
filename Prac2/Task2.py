import json

with open('Tasks.json', 'r', encoding='utf-8') as json_file:
    data_load = json.load(json_file)


def add_task(name_task, tag_task):
    data = {"status": "[ ]", "name": name_task, "tags": tag_task}
    data_load['tasks'].append(data)

    with open('Tasks.json', 'w', encoding='utf-8') as outfile:
        json.dump(data_load, outfile, ensure_ascii=False, indent=2)

    print("Задача", name_task, "добавлена")


def delete_task(name_task):
    index_dict = 0
    for i in data_load['tasks']:
        if i['name'] == name_task:
            del data_load['tasks'][index_dict]
        index_dict += 1

    with open('Tasks.json', 'w', encoding='utf-8') as outfile:
        json.dump(data_load, outfile, ensure_ascii=False, indent=2)


def view_all_task(templates):
    for i in templates['tasks']:
        print(i['status'], i['name'], i['tags'])


def change_task(name_task):
    for i in data_load['tasks']:
        if name_task == i['name']:
            print(i['status'], i['name'], i['tags'])
            command = input('Введите название изменяемоного объекта(status, name, tag): ')
            match command:
                case 'status':
                    i['status'] = '[x]'
                    print('Статус задачи изменен')

                case 'name':
                    new_name = input('Введите новое название задачи: ')
                    i['name'] = new_name

                case 'tag':
                    new_tag = input('Введите новое название категории')
                    i['tags'] = new_tag
    with open('Tasks.json', 'w', encoding='utf-8') as outfile:
        json.dump(data_load, outfile, ensure_ascii=False, indent=2)


def view_task(name_task):
    for i in data_load['tasks']:
        if name_task == i['name']:
            print(i['status'], i['name'], i['tags'])
            break


def view_tag_task(name_tag):
    flag = False
    for i in data_load['tasks']:
        if name_tag == i['tags']:
            flag = True
            print(i['status'], i['name'], i['tags'])

    if flag == False: print('Задач с такой категорией нет')


def main():
    with open('Tasks.json', encoding='utf-8') as f:
        templates = json.load(f)
    while True:
        command = input('Enter command: ')
        match command:
            case "help":
                print('''
                        help                                - вывод всех команд
                        add_task                            - добавление задачи
                        delete_task                         - удаление задачи по названию
                        change_task                         - изменение задачи по названию
                        view_all_task                       - вывод всех имеющихся задач
                        view_task                           - вывод задачи по названию
                        view_tag_task                       - вывод всех задач в категории
                        exit                                - выйти из приложения
                ''')

            case "add_task":
                name_task = input('Введите название задачи: ')
                tag_task = input('Введите категорию задачи: ')
                add_task(name_task, tag_task)

            case "delete_task":
                name_delete_task = input("Введите название задачи: ")
                delete_task(name_delete_task)

            case "change_task":
                name_change_task = input("Введите название изменяемой задачи: ")
                change_task(name_change_task)

            case "view_all_task":
                view_all_task(templates)

            case "view_task":
                name_view_task = input("Введите название задачи: ")
                view_task(name_view_task)

            case "view_tag_task":
                name_view_tag = input("Введите название категории: ")
                view_tag_task(name_view_tag)

            case "exit":
                break

            case _:
                print("Такой команды нет")


if __name__ == '__main__':
    main()
