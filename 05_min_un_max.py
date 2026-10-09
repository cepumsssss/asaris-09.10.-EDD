# 05_min_un_max.py

skaits = int(input("Cik skaitļus ievadīsi? "))

if skaits <= 0:
    print("Kļūda! Skaitļu skaitam jābūt lielākam par 0.")
else:
    pirmais = int(input("Ievadi 1. skaitli: "))
    mazākais = pirmais
    lielākais = pirmais

    for i in range(2, skaits + 1):
        skaitlis = int(input("Ievadi " + str(i) + ". skaitli: "))

        if skaitlis < mazākais:
            mazākais = skaitlis

        if skaitlis > lielākais:
            lielākais = skaitlis

    print("Mazākais skaitlis:", mazākais)
    print("Lielākais skaitlis:", lielākais)