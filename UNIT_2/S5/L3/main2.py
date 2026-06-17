
scegli = input("Che figura geometrica selezioni? (inserisci ):")
if scegli == 'Quadrato':
    print("Quadrato")
    lato = int(input("Quanto misura il lato?"))
    result = lato*4
    print ("il perimetro è" )
    print(result)

elif scegli == "Cerchio":
    print("Cerchio")
    raggio = float(input("Quanto misura il raggio?"))
    result = 2*3.14*raggio
    print("la circonferenza è")
    print(result)

elif scegli =="Rettangolo":
    print("Rettangolo")
    base = int(input("Quanto misura la base?"))
    altezza = int(input("Quanto misura l'altezza?"))
    result = base*2+altezza*2
    print("il perimetro è")
    print(result)

    
else: 
    print("Errore")


