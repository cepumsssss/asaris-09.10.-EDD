skaitlis = int(input("Ievadi veselu skaitli: "))

if skaitlis > 0:
    for i in range(1, 11):
        print(skaitlis, "x", i, "=", skaitlis * i)
elif skaitlis == 0:
    print("Skaitlim jābūt lielākam par 0!")
else:
    print("Skaitlis nedrīkst būt negatīvs!")