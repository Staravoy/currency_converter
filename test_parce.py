import requests
from bs4 import BeautifulSoup
import re

def average(pattern, list_all):
    usd_values = [re.search(pattern, item).group(1) for item in list_all if re.search(pattern, item)]

    list_float = []
    for i in usd_values:
        list_float.append(float(i.replace(',', '.')))
    total = sum(list_float)
    midl_num = total / len(list_float)
    return midl_num
def middle_num(usd_values):
    total = []
    for i in usd_values:
        i = round(float(i.replace(',', '.')),2)
        total.append(i)
    sum_all_num = sum(total)
    middle = sum_all_num/len(total)
    return round(middle, 2)

# URL сторінки
url = "https://minfin.com.ua/ua/currency/"

# Відправити GET-запит
response = requests.get(url)

# Перевірка, чи вдалося отримати сторінку
if response.status_code == 200:
    # Розбираємо HTML-код сторінки за допомогою BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Знаходимо елемент з певним класом (замість "class_name" вставте потрібний клас)
    class_name = "dKDsVV"  # Замініть на потрібний клас
    # class_name ="bKmKjX"  # Замініть на потрібний клас
    #

    element_with_class = soup.find_all(class_=class_name)
    if element_with_class:
        # Отримуємо текстове значення елементу
        list_all_value = []
        for element in element_with_class:
            value = element.text.strip()
            list_all_value.append(value)
        else:
            pass
            # print(f"Елементи з класом '{class_name}' не знайдено на сторінці.")
    currency = input('Enter currency (USD or EUR):')
    if currency == 'USD':
        pattern = re.compile(r"USD(\d+,\d+)")
    elif currency == 'EUR':
        pattern = re.compile(r"EUR(\d+,\d+)")
    else:
        print('This currency not find.')

    numbers_money = input('Enter numbers:')
    average_num = average(pattern, list_all_value)
    result = int(numbers_money) * average_num
    print(f'Result of converter: {round(result, 2)}')
    type_current = input('Enter USD or EUR:')
    if type_current == 'USD':
        pattern = re.compile(r"USD(\d+,\d+)")
        usd_values = [re.search(pattern, item).group(1) for item in list_all_value if re.search(pattern, item)]
        middle = middle_num(usd_values)
    elif type_current == 'EUR':
        pattern = re.compile(r"EUR(\d+,\d+)")
        eur_values = [re.search(pattern, item).group(1) for item in list_all_value if re.search(pattern, item)]
        middle = middle_num(eur_values)
    amount_currency = input('Enter amount currency:')
    result = int(amount_currency) * middle
    print(f'Result = {round(result, 2)}')
else:
    print("Не вдалося отримати сторінку")


