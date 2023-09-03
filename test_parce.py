import requests
from bs4 import BeautifulSoup
import re

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
    element_with_class = soup.find_all(class_=class_name)
    if element_with_class:
        # Отримуємо текстове значення елементу
        list_all_value = []
        for element in element_with_class:
            value = element.text.strip()
            list_all_value.append(value)
        else:
            print(f"Елементи з класом '{class_name}' не знайдено на сторінці.")

    table = soup.find('table', class_= 'sc-1x32wa2-1')
    print(table)
else:
    print("Не вдалося отримати сторінку")


