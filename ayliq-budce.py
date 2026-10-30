gelir = float(input("Aylıq gəlirinizi daxil edin: "))
xerc = float(input("Ümumi xərclərinizi daxil edin: "))

if gelir < 0 or xerc < 0:
    print("Xəta: Gəlir və xərclər mənfi ola bilməz.")
elif gelir == 0:
    if xerc > 0:
        print("Büdcə kəsiri var")
    else:
        print("Gəlir və xərc 0-dır, qənaət yoxdur.")
else:
    qalan_pul = gelir - xerc
    qanaet_faizi = (qalan_pul / gelir) * 100

    if xerc > gelir:
        print("Büdcə kəsiri var")
    elif xerc >= gelir * 0.8:
        print("Xərclərə diqqət et")
    elif xerc >= gelir * 0.5:
        print("Büdcə normaldır")
    else:
        print("Yaxşı qənaət edirsiniz")

    print(f"Qalan pul: {qalan_pul} AZN")
    print(f"Qənaət faizi: {qanaet_faizi}%")