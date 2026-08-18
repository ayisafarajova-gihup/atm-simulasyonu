menu=("\n ISLEM SECIN\n 1-bakiye gör \n 2-para yatir \n 3-para cek \n 4-cikiş")

class Atm:

    def __init__(self,ad,soyad,bakiye=0):
        self.ad = ad
        self.soyad =soyad
        self.bakiye =bakiye
    def bilgiler(self):
        return f" Ad:{self.ad},Soyad:{self.soyad},Bakiye:{self.bakiye}TL"
    def para_yatir(self,miktar):
        self.bakiye += miktar
        return f"Guncel bakiye: {self.bakiye} TL"
    def para_cek(self,miktar):
        if miktar > self.bakiye:
            print("yetersiz bakiye")
        else:
            self.bakiye -= miktar
            print("islem basarili")
            print(f"Guncel bakiye: {self.bakiye} TL")
kullanici = Atm("Ayisa", "Farajova", 1000)
while True:
    print(menu)
    secim =int(input( "seciminiz ?"))
    if secim == 1:
        print(kullanici.bilgiler())
    elif secim == 2:
        miktar =float(input("yatirilacak  para miktarı:"))
        print(kullanici.para_yatir(miktar))
    elif secim == 3:
        miktar = float(input("çekilecek para miktarı:"))
        print(kullanici.para_cek(miktar))
    elif secim == 4:
        print("program kapatıliyor ......")
        break




                  

