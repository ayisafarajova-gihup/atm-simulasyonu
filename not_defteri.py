menu=("\n***MENU***\n 1-not ekle \n 2-notlari oku \n 3-cikis ")
while True:
    try:
        secim =int(input("seciminiz nedir ?"))
        if secim== 1:
                not_icerigi=input("notunuzu girin:")
                with open("not_dosyasi","a",encoding="utf8") as dosya :
                    dosya.write(not_icerigi +"\n")
                    print("notunuz kayedildi")
        elif secim== 2:
            with open("not_dosyasi","r",encoding="utf") as dosya :
                    dosya.read()
        elif secim== 3:
            print("cikis yapiliyor....")
            break
        else:
            print("gecersiz secim")
    except ValueError:
        print("lutfen sayi girin:")

                
          