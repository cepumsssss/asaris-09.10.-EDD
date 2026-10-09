# 04_summa_lidz_n.py

ievade = input("Ievadi pozitīvu veselu skaitli n: ")

if ievade == "":
    print("Kļūda! Ievade ir tukša.")
else:
    try:
        n = int(ievade)

        if n <= 0:
            print("Kļūda! Skaitlim jābūt pozitīvam.")
        else:
            summa = 0

            for i in range(1, n + 1):
                summa = summa + i

            print("Summa ir:", summa)

    except ValueError:
        print("Kļūda! Jāievada vesels skaitlis.")