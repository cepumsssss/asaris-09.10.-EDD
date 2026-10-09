
# 01_vecuma_grupa.py

vecums = input("Ievadi savu vecumu: ")

if vecums == "":
    print("Kļūda: nav ievadīts vecums!")
else:
    vecums = int(vecums)

    if vecums < 0:
        print("Kļūda: vecums nevar būt negatīvs!")
    elif vecums <= 12:
        print("Bērns")
    elif vecums <= 17:
        print("Pusaudzis")
    elif vecums <= 64:
        print("Pieaugušais")
    else:
        print("Seniors")


