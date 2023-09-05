import re

list_all = ['USD37,4250-0.0738,1000-0.0536,56860.00', 'EUR40,6000-0.1541,4900-0.1139,62210.00', 'PLN8,81000.019,2800-0.078,86620.00', 'PLN8,81000.019,2800-0.078,86620.00', 'GBP46,10000.1048,2000-0.2046,33420.00', 'CHF41,4000-0.1043,02500.0341,40.00', 'USD37,630.0237,800.00', 'EUR40,770.0241,150.00', 'PLN9,000.009,200.00', 'GBP47,150.0048,150.00', 'CHF42,000.0042,950.00', 'ВалютаКупівляПродаж']

one_item = 'USD37,4250-0.0738,1000-0.0536,56860.00'

x = 'USD'
pattern = re.compile(r"USD(\d+,\d+)")

usd_values = [re.search(pattern, item).group(1) for item in list_all if re.search(pattern, item)]

list_float = []
for i in usd_values:
    list_float.append(float(i.replace(',','.')))
total = sum(list_float)
midl_num = total/len(list_float)
print(midl_num)