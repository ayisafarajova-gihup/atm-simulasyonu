import random

kelime_listesi=["kedi", "köpek", "kuş", "aslan", "kaplan", "fil", "zürafa", "tavşan", "maymun", "ayı", "kurt", "tilki", "geyik", "at", "inek", "koyun", "keçi", "eşek", "tavuk", "ördek", "kaz", "hindi", "karga", "kartal", "baykuş", "penguen", "yunus", "balina", "köpekbalığı", "ahtapot", "yengeç", "kaplumbağa", "yılan", "timsah", "kertenkele", "kurbağa", "kelebek", "arı", "karınca", "sinek", "örümcek", "akrep", "sincap", "kirpi", "kanguru", "koala", "panda", "deve", "zebra", "suaygırı"]
kelime=random.choice(kelime_listesi)
                 
tahminler = []  # Doğru tahmin edilen harfleri burada tutacağız
can = 5  # Yanlış tahmin hakkı

print("--- KELIMEYI BUL (ADAM ASMACA) ---,\n (hayvan adlari)")

while True:
  print()
  # 1. Ekrana kelimenin son durumunu çizdirme
  bilinen_harf_sayisi = 0
  for harf in kelime:
    if harf in tahminler:
      print(harf, end=" ")
      bilinen_harf_sayisi += 1
    else:
      print("_", end=" ")

  print(f"   (Kalan Can: {can})")

  # Kazanma kontrolü (Tüm harfler açıldı mı?)
  if bilinen_harf_sayisi == len(kelime):
    print("\nTebrikler, kelimenin tamamını bildiniz! Kazandınız! 🎉")
    break

  # 2. Kullanıcıdan tahmin alma
  tahmin = input("\nBir harf tahmin edin: ").lower()

  # Aynı harfi tekrar denediyse uyarı ver
  if tahmin in tahminler:
    print(f"'{tahmin}' harfini zaten daha önce tahmin etmiştiniz.")
    continue

  # 3. Tahmin kontrolü
  if tahmin in kelime:
    print(f"Harika! '{tahmin}' harfi kelimede var.")
    tahminler.append(tahmin)  # Doğru harfi listeye ekle
  else:
    print(f"Üzgünüm, '{tahmin}' harfi kelimede yok.")
    can -= 1  # Hakkını azalt

  # Kaybetme kontrolü (Can bitti mi?)
  if can == 0:
    print(f"\nCanınız bitti! Kaybettiniz. Aranan kelime: {kelime} 😢")
    break