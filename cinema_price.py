print('Программа для подсчета стоимости билетов в кино.')
film=input('Выбрать фильм:')
day=input('Выбрать день (сегодня, завтра):')
time=float(input('Выбрать время:'))
count=float(input('Выбрать количество билетов:'))
if film=='Пятница':
    if day=='завтра':
        if count>=20:
            if time==12:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*0.95*250*count)
            elif time==16:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*0.95*350*count)
            elif time==20:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*0.95*450*count)
        else:
            if time==12:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.95*250*count)
            elif time==16:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.95*350*count)
            elif time==20:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.95*450*count)
    elif day=='сегодня':
        if count>=20:
            if time==12:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*250*count)
            elif time==16:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*350*count)
            elif time==20:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*450*count)
        else:
            if time==12:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 250*count)
            elif time==16:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 350*count)
            elif time==20:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 450*count)
elif film=='Чемпионы':
    if day=='завтра':
        if count>=20:
            if time==10:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*0.95*250*count)
            elif time==13:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*0.95*350*count)
            elif time==16:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*0.95*350*count)
        else:
            if time==10:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.95*250*count)
            elif time==13:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.95*350*count)
            elif time==16:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.95*350*count)
    elif day=='сегодня':
        if count>=20:
            if time==10:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*250*count)
            elif time==13:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*350*count)
            elif time==16:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*350*count)
        else:
            if time==10:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 250*count)
            elif time==13:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 350*count)
            elif time==16:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 350*count)
elif film=='Пернатая банда':
    if day=='завтра':
        if count>=20:
            if time==10:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*0.95*350*count)
            elif time==14:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*0.95*450*count)
            elif time==18:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*0.95*450*count)
        else:
            if time==10:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.95*350*count)
            elif time==14:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.95*450*count)
            elif time==18:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.95*450*count)
    elif day=='сегодня':
        if count>=20:
            if time==10:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*350*count)
            elif time==14:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*450*count)
            elif time==18:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 0.8*450*count)
        else:
            if time==10:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 350*count)
            elif time==14:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 450*count)
            elif time==18:
                print ('Выбрали фильм:', film,' День: ',day,' Время: ',time,' Количество билетов: ',count)
                print ('Результат: ', 450*count)
else:
    print('Ошибка ввода')
