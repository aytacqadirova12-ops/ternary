tecrube = int(input("Namizədin təcrübə illərini daxil edin: "))
bal = int(input("Balını daxil edin (0-100): "))

if 0 <= bal <= 100 and tecrube >= 0:
    result = "kecdi" if (tecrube >= 2 and bal >= 70) or (bal >= 90) else "kecmedi"
    if bal >= 90:
        print("Güclü namizəd")
    elif tecrube >= 2 and bal >= 70:
        print("Növbəti mərhələyə dəvət olunur.")
    else:
        print("Namizəd uyğun deyil")
else:
    print("Xəta: Düzgün bal və təcrübə ili daxil edin.")