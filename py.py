import pandas as pd
import os
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
        #print("Выполняю Заполненние данных для БС Nokia")
        #with open("output.txt", "a") as outfile:
        #    outfile.write("Выполняю Заполненние данных для БС Nokia"+"\n")
        #2 Собрать в список данные, которые необходимо заполнить в шаблоне: 
        listtemplate=["Reg","CELL","SW",'BSC','BCF','LAC','RAC2g','Имя сайта','Sector_name','RAC3g','URA','RNC_ID']
        print("Для заполнения нужны следующие данные: ", listtemplate)
        #with open("output.txt", "a") as outfile:
        #    outfile.write("Для заполнения нужны следующие данные: "+listtemplate[0]+","+listtemplate[1]+","+listtemplate[2]+","+listtemplate[3]+","+listtemplate[4]+","+listtemplate[5]+","+listtemplate[6]+","+listtemplate[7]+","+listtemplate[8]+","+listtemplate[9]+","+listtemplate[10]+","+listtemplate[11]+"\n")
        #3 Найти незаполненные строки БС IR2468 в таблице из CES для каждых технологий - 2g, 3g, 4g:
        print("ВНИМАНИЕ! Выгрузите таблицу с незаполненными данными из CES и поместите файл в папку unloading!")    
        '''cols = [2, 6, 8]
        table = pd.read_excel("Nokia2g Table integrated sitesIR2468.xlsx", usecols=cols)
        #print(table)
        table = table[table["BSS"].isna()]
        print(table)'''


        path = "unloading/"
        #files = [file for file in os.listdir(path) if not file.startswith('.')]
        listfiles = os.listdir(path)
        print(listfiles)             
        tables = pd.DataFrame()
        for file in listfiles:
            print(file)
            cols = [2, 6, 8, 10]
            table = pd.read_excel(path+"/"+file, usecols=cols)
            tables = pd.concat([tables,table])
            tables = tables[tables["BSS"].isna()]
        print(tables)





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