import httpx

from pprint import pprint
input_val = float(input('zadej castku'))

target_curr='EUR'

r = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt')

lines_list = r.text.split('\n')

target_line = ''
for line in lines_list:
    if target_curr in line:
        target_curr = line

exchange_rate = float(target_line.split('|')[-1].replace(',','.'))

output_val = input_val / exchange_rate

print(f"Aktualni hodnota: {output_val:.2f} {target_curr}")
