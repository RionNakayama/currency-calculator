#test1.csv

import csv
my_str = """ACME(tm) US DOLLAR EXCHANGE RATE APP
1) LOAD currency exchange rate data from a file
2) USE AVERAGE exchange rate
3) USE HIGHEST exchange rate
4) USE LOWEST exchange rate
5) CONVERT USD TO EUR
6) CONVERT USD TO AUD
7) CONVERT USD TO GBP
0) QUIT program"""

EUR_list = []
AUD_list = []
GBP_list = []
EUR = 0
AUD = 0
GBP = 0

def Average(list):
    return sum(list) / len(list)

def feature_1():
    file_name = input("Give name of the data file: ")
    file = open(file_name)
    csvreader = csv.reader(file, delimiter=";")
    header = []
    header = next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()

    print("Data loaded successfully!")

    min_date = rows[0][0]
    max_date = rows[-1][0]
    row_count = str(len(rows))
    print("Currency exchange data is from " + row_count + " days between " + min_date + " and " + max_date + ".\n")

    list1 = [i[1] for i in rows]
    list1 = list(filter(None, list1))
    list1 = [float(x) for x in list1]

    list2 = [i[2] for i in rows]
    list2 = list(filter(None, list2))
    list2 = [float(x) for x in list2]

    list3 = [i[3] for i in rows]
    list3 = list(filter(None, list3))
    list3 = [float(x) for x in list3]

    c1 = Average(list1)
    c2 = Average(list2)
    c3 = Average(list3)

    return list1,list2,list3,c1,c2,c3

def feature_2(list1,list2,list3):
    c1 = Average(list1)
    c2 = Average(list2)
    c3 = Average(list3)
    print("Using the average currency exchange rate.\n")
    return c1,c2,c3

def feature_3(list1,list2,list3):
    c1 = max(list1)
    c2 = max(list2)
    c3 = max(list3)
    print("Using the highest currency exchange rate.\n")
    return c1,c2,c3

def feature_4(list1,list2,list3):
    c1 = min(list1)
    c2 = min(list2)
    c3 = min(list3)
    print("Using the lowest currency exchange rate.\n")
    return c1,c2,c3

def feature_5(current):
    USD_CON = int(input("Give USD to convert: "))
    result = (USD_CON) * current
    print(float(USD_CON), "USD in EUR is", round(result, 2), "EUR\n")

def feature_6(current):
    USD_CON = int(input("Give USD to convert: "))
    result = (USD_CON) * current
    print(float(USD_CON), "USD in AUD is", round(result, 2), "AUD\n")

def feature_7(current):
    USD_CON = int(input("Give USD to convert: "))
    result = (USD_CON) * current
    print(float(USD_CON), "USD in GBP is", round(result, 2), "GBP\n")

while True:
  print(my_str)
  action = int(input("Choose what to do: "))

  if action == 0:
      break

  elif action == 1:
      EUR_list,AUD_list,GBP_list,EUR,AUD,GBP = feature_1()

  elif action == 2:
      EUR,AUD,GBP = feature_2(EUR_list,AUD_list,GBP_list)

  elif action == 3:
      EUR,AUD,GBP = feature_3(EUR_list,AUD_list,GBP_list)

  elif action == 4:
      EUR,AUD,GBP = feature_4(EUR_list,AUD_list,GBP_list)

  elif action == 5:
      feature_5(EUR)

  elif action == 6:
      feature_6(AUD)

  elif action == 7:
      feature_7(GBP)
