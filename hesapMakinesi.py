# ilk hesap makinem
def toplama(a,b):
    return a + b

def cikarma(a,b):
    return a - b

def carpma(a,b):
    return a * b
def bolme(a,b):
    return a / b

sec =("""
        IŞLEM SEÇİN
    1-toplama
    2-cıkarma
    3-carpma
    4-bölme
    0-cikis

""")
print(sec)
while True:
    try:
        sec=input("seciminiz:")
        if sec =="0":
            print("Çıkış iyi günler")
            break
        if sec not in( "1","2","3","4"):
            print("yalnış seçim")
            continue
        sayi_1=float(input("1.sayı girin:"))
        sayi_2=float(input("2.sayı girin:"))
        if sec=="1":
            print(f"sonuc:{toplama(sayi_1,sayi_2)}")
        elif sec=="2":
            print(f"sonuc:{cikarma(sayi_1,sayi_2)}")
        elif sec=="3":
             
             print(f"sonuc:{carpma(sayi_1,sayi_2)}")
        elif sec=="4":
            print(f"sonuc:{bolme(sayi_1,sayi_2)}")
    except ValueError:
         print("Lütfen sayı girin")
    except ZeroDivisionError:
         print("0-a bölme hatası")
    print("-" * 25)

   
   
   
    