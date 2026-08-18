import random

bilgisayar_skoru = 0
kulanici_skoru = 0

def secim_ugret():  
    bilgisayar_secimi = random.randint(1,3)
    if bilgisayar_secimi == 1:
        return "tas"
    elif bilgisayar_secimi == 2:
        return "kagit"
    else:
        return "makas"

while True:
    kulanici_secimi = input("tas? kagit? makas? ").lower()
    
    # Geçersiz bir şey yazılırsa turu baştan başlatır
    if kulanici_secimi not in ["tas", "kagit", "makas"]:
        print("Lütfen sadece tas, kagit veya makas yazın!")
        continue 
        
    bilgisayar_secimi = secim_ugret()
    print("Bilgisayarın seçimi:", bilgisayar_secimi) # Bilgisayarın ne seçtiğini görmek iyi olur
    
    if bilgisayar_secimi == kulanici_secimi:
        print("berabere")
    elif bilgisayar_secimi == "tas" and kulanici_secimi == "kagit":
        kulanici_skoru += 1
        print("bu turu siz kazandiniz")
        print(kulanici_skoru, "VS", bilgisayar_skoru)
    elif bilgisayar_secimi == "kagit" and kulanici_secimi == "makas":
        kulanici_skoru += 1
        print("bu turu siz kazandiniz")
        print(kulanici_skoru, "VS", bilgisayar_skoru)
    elif bilgisayar_secimi == "makas" and kulanici_secimi == "tas":
        kulanici_skoru += 1
        print("bu turu siz kazandiniz")
        print(kulanici_skoru, "VS", bilgisayar_skoru)
    else:
        bilgisayar_skoru += 1
        print("bu turu bilgisayar kazandi")
        print(kulanici_skoru, "VS", bilgisayar_skoru)
        
    # BİTİŞ KOŞULU DÜZELTİLDİ:
    if kulanici_skoru == 3 or bilgisayar_skoru == 3:
        print("Oyun Bitti! Sonuç:")
        print(kulanici_skoru, "VS", bilgisayar_skoru)
        break