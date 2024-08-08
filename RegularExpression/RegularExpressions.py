import re
# from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# регулярное выражение
pattern = re.compile(r'(\+7|7|8)?\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(?(\w*)\s*')
subst_pattern = r'+7(\2)\3-\4-\5 \6' # шаблон замены и приведения к одному виду

# логика такова, что создаем словарь с ключами- заголовками из данного файла- справочника.
# Затем мы создаем списки значкний для каждого ключа. Например, для ключа LASTNAME у нас будет значение список имен.
# И так для каждого ключа.
new_dict = dict.fromkeys(contacts_list[0]) # создаем словарь с ключами
lastname_list = []
firstname_list = []
surname_list = []
org_list = []
pos_list = []
phone_list = []
email_list = []
merged_list = []
'''
Функция "merge_person()" на вход будет принимать данные о пользователе - фамилия, имя, отчество, наименование организации, 
должность, телефон, адрес электронной почты. Функция будет производить слияние данных, в случаях, 
когда имя и фамилия идентичны а справочную информацию созранять соответсвующим непустым значением. 
Для этого будет происходить проверка по соответсвующему индексу найденного элемента списка 
'''
def merge_person(last_name, first_name,sur_name,org, position, phone, email):
    # начинаем проверку для случаев, когда имя и фамилия не пусты
    if last_name and first_name:
        # проверяем, присутсвует ли полученные им и фамилия в наших списках, если нет, то считаем,
        # что это абсолютно новый пользователь и добавляем всю информацию по нему в соответсвующие списки
        if last_name not in lastname_list and first_name not in firstname_list:
            add_person_to_list(l_name, f_name, s_name, org, position, phone, email)
        # то же самое для случаев, когда фамилия совпадает, но имя другое
        elif last_name in lastname_list and first_name not in firstname_list:
            add_person_to_list(l_name, f_name, s_name, org, position, phone, email)
        # в случае когда имя и фамилия уже есть в наших списках, то начинаем проверку справочной информации
        elif last_name in lastname_list and first_name in firstname_list:
            # для этого получаем индекс элемента списка по имеющемся имени и фамилии и сохраняем в переменную ind
            ind = lastname_list.index(last_name)
            # проверям, если значение текущего элемента в списке пустое и полученное не пустое,
            # то производим замену элемента по соответствующему индексу
            if not org_list[ind] and org:
                org_list.insert(ind, org)
            if not pos_list[ind] and position:
                pos_list.insert(ind, position)
            if not phone_list[ind] and phone:
                phone_list.insert(ind, phone)
            if not email_list[ind] and email:
                email_list.insert(ind, email)
    new_dict["lastname"] = lastname_list
    new_dict["firstname"] = firstname_list
    new_dict["surname"] = surname_list
    return new_dict
'''
Функция добавления информации о пользователе в словари и списки
'''
def add_person_to_list(l_name, f_name, s_name, org, position, phone, email):
    lastname_list.append(l_name)
    firstname_list.append(f_name)
    surname_list.append(s_name)
    org_list.append(org)
    pos_list.append(position)
    phone_list.append(phone)
    email_list.append(email)
    new_dict["organization"] = org_list
    new_dict["position"] = pos_list
    new_dict["phone"] = phone_list
    new_dict["email"] = email_list

# запускаем цикл и бежим по каждому элементу списка contacts_list
for item in contacts_list:
    # т.к. имя, фамилия, отчество хранятся по- разному в полях lastname, firstname, surname
    # то "слепим" список
    lfs_res = ' '.join(item[:3]).split(' ')
    l_name = lfs_res[0] # из полученного списка lfs_res возьмем фамилию
    f_name = lfs_res[1] # из полученного списка lfs_res возьмем имя
    s_name = lfs_res[2] # из полученного списка lfs_res возьмем отчество
    org = item[3] # из полученного элемента списка contacts_list возьмем организацию
    position = item[4] # из полученного элемента списка contacts_list возьмем должность
    # из полученного элемента списка contacts_list возьмем телефон и сразу приведем его к нужному формату
    phone = pattern.sub(subst_pattern, item[5]).strip()
    email = item[6] # из полученного элемента списка contacts_list возьмем email
    merge_person(l_name, f_name,s_name,org, position, phone, email) # вызываем функцию обработки получнных данных

# в итоге у нас получился словарь, где ключи это заголовки файла, а значения это соответствующие списки
# но для дальнешей записи в файл нам нужен список, поэтому из нашего словаря вытаскаиваем значени- списки
# при том, что в нашем словаре также присутствует список полей как одно из значений
new_contacts_list = list(new_dict.values())
new_list = [] # создаем новый список
# зиппуем
for el_lname, el_fname, el_sname, el_org, el_pos, el_phone, el_email in \
        zip(new_contacts_list[0], new_contacts_list[1], new_contacts_list[2], new_contacts_list[3], \
            new_contacts_list[4], new_contacts_list[5], new_contacts_list[6]):
    # создаем еще список, в котором уже будет храниться полная информация по каждому человеку
    person_list = []
    person_list.append(el_lname)
    person_list.append(el_fname)
    person_list.append(el_sname)
    person_list.append(el_org)
    person_list.append(el_pos)
    person_list.append(el_phone)
    person_list.append(el_email)
    # и добавляем этот список в итоговый списко, который в дальнейшем и будет использоавться для записи в файл
    new_list.append(person_list)

# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="ANSI",newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_list)