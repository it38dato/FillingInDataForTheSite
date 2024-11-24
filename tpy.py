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
        datasite = dict()
        datasites = dict()
        print("Добавьте файлы форматов kml в папку, где находится программа для дальнейшей обработки данных.")
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
        #7 Создать словарь и собрать данные: key - ИМЯ БС, value - Координаты, TAC, BSC:
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
    else:
        print("Введите y/n")