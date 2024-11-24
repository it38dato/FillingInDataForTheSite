Цель:
#
Skills:
# Разработка Автоматизация процесса заполнения данных.
Task:
Автоматизировать процесс заполнения данных в excel для довесов технологии 2g, 4g Ericsson, 2g, 4g Nokia.
# Разработка Автоматизация процесса заполнения данных.
Decision:
'''print("Введите список БС:")
A = list(map(str, input().split()))
print(A)'''
import pandas as pd
#2gEricsson
'''cols = [2, 6, 8, 12, 13, 14, 16, 17, 20, 66, 67, 68, 69]
table = pd.read_excel('Table integrated sites.xlsx', skiprows=1, usecols=cols)
#print(table.head())
ces = table[table['BSS'].isna()]
#print(ces)
ces=ces.drop('BSS', axis=1)
delcol=ces['CELL']
ces=ces.drop('CELL', axis=1)
ces.insert(11, 'CELL', delcol)
#print(ces)
cols = [0, 4, 8]
unloading = pd.read_excel('Er_21102024.xlsx', usecols=cols, sheet_name='GeranCell')
#print(unloading.head())
#result = pd.merge(ces, unloading, left_on='CELL',right_on='GeranCellId', how='outer')
result = pd.merge(ces, unloading, left_on='CELL',right_on='GeranCellId', how='inner')
#print(result)
renamecol = "GeranCellId"
result[renamecol] = result[renamecol].str[0:6]
#print(result)
result['TG'] = result['TG'].fillna('0')
result=result.fillna('-')
#print(result)
result=result.drop('BSC', axis=1)
result=result.drop('RSITE', axis=1)
result=result.drop('LAC_x', axis=1)
delcol=result['NodeId']
result=result.drop('NodeId', axis=1)
result.insert(2, 'NodeId', delcol)
delcol=result['GeranCellId']
result=result.drop('GeranCellId', axis=1)
result.insert(4, 'GeranCellId', delcol)
delcol=result['LAC_y']
result=result.drop('LAC_y', axis=1)
result.insert(6, 'LAC_y', delcol)
result.to_csv('tempfile.csv', sep=',', index=False, header=False)'''
#4gEricsson
def unloadingSite(coll1, coll2, coll3, coll4):
    cols = [coll1, coll2, coll3, coll4]
    table = pd.read_excel('Ericsson4g Table integrated sites.xlsx', skiprows=1, usecols=cols)
    table=table[table['BSS'].isna()]
    table=table.drop('BSS', axis=1)
    copycol=table['System_module_name_4G']
    table.insert(3, 'BS_NAME_ID1', copycol)
    valcol = "BS_NAME_ID1"#!
    table[valcol] = table[valcol].str[0:6]#!
    return table
#print(unloadingSite(2, 6, 8, 18))
def unloadingEricsson(coll1, coll2):
    cols = [coll1, coll2]
    table = pd.read_excel('Er_05112024.xlsx', usecols=cols, sheet_name='GeranCell')
    copycol=table['GeranCellId']
    table.insert(2, 'BS_NAME_ID2', copycol)
    valcol = "BS_NAME_ID2"#!
    table[valcol] = table[valcol].str[0:6]#!
    table=table.drop('GeranCellId', axis=1)
    table=table.drop_duplicates()
    return table
#print(unloadingEricsson(4, 8))
def resultTable():
    result = pd.merge(unloadingSite(2, 6, 8, 18), unloadingEricsson(4, 8), left_on='BS_NAME_ID1', right_on='BS_NAME_ID2', how='inner')
    result=result.drop('BS_NAME_ID1', axis=1)
    result=result.drop('BS_NAME_ID2', axis=1)
    result = result.reindex(columns=['Reg', 'System_module_name_4G', 'LAC', 'Sector_name'])
    result.to_csv('tempfile.csv', sep=',', index=False, header=False)
    return result
#print(resultTable())
Source:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html - Как объединить две таблицы в pandas?
# https://sky.pro/wiki/python/udalenie-dublikatov-v-pandas-data-frame-po-vybrannym-kolonkam/ - Удаление дубликатов в Pandas DataFrame по выбранным колонкам.
Task:
Вывести всю информацию одной БС из файла kml.
# Разработка Автоматизация процесса заполнения данных.
Decision:
PS C:\Windows\system32> cat .\tpy.py
#1 перечислить список команд, которые может выполнить программа:
repeat="y"
listcmd=['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
#2 Создать пустой файл, который будет очищать при первом запуске и дублировать в дальнейшем информацию из консоли программы:
with open("output.txt", "w") as outfile:
    outfile.write("") 
while repeat == "y":
    print("Выполните действия, которые необходимо выполнить в CES:")    
    print(listcmd)
    choicecmd = input()
    #print(choicecmd)
    if choicecmd == '1':
        print("Добавьте файлы формата kml в папке где находится программа для дальнейшей обработки данных")
        #3 Вывести всю информацию одной БС из файла kml:
        with open("Site_IR000478_1.kml","r", encoding="utf8") as rdbfile:
            file = rdbfile.read()
        #print(file)
        with open("output.txt", "a") as outfile:
            outfile.write(file)
    elif choicecmd == '2':
        print("Ты выбрал Заполненние довесов БС Nokia")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Nokia"+"\n")
    elif choicecmd == '3':
        print("Ты выбрал Заполненние довесов БС Ericsson")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Ericsson"+"\n")
    repeat = input("Do you want to continue? (y/n): ")
    if repeat == "n":
        break
PS C:\Windows\system32> python .\tpy.py
Выполните действия, которые необходимо выполнить в CES:
['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
1
Добавьте файлы формата kml для дальнейшей обработки данных
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2"> <Placemark>
<name>IR000478/1</name>
<description>Область Иркутская, Район Черемховский, Деревня Хандагай\16а</description>
<Point>
<coordinates>102.149558,53.127582,0</coordinates>
</Point>
</Placemark></kml>
Do you want to continue? (y/n): n
Task:
В двух файлах название БС, координаты, LAC и BSC отображаются в одном атрибуте Placemark. Нужно вывести всю информацию внутри атрибута Placemark.
# Разработка Автоматизация процесса заполнения данных.
Decision:
PS C:\Windows\system32> cat .\tpy.py
import re
#1 перечислить список команд, которые может выполнить программа:
repeat="y"
listcmd=['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
#2 Создать пустой файл, который будет очищать при первом запуске и дублировать в дальнейшем информацию из консоли программы:
with open("output.txt", "w") as outfile:
    outfile.write("") 
while repeat == "y":
    print("Выполните действия, которые необходимо выполнить в CES:")    
    print(listcmd)
    choicecmd = input()
    #print(choicecmd)
    if choicecmd == '1':
        print("Добавьте файлы формата kml в папке где находится программа для дальнейшей обработки данных.")
        #3 Вывести всю информацию одной БС из файла kml:
        with open("Site_IR000478_1.kml","r", encoding="utf8") as rdbfile:
            file = rdbfile.read()
        #print(file)
        #4 В двух файлах название БС, координаты, LAC и BSC отображаются в одном атрибуте Placemark. Нужно вывести всю информацию внутри атрибута Placemark:
        Placemark = re.findall(r'<Placemark>(.*?)</Placemark>', file, re.DOTALL)
        for i in Placemark:
            print(i)
            with open("output.txt", "a") as outfile:
                outfile.write(i)
    elif choicecmd == '2':
        print("Ты выбрал Заполненние довесов БС Nokia")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Nokia"+"\n")
    elif choicecmd == '3':
        print("Ты выбрал Заполненние довесов БС Ericsson")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Ericsson"+"\n")
    repeat = input("Do you want to continue? (y/n): ")
    if repeat == "n":
        break
PS C:\Windows\system32> python .\tpy.py
['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
1
Добавьте файлы формата kml в папке где находится программа для дальнейшей обработки данных.
<name>IR000478/1</name>
<description>Область Иркутская, Район Черемховский, Деревня Хандагай\16а</description>
<Point>
<coordinates>102.149558,53.127582,0</coordinates>
</Point>
Do you want to continue? (y/n): n
Task:
Написать код, который выводит Имя БС в каждом фрагменте Placemark выводит его в нужном формате и добавить в пустой список
# Разработка Автоматизация процесса заполнения данных.
Decision:
PS C:\Windows\system32> cat .\tpy.py
import re
#1 перечислить список команд, которые может выполнить программа:
repeat="y"
listcmd=['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
namelist=[]
#2 Создать пустой файл, который будет очищать при первом запуске и дублировать в дальнейшем информацию из консоли программы:
with open("output.txt", "w") as outfile:
    outfile.write("") 
while repeat == "y":
    print("Выполните действия, которые необходимо выполнить в CES:")    
    print(listcmd)
    choicecmd = input()
    #print(choicecmd)
    if choicecmd == '1':
        print("Добавьте файлы формата kml в папке где находится программа для дальнейшей обработки данных.")
        #3 Вывести всю информацию одной БС из файла kml:
        with open("Site_IR000478_1.kml","r", encoding="utf8") as rdbfile:
            file = rdbfile.read()
        #print(file)
        #4 В двух файлах название БС, координаты, LAC и BSC отображаются в одном атрибуте Placemark. Нужно вывести всю информацию внутри атрибута Placemark:
        Placemark = re.findall(r'<Placemark>(.*?)</Placemark>', file, re.DOTALL)
        for i in Placemark:
            #print(i)
            #5 Написать код, который выводит Имя БС в каждом фрагменте Placemark, выводит его в нужном формате и добавить в пустой список:
            listbs = re.findall(r'<name>(.*?)</name>', i, re.DOTALL)
            print(listbs)
            for bs in listbs:
                if '/' in bs:
                    bs = bs.split('/')[0]
                    i1 = 2
                    i2 = 3
                    bs = bs[:i1] + bs[i2+1:]
                    namelist.append(bs)
                    print(namelist)                       
                    print(bs)
                    with open("output.txt", "a") as outfile:
                        outfile.write(bs)
                else:
                    print("Имя базой станции другого формата!")
                    with open("output.txt", "a") as outfile:
                        outfile.write("Имя базой станции другого формата!")
        print(namelist)
    elif choicecmd == '2':
        print("Ты выбрал Заполненние довесов БС Nokia")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Nokia"+"\n")
    elif choicecmd == '3':
        print("Ты выбрал Заполненние довесов БС Ericsson")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Ericsson"+"\n")
    repeat = input("Do you want to continue? (y/n): ")
    if repeat == "n":
        break
PS C:\Windows\system32> python .\tpy.py
Выполните действия, которые необходимо выполнить в CES:
['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
1
Добавьте файлы формата kml в папке где находится программа для дальнейшей обработки данных.
['IR000478/1']
IR0478
['IR0478']
Do you want to continue? (y/n): n
Task:
Написать код, который выводит координаты в каждом фрагменте Placemark и выводит их в нужном формате и добавить в пустой список
# Разработка Автоматизация процесса заполнения данных.
Decision:
PS C:\Windows\system32> cat .\tpy.py
import re
#1 перечислить список команд, которые может выполнить программа:
repeat="y"
listcmd=['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
namelist=[]
listxy=[]
#2 Создать пустой файл, который будет очищать при первом запуске и дублировать в дальнейшем информацию из консоли программы:
with open("output.txt", "w") as outfile:
    outfile.write("") 
while repeat == "y":
    print("Выполните действия, которые необходимо выполнить в CES:")    
    print(listcmd)
    choicecmd = input()
    #print(choicecmd)
    if choicecmd == '1':
        print("Добавьте файлы формата kml в папке где находится программа для дальнейшей обработки данных.")
        #3 Вывести всю информацию одной БС из файла kml:
        with open("Site_IR000478_1.kml","r", encoding="utf8") as rdbfile:
            file = rdbfile.read()
        #print(file)
        #4 В двух файлах название БС, координаты, LAC и BSC отображаются в одном атрибуте Placemark. Нужно вывести всю информацию внутри атрибута Placemark:
        Placemark = re.findall(r'<Placemark>(.*?)</Placemark>', file, re.DOTALL)
        for i in Placemark:
            #print(i)
            #5 Написать код, который выводит Имя БС в каждом фрагменте Placemark, выводит его в нужном формате и добавить в пустой список:
            listbs = re.findall(r'<name>(.*?)</name>', i, re.DOTALL)
            #print(listbs)
            for bs in listbs:
                if '/' in bs:
                    bs = bs.split('/')[0]
                    i1 = 2
                    i2 = 3
                    bs = bs[:i1] + bs[i2+1:]
                    namelist.append(bs)
                    print(bs)
                    with open("output.txt", "a") as outfile:
                        outfile.write(bs + "\n")
                else:
                    print("Имя базой станции другого формата!")
                    with open("output.txt", "a") as outfile:
                        outfile.write("Имя базой станции другого формата!\n")
            #6 Написать код, который выводит координаты в каждом фрагменте Placemark и выводит его в нужном формате и добавить в пустой список:
            listcoords = re.findall(r'<coordinates>(.*?)</coordinates>', i, re.DOTALL)
            #print(listcoords)
            for coords in listcoords:
                #print(coords)
                longitude = coords.split(',')[0]
                latitude = coords.split(',')[1]
                print(longitude + " " + latitude + "\n")
                with open("output.txt", "a") as outfile:
                    outfile.write(longitude + " " + latitude + "\n")
                listxy.append(longitude)
                listxy.append(latitude)
        print(namelist)
        print(listxy)
    elif choicecmd == '2':
        print("Ты выбрал Заполненние довесов БС Nokia")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Nokia"+"\n")
    elif choicecmd == '3':
        print("Ты выбрал Заполненние довесов БС Ericsson")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Ericsson"+"\n")
    repeat = input("Do you want to continue? (y/n): ")
    if repeat == "n":
        break
PS C:\Windows\system32> python .\tpy.py
Выполните действия, которые необходимо выполнить в CES:
['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
1
Добавьте файлы формата kml в папке где находится программа для дальнейшей обработки данных.
IR0478
102.149558 53.127582
['IR0478']
['102.149558', '53.127582']
Do you want to continue? (y/n): n
# Разработка Автоматизация процесса заполнения данных.
Создать словарь и собрать данные: key - ИМЯ БС, value - Координаты.
# Разработка Автоматизация процесса заполнения данных.
Decision:
PS C:\Windows\system32> cat .\tpy.py
import re
#1 перечислить список команд, которые может выполнить программа:
repeat="y"
listcmd=['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
listname=[]
listxy=[]
#7 Создать словарь и собрать данные: key - ИМЯ БС, value - Координаты, TAC, BSC:
datasites = dict()
#2 Создать пустой файл, который будет очищать при первом запуске и дублировать в дальнейшем информацию из консоли программы:
with open("output.txt", "w") as outfile:
    outfile.write("") 
while repeat == "y":
    print("Выполните действия, которые необходимо выполнить в CES:")    
    print(listcmd)
    choicecmd = input()
    #print(choicecmd)
    if choicecmd == '1':
        print("Добавьте файлы формата kml в папке где находится программа для дальнейшей обработки данных.")
        #3 Вывести всю информацию одной БС из файла kml:
        with open("Site_IR000478_1.kml","r", encoding="utf8") as rdbfile:
            file = rdbfile.read()
        #print(file)
        #4 В двух файлах название БС, координаты, LAC и BSC отображаются в одном атрибуте Placemark. Нужно вывести всю информацию внутри атрибута Placemark:
        Placemark = re.findall(r'<Placemark>(.*?)</Placemark>', file, re.DOTALL)
        for i in Placemark:
            #print(i)
            #5 Написать код, который выводит Имя БС в каждом фрагменте Placemark, выводит его в нужном формате и добавить в пустой список:
            listbs = re.findall(r'<name>(.*?)</name>', i, re.DOTALL)
            #print(listbs)
            for bs in listbs:
                if '/' in bs:
                    bs = bs.split('/')[0]
                    i1 = 2
                    i2 = 3
                    bs = bs[:i1] + bs[i2+1:]
                    listname.append(bs)
                    print(bs)
                    with open("output.txt", "a") as outfile:
                        outfile.write(bs + "\n")
                else:
                    print("Имя базой станции другого формата!")
                    with open("output.txt", "a") as outfile:
                        outfile.write("Имя базой станции другого формата!\n")
            #6 Написать код, который выводит координаты в каждом фрагменте Placemark и выводит его в нужном формате и добавить в пустой список:
            listcoords = re.findall(r'<coordinates>(.*?)</coordinates>', i, re.DOTALL)
            #print(listcoords)
            for coords in listcoords:
                #print(coords)
                longitude = coords.split(',')[0]
                latitude = coords.split(',')[1]
                print(longitude + " " + latitude + "\n")
                with open("output.txt", "a") as outfile:
                    outfile.write(longitude + " " + latitude + "\n")
                listxy.append(longitude)
                listxy.append(latitude)
        print(listname)
        print(listxy)
        #7
        #datasites["test1"]="test2"        
        datasites[listname[0]]=listxy
        print(datasites)        
    elif choicecmd == '2':
        print("Ты выбрал Заполненние довесов БС Nokia")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Nokia"+"\n")
    elif choicecmd == '3':
        print("Ты выбрал Заполненние довесов БС Ericsson")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Ericsson"+"\n")
    repeat = input("Do you want to continue? (y/n): ")
    if repeat == "n":
        break
PS C:\Windows\system32> python .\tpy.py
Выполните действия, которые необходимо выполнить в CES:
['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
1
Добавьте файлы формата kml в папке где находится программа для дальнейшей обработки данных.
IR0478
102.149558 53.127582
['IR0478']
['102.149558', '53.127582']
{'IR0478': ['102.149558', '53.127582']}
Do you want to continue? (y/n): n
Task:
Собрать данные для второго файла, в котором есть bsc и Tac.
# Разработка Автоматизация процесса заполнения данных.
Decision:
PS C:\Windows\system32> cat .\tpy.py
import re
#1 перечислить список команд, которые может выполнить программа:
repeat="y"
listcmd=['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
listname=[]
listxy=[]
listallname=[]
listall=[]
#7 Создать словарь и собрать данные: key - ИМЯ БС, value - Координаты, TAC, BSC:
datasites = dict()
#2 Создать пустой файл, который будет очищать при первом запуске и дублировать в дальнейшем информацию из консоли программы:
with open("output.txt", "w") as outfile:
    outfile.write("") 
while repeat == "y":
    print("Выполните действия, которые необходимо выполнить в CES:")    
    print(listcmd)
    choicecmd = input()
    #print(choicecmd)
    if choicecmd == '1':
        print("Добавьте файлы формата kml в папке где находится программа для дальнейшей обработки данных.")
        #3 Вывести всю информацию одной БС из файла kml:
        with open("Site_IR000478_1.kml","r", encoding="utf8") as rdbfile:
            file = rdbfile.read()
        #print(file)
        #4 В двух файлах название БС, координаты, LAC и BSC отображаются в одном атрибуте Placemark. Нужно вывести всю информацию внутри атрибута Placemark:
        Placemark = re.findall(r'<Placemark>(.*?)</Placemark>', file, re.DOTALL)
        for i in Placemark:
            #print(i)
            #5 Написать код, который выводит Имя БС в каждом фрагменте Placemark, выводит его в нужном формате и добавить в пустой список:
            listbs = re.findall(r'<name>(.*?)</name>', i, re.DOTALL)
            #print(listbs)
            for bs in listbs:
                if '/' in bs:
                    bs = bs.split('/')[0]
                    i1 = 2
                    i2 = 3
                    bs = bs[:i1] + bs[i2+1:]
                    listname.append(bs)
                    #print(bs)
                    with open("output.txt", "a") as outfile:
                        outfile.write(bs + "\n")
                else:
                    #print("Имя базой станции другого формата!")
                    with open("output.txt", "a") as outfile:
                        outfile.write("Имя базой станции другого формата!\n")
            #6 Написать код, который выводит координаты в каждом фрагменте Placemark и выводит его в нужном формате и добавить в пустой список:
            listcoords = re.findall(r'<coordinates>(.*?)</coordinates>', i, re.DOTALL)
            #print(listcoords)
            for coords in listcoords:
                #print(coords)
                longitude = coords.split(',')[0]
                latitude = coords.split(',')[1]
                #print(longitude + " " + latitude + "\n")
                with open("output.txt", "a") as outfile:
                    outfile.write(longitude + " " + latitude + "\n")
                listxy.append(longitude)
                listxy.append(latitude)
        #print(listname)
        #print(listxy)
        #7
        #datasites["test1"]="test2"        
        datasites[listname[0]]=listxy
        print(datasites)
        #8 Собрать данные для второго файла, в котором есть Bsc и Lac:
        with open("IR.kml","r", encoding="utf8") as rdbfile:
            file = rdbfile.read()
        #print(file)
        Placemark = re.findall(r'<Placemark>(.*?)</Placemark>', file, re.DOTALL)
        for i in Placemark:
            #print(i)
            #if '<longitude>' and 'LAC' in i:
            if ('<longitude>' in i) and ('LAC' in i) and ('BSC: ' in i):
                listbs = re.findall(r'<name>(.*?)</name>', i, re.DOTALL)
                #print(listbs)
                for bs in listbs:
                    if (len(bs)==6) == True:
                        #print(bs)
                        listallname.append(bs)
                        with open("output.txt", "a") as outfile:
                            outfile.write(bs + "\n")
                    else:
                        #print("Имя базой станции другого формата!")
                        with open("output.txt", "a") as outfile:
                            outfile.write("Имя базой станции другого формата!\n")
                listcoords = re.findall(r'<longitude>(.*?)</latitude>', i, re.DOTALL)
                #print(listcoords)
                for coords in listcoords:
                    #print(coords)
                    coordinates = coords.split('</longitude>\n     <latitude>')
                    #print(coordinates)
                    longitude = coordinates[0]
                    latitude = coordinates[1]
                    #print(longitude + " " + latitude + "\n")
                    with open("output.txt", "a") as outfile:
                        outfile.write(longitude + " " + latitude + "\n")
                    listall.append(longitude)
                    listall.append(latitude)
                listbsctac = re.findall(r'<description>BSC: (.*?)</description>', i, re.DOTALL)
                #print(listbsctac)
                for data in listbsctac:
                    #print(data)
                    datas = data.split(' LAC: ')
                    #print(datas)
                    bsc = datas[0]
                    lac = datas[1]
                    #print(bsc + " " + lac + "\n")
                    with open("output.txt", "a") as outfile:
                        outfile.write(bsc + " " + lac + "\n")
                    listall.append(bsc)
                    listall.append(lac)
            else:
                #print("Координаты отсутсвуют!")
                #with open("output.txt", "a") as outfile:
                #    outfile.write("Координаты отсутсвуют!\n")
                break
        #print(listallname)
        print(listall)
    elif choicecmd == '2':
        print("Ты выбрал Заполненние довесов БС Nokia")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Nokia"+"\n")
    elif choicecmd == '3':
        print("Ты выбрал Заполненние довесов БС Ericsson")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Ericsson"+"\n")
    repeat = input("Do you want to continue? (y/n): ")
    if repeat == "n":
        break
Task:
Добавить в словарь данные загруженные из второго файла
[n1]
[x1,y1]
{n1:[x1,y1]}
[name1,name2,name3]
[datax1,datay1,datalac1,datax2,datay2,datalac2,datax3,datay3,datalac3]
{n1:[x1,y1], name1:[datax1,datay1,datalac1], name2:[datax2,datay2,datalac2], name3:[datax3,datay3,datalac3]}
# Разработка Автоматизация процесса заполнения данных.
Decision:
PS C:\Windows\system32> cat .\tpy.py
import re
#1 перечислить список команд, которые может выполнить программа:
repeat="y"
listcmd=['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
listname=[]
listxy=[]
listallname=[]
listall=[]
#7 Создать словарь и собрать данные: key - ИМЯ БС, value - Координаты, TAC, BSC:
datasites = dict()
#2 Создать пустой файл, который будет очищать при первом запуске и дублировать в дальнейшем информацию из консоли программы:
with open("output.txt", "w") as outfile:
    outfile.write("") 
while repeat == "y":
    print("Выполните действия, которые необходимо выполнить в CES:")    
    print(listcmd)
    choicecmd = input()
    #print(choicecmd)
    if choicecmd == '1':
        print("Добавьте файлы формата kml в папке где находится программа для дальнейшей обработки данных.")
        #3 Вывести всю информацию одной БС из файла kml:
        with open("Site_IR000478_1.kml","r", encoding="utf8") as rdbfile:
            file = rdbfile.read()
        #print(file)
        #4 В двух файлах название БС, координаты, LAC и BSC отображаются в одном атрибуте Placemark. Нужно вывести всю информацию внутри атрибута Placemark:
        Placemark = re.findall(r'<Placemark>(.*?)</Placemark>', file, re.DOTALL)
        for i in Placemark:
            #print(i)
            #5 Написать код, который выводит Имя БС в каждом фрагменте Placemark, выводит его в нужном формате и добавить в пустой список:
            listbs = re.findall(r'<name>(.*?)</name>', i, re.DOTALL)
            #print(listbs)
            for bs in listbs:
                if '/' in bs:
                    bs = bs.split('/')[0]
                    i1 = 2
                    i2 = 3
                    bs = bs[:i1] + bs[i2+1:]
                    listname.append(bs)
                    #print(bs)
                    with open("output.txt", "a") as outfile:
                        outfile.write(bs + "\n")
                else:
                    #print("Имя базой станции другого формата!")
                    with open("output.txt", "a") as outfile:
                        outfile.write("Имя базой станции другого формата!\n")
            #6 Написать код, который выводит координаты в каждом фрагменте Placemark и выводит его в нужном формате и добавить в пустой список:
            listcoords = re.findall(r'<coordinates>(.*?)</coordinates>', i, re.DOTALL)
            #print(listcoords)
            for coords in listcoords:
                #print(coords)
                longitude = coords.split(',')[0]
                latitude = coords.split(',')[1]
                #print(longitude + " " + latitude + "\n")
                with open("output.txt", "a") as outfile:
                    outfile.write(longitude + " " + latitude + "\n")
                listxy.append(longitude)
                listxy.append(latitude)
        #print(listname)
        #print(listxy)
        #7
        #datasites["test1"]="test2"        
        datasites[listname[0]]=listxy
        #print(datasites)
        #8 Собрать данные для второго файла, в котором есть Bsc и Lac:
        with open("IR.kml","r", encoding="utf8") as rdbfile:
            file = rdbfile.read()
        #print(file)
        Placemark = re.findall(r'<Placemark>(.*?)</Placemark>', file, re.DOTALL)
        for i in Placemark:
            #print(i)
            #if '<longitude>' and 'LAC' in i:
            if ('<longitude>' in i) and ('LAC' in i) and ('BSC: ' in i):
                listbs = re.findall(r'<name>(.*?)</name>', i, re.DOTALL)
                #print(listbs)
                for bs in listbs:
                    if (len(bs)==6) == True:
                        #print(bs)
                        listallname.append(bs)
                        with open("output.txt", "a") as outfile:
                            outfile.write(bs + "\n")                           
                    else:
                        #print("Имя базой станции другого формата!")
                        with open("output.txt", "a") as outfile:
                            outfile.write("Имя базой станции другого формата!\n")
                listcoords = re.findall(r'<longitude>(.*?)</latitude>', i, re.DOTALL)
                #print(listcoords)
                for coords in listcoords:
                    #print(coords)
                    coordinates = coords.split('</longitude>\n     <latitude>')
                    #print(coordinates)
                    longitude = coordinates[0]
                    latitude = coordinates[1]
                    #print(longitude + " " + latitude + "\n")
                    with open("output.txt", "a") as outfile:
                        outfile.write(longitude + " " + latitude + "\n")
                    listall.append(longitude)
                    listall.append(latitude)
                listbsctac = re.findall(r'<description>BSC: (.*?)</description>', i, re.DOTALL)
                #print(listbsctac)
                for data in listbsctac:
                    #print(data)
                    datas = data.split(' LAC: ')
                    #print(datas)
                    bsc = datas[0]
                    lac = datas[1]
                    #print(bsc + " " + lac + "\n")
                    with open("output.txt", "a") as outfile:
                        outfile.write(bsc + " " + lac + "\n")
                    listall.append(bsc)
                    listall.append(lac)
            else:
                #print("Координаты отсутсвуют!")
                #with open("output.txt", "a") as outfile:
                #    outfile.write("Координаты отсутсвуют!\n")
                break
        #9 Добавить в словарь данные загруженные из второго файла:
        #print(listallname)
        #print(listall)
        remainder = (len(listall)//len(listallname))
        #print(remainder)
        for numeration in range(len(listallname)):
            #print(numeration)
            datasites[listallname[numeration]] = [listall[y] for y in range(remainder*numeration,remainder*numeration+remainder)]
        print(datasites)
    elif choicecmd == '2':
        print("Ты выбрал Заполненние довесов БС Nokia")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Nokia"+"\n")
    elif choicecmd == '3':
        print("Ты выбрал Заполненние довесов БС Ericsson")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Ericsson"+"\n")
    repeat = input("Do you want to continue? (y/n): ")
    if repeat == "n":
        break
PS C:\Windows\system32> python .\tpy.py
Task:
Сравнить элементы из первого ключа с последующими в словаре и при совпадении выдать ключ и значения из словаря.
Есть словарь:
{n1:[x1,y1], name1:[datax1,datay1,datalac1], name2:[datax2,datay2,datalac2], name3:[datax3,datay3,datalac3]}
Как значения x1,y1 сравнить с последующими значениями от datax1,datay1 до datax3,datay3 в словаре? 
если значения равны, то вывести имя и коорднаты, например, name3, datax3, datay3.
# Разработка Автоматизация процесса заполнения данных.
Decision:
PS C:\Windows\system32> cat .\tpy.py
import re
#1 перечислить список команд, которые может выполнить программа:
repeat="y"
listcmd=['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
listname=[]
listxy=[]
listallname=[]
listall=[]
#7 Создать словарь и собрать данные: key - ИМЯ БС, value - Координаты, TAC, BSC:
datasite = dict()
datasites = dict()
#2 Создать пустой файл, который будет очищать при первом запуске и дублировать в дальнейшем информацию из консоли программы:
with open("output.txt", "w") as outfile:
    outfile.write("") 
while repeat == "y":
    print("Выполните действия, которые необходимо выполнить в CES:")    
    print(listcmd)
    choicecmd = input()
    #print(choicecmd)
    if choicecmd == '1':
        print("Добавьте файлы формата kml в папке где находится программа для дальнейшей обработки данных.")
        #3 Вывести всю информацию одной БС из файла kml:
        with open("Site_IR000478_1.kml","r", encoding="utf8") as rdbfile:
            file = rdbfile.read()
        #print(file)
        #4 В двух файлах название БС, координаты, LAC и BSC отображаются в одном атрибуте Placemark. Нужно вывести всю информацию внутри атрибута Placemark:
        Placemark = re.findall(r'<Placemark>(.*?)</Placemark>', file, re.DOTALL)
        for i in Placemark:
            #print(i)
            #5 Написать код, который выводит Имя БС в каждом фрагменте Placemark, выводит его в нужном формате и добавить в пустой список:
            listbs = re.findall(r'<name>(.*?)</name>', i, re.DOTALL)
            #print(listbs)
            for bs in listbs:
                if '/' in bs:
                    bs = bs.split('/')[0]
                    i1 = 2
                    i2 = 3
                    bs = bs[:i1] + bs[i2+1:]
                    listname.append(bs)
                    #print(bs)
                    with open("output.txt", "a") as outfile:
                        outfile.write(bs + "\n")
                else:
                    #print("Имя базой станции другого формата!")
                    with open("output.txt", "a") as outfile:
                        outfile.write("Имя базой станции другого формата!\n")
            #6 Написать код, который выводит координаты в каждом фрагменте Placemark и выводит его в нужном формате и добавить в пустой список:
            listcoords = re.findall(r'<coordinates>(.*?)</coordinates>', i, re.DOTALL)
            #print(listcoords)
            for coords in listcoords:
                #print(coords)
                longitude = coords.split(',')[0]
                latitude = coords.split(',')[1]
                #print(longitude + " " + latitude + "\n")
                with open("output.txt", "a") as outfile:
                    outfile.write(longitude + " " + latitude + "\n")
                listxy.append(longitude)
                listxy.append(latitude)
        #print(listname)
        #print(listxy)
        #7
        #datasite["test1"]="test2"        
        datasite[listname[0]]=listxy
        #print(datasite)
        #8 Собрать данные для второго файла, в котором есть Bsc и Lac:
        with open("IR.kml","r", encoding="utf8") as rdbfile:
            file = rdbfile.read()
        #print(file)
        Placemark = re.findall(r'<Placemark>(.*?)</Placemark>', file, re.DOTALL)
        for i in Placemark:
            #print(i)
            #if '<longitude>' and 'LAC' in i:
            if ('<longitude>' in i) and ('LAC' in i) and ('BSC: ' in i):
                listbs = re.findall(r'<name>(.*?)</name>', i, re.DOTALL)
                #print(listbs)
                for bs in listbs:
                    if (len(bs)==6) == True:
                        #print(bs)
                        listallname.append(bs)
                        #with open("output.txt", "a") as outfile:
                        #    outfile.write(bs + "\n")                           
                    else:
                        #print("Имя базой станции другого формата!")
                        with open("output.txt", "a") as outfile:
                            outfile.write("Имя базой станции другого формата!\n")
                listcoords = re.findall(r'<longitude>(.*?)</latitude>', i, re.DOTALL)
                #print(listcoords)
                for coords in listcoords:
                    #print(coords)
                    coordinates = coords.split('</longitude>\n     <latitude>')
                    #print(coordinates)
                    longitude = coordinates[0]
                    latitude = coordinates[1]
                    #print(longitude + " " + latitude + "\n")
                    #with open("output.txt", "a") as outfile:
                    #    outfile.write(longitude + " " + latitude + "\n")
                    listall.append(longitude)
                    listall.append(latitude)
                listbsctac = re.findall(r'<description>BSC: (.*?)</description>', i, re.DOTALL)
                #print(listbsctac)
                for data in listbsctac:
                    #print(data)
                    datas = data.split(' LAC: ')
                    #print(datas)
                    bsc = datas[0]
                    lac = datas[1]
                    #print(bsc + " " + lac + "\n")
                    #with open("output.txt", "a") as outfile:
                    #    outfile.write(bsc + " " + lac + "\n")
                    listall.append(bsc)
                    listall.append(lac)
            else:
                #print("Координаты отсутсвуют!")
                #with open("output.txt", "a") as outfile:
                #    outfile.write("Координаты отсутсвуют!\n")
                break
        #9 Добавить в словарь данные загруженные из второго файла:
        #print(listallname)
        #print(listall)
        remainder = (len(listall)//len(listallname))
        #print(remainder)
        for numeration in range(len(listallname)):
            #print(numeration)
            datasites[listallname[numeration]] = [listall[y] for y in range(remainder*numeration,remainder*numeration+remainder)]
        #print(datasites)
        #10 Сравнить элементы из первого ключа с последующими в словаре и при совпадении выдать ключ и значения из словаря.
        #print(datasites[list(datasites.keys())[0]])
        for key, value in datasite.items():
            #print(key,value[0],value[1])
            for keys, values in  datasites.items():
                #print(keys,values) 
                if key != keys:
                    print("FALSE", key, keys, float(value[0]), float(value[1]), values[0], values[1], values[2], values[3])
                    with open("output.txt", "a") as outfile:
                        outfile.write("FALSE " + key + " " + keys  + " " + value[0]  + " " + value[1]  + " " + values[0]  + " " + values[1]  + " " + values[2]  + " " + values[3] + "\n")                    
                else:
                    print("Уже есть данные LAC и BSC для базовой станции:", key)
                    with open("output.txt", "a") as outfile:
                        outfile.write("Уже есть данные LAC и BSC для базовой станции: " + key + "\n")
    elif choicecmd == '2':
        print("Ты выбрал Заполненние довесов БС Nokia")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Nokia"+"\n")
    elif choicecmd == '3':
        print("Ты выбрал Заполненние довесов БС Ericsson")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Ericsson"+"\n")
    repeat = input("Do you want to continue? (y/n): ")
    if repeat == "n":
        break
PS C:\Windows\system32> python .\tpy.py
Выполните действия, которые необходимо выполнить в CES:
['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
1
....
FALSE IR0478 IR2970 102.149558 102.149558 103.872418234894 52.609637656718 401257 5272
FALSE IR0478 IR2981 102.149558 102.149558 103.885440774559 52.5517154218339 401257 5272
Do you want to continue? (y/n): n
Task:
Найти ближайшего соседа базовой станции по формуле sqrt((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2)).
# Разработка Автоматизация процесса заполнения данных.
Decision:
import re
from math import sqrt, pow
#1 перечислить список команд, которые может выполнить программа:
repeat="y"
listcmd=['Заполненние новых БС Nokia (1)', 'Заполненние довесов БС Nokia (2)', 'Заполненние довесов БС Ericsson (3)']
#2 Создать пустой файл, который будет очищать при первом запуске и дублировать в дальнейшем информацию из консоли программы:
with open("output.txt", "w") as outfile:
    outfile.write("") 
while repeat == "y":
    print("Выполните действия, которые необходимо выполнить в CES:")    
    print(listcmd)
    choicecmd = input()
    #print(choicecmd)
    if choicecmd == '1':
        listname=[]
        listxy=[]
        listallname=[]
        listall=[]
        listmin=[]
        listdistace=[]
        #7 Создать словарь и собрать данные: key - ИМЯ БС, value - Координаты, TAC, BSC:
        datasite = dict()
        datasites = dict()
        print("Добавьте файлы формата kml в папке где находится программа для дальнейшей обработки данных.")
        #3 Вывести всю информацию одной БС из файла kml:
        with open("Site_IR000478_1.kml","r", encoding="utf8") as rdbfile:
            file = rdbfile.read()
        #print(file)
        #4 В двух файлах название БС, координаты, LAC и BSC отображаются в одном атрибуте Placemark. Нужно вывести всю информацию внутри атрибута Placemark:
        Placemark = re.findall(r'<Placemark>(.*?)</Placemark>', file, re.DOTALL)
        for i in Placemark:
            #print(i)
            #5 Написать код, который выводит Имя БС в каждом фрагменте Placemark, выводит его в нужном формате и добавить в пустой список:
            listbs = re.findall(r'<name>(.*?)</name>', i, re.DOTALL)
            #print(listbs)
            for bs in listbs:
                if '/' in bs:
                    bs = bs.split('/')[0]
                    i1 = 2
                    i2 = 3
                    bs = bs[:i1] + bs[i2+1:]
                    listname.append(bs)
                    #print(bs)
                    #with open("output.txt", "a") as outfile:
                    #    outfile.write(bs + "\n")
                else:
                    #print("Имя базой станции другого формата!")
                    with open("output.txt", "a") as outfile:
                        outfile.write("Имя базой станции другого формата!\n")
            #6 Написать код, который выводит координаты в каждом фрагменте Placemark и выводит его в нужном формате и добавить в пустой список:
            listcoords = re.findall(r'<coordinates>(.*?)</coordinates>', i, re.DOTALL)
            #print(listcoords)
            for coords in listcoords:
                #print(coords)
                longitude = coords.split(',')[0]
                latitude = coords.split(',')[1]
                #print(longitude + " " + latitude + "\n")
                #with open("output.txt", "a") as outfile:
                #    outfile.write(longitude + " " + latitude + "\n")
                listxy.append(longitude)
                listxy.append(latitude)
        #print(listname)
        #print(listxy)
        #7
        #datasite["test1"]="test2"        
        datasite[listname[0]]=listxy
        #print(datasite)
        #8 Собрать данные для второго файла, в котором есть Bsc и Lac:
        with open("IR.kml","r", encoding="utf8") as rdbfile:
            file = rdbfile.read()
        #print(file)
        Placemark = re.findall(r'<Placemark>(.*?)</Placemark>', file, re.DOTALL)
        for i in Placemark:
            #print(i)
            #if '<longitude>' and 'LAC' in i:
            if ('<longitude>' in i) and ('LAC' in i) and ('BSC: ' in i):
                listbs = re.findall(r'<name>(.*?)</name>', i, re.DOTALL)
                #print(listbs)
                for bs in listbs:
                    if (len(bs)==6) == True:
                        #print(bs)
                        listallname.append(bs)
                        #with open("output.txt", "a") as outfile:
                        #    outfile.write(bs + "\n")                           
                    else:
                        #print("Имя базой станции другого формата!")
                        with open("output.txt", "a") as outfile:
                            outfile.write("Имя базой станции другого формата!\n")
                listcoords = re.findall(r'<longitude>(.*?)</latitude>', i, re.DOTALL)
                #print(listcoords)
                for coords in listcoords:
                    #print(coords)
                    coordinates = coords.split('</longitude>\n     <latitude>')
                    #print(coordinates)
                    longitude = coordinates[0]
                    latitude = coordinates[1]
                    #print(longitude + " " + latitude + "\n")
                    #with open("output.txt", "a") as outfile:
                    #    outfile.write(longitude + " " + latitude + "\n")
                    listall.append(longitude)
                    listall.append(latitude)
                listbsctac = re.findall(r'<description>BSC: (.*?)</description>', i, re.DOTALL)
                #print(listbsctac)
                for data in listbsctac:
                    #print(data)
                    datas = data.split(' LAC: ')
                    #print(datas)
                    bsc = datas[0]
                    lac = datas[1]
                    #print(bsc + " " + lac + "\n")
                    #with open("output.txt", "a") as outfile:
                    #    outfile.write(bsc + " " + lac + "\n")
                    listall.append(bsc)
                    listall.append(lac)
            else:
                #print("Координаты отсутсвуют!")
                #with open("output.txt", "a") as outfile:
                #    outfile.write("Координаты отсутсвуют!\n")
                break
        #9 Добавить в словарь данные загруженные из второго файла:
        #print(listallname)
        #print(listall)
        remainder = (len(listall)//len(listallname))
        #print(remainder)
        for numeration in range(len(listallname)):
            #print(numeration)
            datasites[listallname[numeration]] = [listall[y] for y in range(remainder*numeration,remainder*numeration+remainder)]
        #print(datasites)
        #10 Сравнить элементы из первого ключа с последующими в словаре и при совпадении выдать ключ и значения из словаря.
        #print(datasites[list(datasites.keys())[0]])
        for key, value in datasite.items():
            #print(key,value[0],value[1])
            for keys, values in  datasites.items():
                #print(key, value[1], value[0], keys, values[1], values[0], values[2], values[3]) 
                if key != keys and values[0] != '':
                    #11 Найти ближайшего соседа базовой станции по формуле sqrt((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2)):
                    #distance=sqrt((float(value[1])-float(values[1])) * (float(value[1])-float(values[1])) + (float(value[0])-float(values[0])) * (float(value[0])-float(values[0])))
                    distance=str(sqrt(pow(float(value[1])-float(values[1]),2) + pow(float(value[0])-float(values[0]),2)))                    
                    listdistace.append(distance)
                    #          x1        y1              x2         y2
                    #print(key, value[1], value[0], keys, values[1], values[0], values[2], values[3], distance)
                    #with open("output.txt", "a") as outfile:
                    #    outfile.write(key  + " " + value[1] +  " " + value[0] +  " " + keys + " " + values[1] +  " " + values[0]  + " " + values[2] +  " " + values[3] + " " + distance + "\n")
                    if distance == min(listdistace):
                        #print(key, value[1], value[0], keys, values[1], values[0], values[2], values[3], distance, min(listdistace))
                        #with open("output.txt", "a") as outfile:
                        #    outfile.write(key  + " " + value[1] +  " " + value[0] +  " " + keys + " " + values[1] +  " " + values[0]  + " " + values[2] +  " " + values[3] + " " + distance + "\n")
                        listmin.append(key)
                        listmin.append(values[2])
                        listmin.append(values[3])
                    else:
                        continue
                elif values[0] == '':
                    #print("У БС", keys, "отсуствуют координаты!")
                    #with open("output.txt", "a") as outfile:
                    #    outfile.write("У БС " + keys + "отсуствуют координаты!\n")
                    continue
                else:
                    print("Уже есть данные LAC и BSC для базовой станции:", key)
                    with open("output.txt", "a") as outfile:
                        outfile.write("Уже есть данные LAC и BSC для базовой станции: " + key + "\n")
        #11
        bsready=listmin[-3:]
        print(bsready[0],bsready[1],bsready[2])
        with open("output.txt", "a") as outfile:
            outfile.write(bsready[0] +  " " + bsready[1] +  " " + bsready[2] + "\n")
        '''#11:
        print(min(listdistace))
        for key, value in datasite.items():
            for keys, values in  datasites.items():
                if key != keys and values[0] != '':
                    distance=str(sqrt(pow(float(value[1])-float(values[1]),2) + pow(float(value[0])-float(values[0]),2)))
                    if distance == min(listdistace):
                        print(key, value[1], value[0], keys, values[1], values[0], values[2], values[3], distance)
                        with open("output.txt", "a") as outfile:
                            outfile.write(key  + " " + value[1] +  " " + value[0] +  " " + keys + " " + values[1] +  " " + values[0]  + " " + values[2] +  " " + values[3] + " " + distance + "\n")  
                    else:
                        #print("FALSE")
                        continue
                elif values[0] == '':
                    continue
                else:
                    print("Уже есть данные LAC и BSC для базовой станции:", key)
                    with open("output.txt", "a") as outfile:
                        outfile.write("Уже есть данные LAC и BSC для базовой станции: " + key + "\n")'''
    elif choicecmd == '2':
        print("Ты выбрал Заполненние довесов БС Nokia")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Nokia"+"\n")
    elif choicecmd == '3':
        print("Ты выбрал Заполненние довесов БС Ericsson")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние довесов БС Ericsson"+"\n")
    repeat = input("Do you want to continue? (y/n): ")
    if repeat == "n":
        break


























Цель:
# Перечислить список команд, которые может выполнить программа.
# Собрать в список данные, которые необходимо заполнить в шаблоне.
# Настроить библиотеку для работы с таблицами excel.
# Найти незаполненные строки БС в таблице из CES.
Skills:
# Разработка Команды для работы с программой.
# Разработка Список данных.
# Администрирование локальных, виртуальных и облачных серверов.
Task:
Перечислить список команд, которые может выполнить программа.
# Разработка Команды для работы с программой.
Decision:
PS C:\Windows\system32> cat .\1cmd.py
#1 перечислить список команд, которые может выполнить программа:
repeat="y"
with open("output.txt", "w") as outfile:
    outfile.write("") 
while repeat == "y":
    print("Выполните действия, которые необходимо выполнить в CES:")
    listcmd=['Заполненние данных для БС Nokia (1)', 'Заполненние данных для БС Ericsson (2)']
    print(listcmd)
    choicecmd = input()
    #print(choicecmd)
    if choicecmd == '1':
        print("Ты выбрал Заполненние данных для БС Nokia")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние данных для БС Nokia"+"\n")
    elif choicecmd == '2':
        print("Ты выбрал Заполненние данных для БС Ericsson")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние данных для БС Ericsson"+"\n")
    else:
        print("Введите y/n")        
    repeat = input("Do you want to continue? (y/n): ")
    if repeat == "n":
        break
    else:
        print("Введите y/n")
PS C:\Windows\system32> python .\1cmd.py
Выполните действия, которые необходимо выполнить в CES:
['Заполненние данных для БС Nokia (1)', 'Заполненние данных для БС Ericsson (2)']
1
Ты выбрал Заполненние данных для БС Nokia
Do you want to continue? (y/n): y
Введите y/n
Выполните действия, которые необходимо выполнить в CES:
['Заполненние данных для БС Nokia (1)', 'Заполненние данных для БС Ericsson (2)']
t
Введите y/n
Do you want to continue? (y/n): y
Введите y/n
Выполните действия, которые необходимо выполнить в CES:
['Заполненние данных для БС Nokia (1)', 'Заполненние данных для БС Ericsson (2)']
2
Ты выбрал Заполненние данных для БС
Task:
Собрать в список данные, которые необходимо заполнить в шаблоне.
2g - Reg CELL SW BSC BCF LAC RAC
3g - Reg Имя сайта Sector_name LAC RAC URA RNC_ID
4g - Reg Имя сайта Sector_name TAC
# Разработка Список данных.
Decision:
PS C:\Windows\system32> cat .\2listdata.py
#1 перечислить список команд, которые может выполнить программа:
repeat="y"
with open("output.txt", "w") as outfile:
    outfile.write("") 
while repeat == "y":
    print("Выполните действия, которые необходимо выполнить в CES:")
    listcmd=['Заполненние данных для БС Nokia (1)', 'Заполненние данных для БС Ericsson (2)']
    print(listcmd)
    choicecmd = input()
    #print(choicecmd)
    if choicecmd == '1':
        #print("Ты выбрал Заполненние данных для БС Nokia")
        #with open("output.txt", "a") as outfile:
        #    outfile.write("Выполняю Заполненние данных для БС Nokia"+"\n")
        #2 Собрать в список данные, которые необходимо заполнить в шаблоне: 
        listtemplate=['Reg','CELL','SW','BSC','BCF','LAC','RAC2g','Имя сайта','Sector_name','RAC3g','URA','RNC_ID']
        print("Для заполнения нужны следующие данные: ", listtemplate)
        with open("output.txt", "a") as outfile:
            outfile.write("Для заполнения нужны следующие данные: "+listtemplate[0]+","+listtemplate[1]+","+listtemplate[2]+","+listtemplate[3]+","+listtemplate[4]+","+listtemplate[5]+","+listtemplate[6]+","+listtemplate[7]+","+listtemplate[8]+","+listtemplate[9]+","+listtemplate[10]+","+listtemplate[11]+"\n")
    elif choicecmd == '2':
        print("Ты выбрал Заполненние данных для БС Ericsson")
        with open("output.txt", "a") as outfile:
            outfile.write("Ты выбрал Заполненние данных для БС Ericsson"+"\n")
    else:
        print("Введите y/n")        
    repeat = input("Do you want to continue? (y/n): ")
    if repeat == "n":
        break
    else:
        print("Введите y/n")
PS C:\Windows\system32> python .\py.py
Выполните действия, которые необходимо выполнить в CES:
['Заполненние данных для БС Nokia (1)', 'Заполненние данных для БС Ericsson (2)']
1
Для заполнения нужны следующие данные:  ['Reg', 'CELL', 'SW', 'BSC', 'BCF', 'LAC', 'RAC2g', 'Имя сайта', 'Sector_name', 'RAC3g', 'URA', 'RNC_ID']
Do you want to continue? (y/n): n
Task:
Настроить библиотеку для работы с таблицами excel.
# Администрирование локальных, виртуальных и облачных серверов.
Decision:
PS C:\Windows\system32> pip install pandas --proxy http://t2rs-fgproxy.corp.tele2.ru:8080
root@kvmubuntu:~# python -m venv sortenv
root@kvmubuntu:~# source sortenv/Scripts/activate
root@kvmubuntu:~# touch requirements.txt
root@kvmubuntu:~# cat requirements.txt
pandas==2.2.3
openpyxl==3.1.5 
root@kvmubuntu:~# pip install -r requirements.txt
Task:
Найти незаполненные строки БС в таблице из CES.
# Разработка Поиск незаполненных данных в таблице.
Decision:

Source:
# https://stackoverflow.com/questions/57448042/regular-expressions-returning-partial-matches - Регулярные выражения, возвращающие частичные совпадения.
# https://www.w3schools.com/python/ref_string_split.asp - Python String split() Method.
# https://blog.skillfactory.ru/rabota-s-failami-python/ - Чтение файла.
# https://blog.skillfactory.ru/regulyarnye-vyrazheniya-v-python/ - Функции регулярных выражений в Python.
# https://sky.pro/media/zapis-stroki-s-peremennoj-v-tekstovyj-fajl-v-python/ - Запись строки с переменной в текстовый файл в Python.
# https://sky.pro/wiki/python/dobavlyaem-novuyu-stroku-pri-zapisi-v-fayl-python-file-write/ - Добавляем новую строку при записи в файл Python: file.write().
# https://pythonru.com/primery/kak-perevesti-tekst-na-novuju-stroku-v-python - Символ новой строки в print.
# https://timeweb.cloud/tutorials/python/kak-udalit-simvol-iz-stroki-python - Как удалить символы с помощью среза.
# https://www.w3schools.com/python/python_while_loops.asp - The break Statement.
# https://sky.pro/wiki/python/kak-dobavit-element-v-spisok-v-python/ - Использование метода append() для добавления элемента.
# https://pythonist.ru/kak-dobavit-element-v-slovar/ - Совет: добавление и обновление происходит одинаково.
# https://ru.stackoverflow.com/questions/1599918/%d0%9a%d0%b0%d0%ba-%d0%bc%d0%bd%d0%b5-%d0%b2-%d0%b3%d0%be%d1%82%d0%be%d0%b2%d1%8b%d0%b9-%d1%81%d0%bb%d0%be%d0%b2%d0%b0%d1%80%d1%8c-%d0%b4%d0%be%d0%b1%d0%b0%d0%b2%d0%b8%d1%82%d1%8c-%d0%ba%d0%bb%d1%8e%d1%87%d0%b8-%d0%b8-%d0%b7%d0%bd%d0%b0%d1%87%d0%b5%d0%bd%d0%b8%d1%8f-%d0%b8%d0%b7-%d0%b4%d0%b2%d1%83%d1%85-%d1%81%d0%bf%d0%b8%d1%81%d0%ba%d0%be%d0%b2/1599920#1599920 - Как мне в готовый словарь добавить ключи и значения из двух списков?
# https://stepik.org/lesson/265110/step/2?unit=246058 - Евклидово расстояние.
# https://habr.com/ru/articles/801885/ - Принцип работы KNN.
# https://sky.pro/media/poluchenie-indeksa-maksimalnogo-ili-minimalnogo-znacheniya-v-spiske-v-python/ - Использование встроенных функций max(), min() и index().
# https://stackoverflow.com/questions/27749553/how-can-i-read-the-contents-of-all-the-files-in-a-directory-with-pandas - How can I read the contents of all the files in a directory with pandas?