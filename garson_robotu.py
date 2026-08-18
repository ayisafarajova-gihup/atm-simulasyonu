print("🤖🤖🤖YAPAY LOKANTA🤖🤖🤖")

menu = [
    {"id": 1, "ad": "Atom Burger", "fiyat": 100},
    {"id": 2, "ad": "Siber Tavuk", "fiyat": 200},
    {"id": 3, "ad": "Hizli Durum", "fiyat": 300},
    {"id": 4, "ad": "Nano Patates", "fiyat": 400},
    {"id": 5, "ad": "Robot Corbasi", "fiyat": 120},
    {"id": 6, "ad": "Piksel Pizza", "fiyat": 107},
    {"id": 7, "ad": "Neon Salata", "fiyat": 130},
    {"id": 8, "ad": "Soguk Limonata", "fiyat": 190},
    {"id": 9, "ad": "Enerji Icecegi", "fiyat": 160},
    {"id": 10, "ad": "Cip Tatlisi", "fiyat": 800},
]

pb = "Galaksiya"

ad = input("Hoş geldiniz, isminiz nedir?\n")
print("Merhaba " + ad + ", lokantamıza hoş geldin!\n")

print("--- MENÜ ---")
for mn in menu:
    print(f"{mn['id']}. {mn['ad']} - {mn['fiyat']} {pb}")

# Kullanıcıdan seçimi alıp tam sayıya (int) çeviriyoruz


secim = int(input("\nSeçiminiz nedir? (Ürün numarasını girin):\n"))
    

# Menüde bu ID'ye sahip ürün var mı kontrol edelim
secilen_yemek = None
for mn in menu:
    if mn["id"] == secim:
        secilen_yemek = mn
        break

if secilen_yemek:
    print(f"Hımmm harika seçim, {secilen_yemek['ad']} seçtiniz!")
    
    # Adet bilgisini kullanıcıdan sayı olarak alıyoruz
    adet = int(input("Kaç adet istersiniz?:\n"))
    
    # Toplam fiyatı hesaplıyoruz
    toplam_fiyat = adet * secilen_yemek["fiyat"]
    
    print("\n--- SİPARİŞ ÖZETİ ---")
    print(f"İşte siparişiniz: {adet} adet {secilen_yemek['ad']}")
    print(f"Ödenecek Toplam Tutar: {toplam_fiyat} {pb}")
else:
    print("Menüde böyle bir seçenek yok.")