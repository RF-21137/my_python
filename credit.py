# credit.py
import csv
region = dict()    
try:   
    with open('opendata.csv', encoding='cp1251') as csvfile:
        money_reader = csv.reader(csvfile, delimiter=',')
        for row in money_reader:
            if row[0] == 'Количество заявок на потребительские кредиты':
                #print(row)
                if row[2].split('-')[0] == '2017':                    
                    if row[1] in region:
                        region[row[1]] += int(row[3])
                    else:
                        region[row[1]] = int(row[3])   

except Exception as e:
    print(e)

for i in sorted(region, key=region.get, reverse=True):
    print(i, region[i])
