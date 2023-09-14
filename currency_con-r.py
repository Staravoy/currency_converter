from tkinter import *
from tkinter import ttk
import re
from bs4 import BeautifulSoup
import requests


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
            pass
else:
    print("Не вдалося отримати сторінку")

# заміна коми на крапку та отримання середнього значення
def middle_num(usd_values):
    total = []
    for i in usd_values:
        i = round(float(i.replace(',', '.')),2)
        total.append(i)
    sum_all_num = sum(total)
    middle = sum_all_num/len(total)
    return round(middle, 2)


def on_dropdown_select(): # Функція, яка викликається при виборі елемента у випадаючому списку
    # отримуємо результат вибору з списку валют
    selected_item = dropdown_var.get()
    # Здійснюємо перевірку, обрізання та отримання єдиного середнього значення
    if selected_item == "USD":
        pattern = re.compile(r"USD(\d+,\d+)")
        usd_values = [re.search(pattern, item).group(1) for item in list_all_value if re.search(pattern, item)]
        middle = middle_num(usd_values)
        image_label.config(image=flag_usd)
        return middle
    elif selected_item == "EUR":
        pattern = re.compile(r"EUR(\d+,\d+)")
        eur_values = [re.search(pattern, item).group(1) for item in list_all_value if re.search(pattern, item)]
        middle = middle_num(eur_values)
        image_label.config(image=flag_eur)
        return middle


def calculate_result():
    # Отримайте значення введених цифр і виконайте обчислення
    input_value = input_entry.get()
    try:
        input_value = float(input_value)
        # Ваші обчислення тут
        middle = on_dropdown_select()
        result = round(int(input_value) * middle, 2)  # Приклад обчислення
        result_var.set(result)
    except ValueError:
        result_var.set("Помилка: Введіть число")
# Створення головного вікна
root = Tk()
root.title("Конвертер валют")
root.geometry("380x140+400+200")

# Створення випадаючого списку
currents =["USD", "EUR"]
dropdown_var = StringVar(value=currents[0])
dropdown_label = ttk.Label(root, text="Оберіть валюту:")
dropdown_label.grid(row=1, column=1)
dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=currents)
dropdown.grid(row=2, column=1)
dropdown.bind("<<ComboboxSelected>>", lambda event=None: on_dropdown_select)

# Малюнок
flag_usd = PhotoImage(file="united-states.png")
flag_eur = PhotoImage(file="european-union.png")
flag_uah = PhotoImage(file="ukraine.png")

image_label = ttk.Label(root, image=flag_usd)
image_label.grid(row=2, column=2)


# Поле для введення цифр
input_label = ttk.Label(root, text="Введіть кількість:")
input_label.grid(row=3, column=1)
input_entry = ttk.Entry(root)
input_entry.grid(row=4, column=1)

# Кнопка зі стрілочками
calculate_button = ttk.Button(root, text="Обчислити", command=calculate_result)
calculate_button.grid(row=3, column=2, sticky=W)

# Надпис UAH
uah_label = ttk.Label(root, image=flag_uah, text="UAH:", compound="left")
uah_label.grid(row=6, column=1, sticky=E)

# Результат обчислення
result_var = StringVar()
result_label = ttk.Label(root, textvariable=result_var)
result_label.grid(row=6, column=2, sticky=W)

root.mainloop()
