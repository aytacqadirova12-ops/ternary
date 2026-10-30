mebleg = float(input("sifarişin məbləğini daxil edin:")) 

if mebleg >=200: 
    endirim = mebleg *0.8 
elif 100<= mebleg <=199.9: 
    endirim = mebleg *0.9 
else: 
    endirim = 0.0 

result="endirim qazandiniz" if endirim>0 else "endirim yoxdur" 
print(result,endirim)