class Atm:
    def __init__(self, ad, bakiye=0):
        self.ad = ad
        self.bakiye = bakiye
        
    def para_ekle(self, miktar):
        self.bakiye += miktar
        return f"Bakiyeye {miktar} TL ekleme yapıldı. Güncel bakiye: {self.bakiye} TL"
        
    def para_cek(self, miktar):
        if miktar > self.bakiye:
            return f"Yetersiz bakiye! Mevcut bakiye: {self.bakiye} TL"
        
        self.bakiye -= miktar
        return f"İşlem başarılı. Yeni bakiye: {self.bakiye} TL"
        
    def bilgileri_goster(self):
        return f"AD: {self.ad} | BAKİYE: {self.bakiye} TL"

# Kullanıcı oluşturma
kullanici1 = Atm("Ayisa", 4000)

print(f"Hoş geldiniz, {kullanici1.ad}!")

while True:
    try:
        islem = int(input("\n0- Çıkış\n1- Para Ekle\n2- Para Çek\n3- Bilgileri Göster\nİşlem seçiniz: "))
        
        if islem == 0:
            print("Sistemden çıkılıyor. İyi günler dileriz!")
            break
            
        elif islem == 1:
            miktar = float(input("Yatırılacak miktar (TL): "))
            print(kullanici1.para_ekle(miktar))
            
        elif islem == 2:
            miktar = float(input("Çekilecek miktar (TL): "))
            print(kullanici1.para_cek(miktar))
            
        elif islem == 3:
            print(kullanici1.bilgileri_goster())
            
        else:
            print("Geçersiz seçim! Lütfen menüdeki numaralardan birini girin.")
            
    except ValueError:
        print("Lütfen sadece sayı giriniz!")