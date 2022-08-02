from datetime import date as d

teraz = d.today()

#print("dzien",teraz.strftime("%d"))
#print("miesiac",teraz.strftime("%m"))
#print("rok",teraz.strftime("%Y"))
print("Policze ile minęło dni od twoich urodzin")
print("Podaj date swoich urodzin")
dzienUrodzin = int(input("podaj dzien (liczbowo) "))
miesiacUrodzin = int(input("podaj miesiac (liczbowo) "))
rokUrodzin = input(("podaj miesiac rok "))

#dni miesiaca w roku zwyklymm
dniZw=[31,28,31,30,31,30,31,31,30,31,30,31]
#dni miesiaca w roku przestepnym
dniP=[31,29,31,30,31,30,31,31,30,31,30,31]
data_check=True
rokPrzestepny=False

if((int(rokUrodzin)%4 == 0 and int(rokUrodzin)%100!=0 )) or (int(rokUrodzin)%400 == 0):
    #rok przystępny
    rokPrzestepny=True
    if not(0<miesiacUrodzin<=12):
        #print("data nieprawidlowa (miesiac)")
        data_check=False
    elif not(0<dzienUrodzin<=dniP[miesiacUrodzin-1]):
            #print("data nieprawidlowa(dzien)")
            data_check = False
else:
    #zwykly rok
    if not(0<miesiacUrodzin<=12):
        #print("data nieprawidlowa (miesiac)")
        data_check = False
    elif not(0<dzienUrodzin<=dniZw[miesiacUrodzin-1]):
            #print("data nieprawidlowa(dzien)")
            data_check = False

lataOdUrodzin=int(teraz.strftime("%Y"))-int(rokUrodzin)
if(data_check==False):
    print("Podana data jest nieprawidlowa")
else:
    #liczenie lat przestepnych od urodzin
    ileLatPrzestepnych=0
    for i in range(0,lataOdUrodzin):
        #print(int(rokUrodzin)+i)
        if (((int(rokUrodzin)+i) % 4 == 0 and (int(rokUrodzin)+i) % 100 != 0)) or ((int(rokUrodzin)+i) % 400 == 0):
            ileLatPrzestepnych+=1

    #przeliczanie lat na dni
    #bez roku urodzin i roku bieżącego
    lataNaDni=0;
    if((rokPrzestepny == True) and (miesiacUrodzin>2)):
        lataNaDni=(lataOdUrodzin-1)*365+ileLatPrzestepnych-1
    else:
        lataNaDni=(lataOdUrodzin-1)*365+ileLatPrzestepnych

    #policzenie dni od dnia urodzin do konca roku
    dniOdUrodzin=0
    dniDoUrodzin=0
    pomoc=0
    while(pomoc<int(miesiacUrodzin-1)):
        if(rokPrzestepny==True):
            dniDoUrodzin+=dniP[pomoc]
        else:
            dniDoUrodzin+=dniZw[pomoc]
        pomoc+=1

    dniDoUrodzin+=int(dzienUrodzin)-1
    if(rokPrzestepny==True):
        dniOdUrodzin=366-dniDoUrodzin
    else:
        dniOdUrodzin = 365 - dniDoUrodzin

    #Czy bieżący rok jest przystępny?
    biezacyRokP=False
    if(int(teraz.strftime("%Y"))%4 == 0 and int(teraz.strftime("%Y")) or (int(teraz.strftime("%Y"))%400 == 0)):
        #rok przystępny
        biezacyRokP=True

    #dni od poczatku roku do teraz
    dniOdPoczatku=0
    pomoc=0
    while(pomoc<(int(teraz.strftime("%m"))-1)):
        if(biezacyRokP==True):
            dniOdPoczatku+=dniP[pomoc]
        else:
            dniOdPoczatku+=dniZw[pomoc]
        pomoc+=1
    dniOdPoczatku+=int(teraz.strftime("%d"))-1

    ileDni=lataNaDni+dniOdUrodzin+dniOdPoczatku

    #print(data_check)
    #print("Dni od poczatku roku do urodzin ",dniDoUrodzin)
    #print("Dni od poczatku roku do dzisiaj ",dniOdPoczatku)
    #print("ilosc lat przestepnych od roku urodzin do biezacego roku ",ileLatPrzestepnych)
    #print("ile lat od urodzin do teraz ",lataOdUrodzin)
    #print("lata na dni ", lataNaDni)
    if (ileDni<0):
        print("Podana data jeszcze nie wystapila")
    else:
        print("Od twoich urodzin do dzisiaj minelo ",ileDni," dni")



