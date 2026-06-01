import menu_islemleri
import sepet_islemleri

while True:
    print("\n1. Menüyü Gör")
    print("2. Sepete Ürün Ekle")
    print("3. Sepeti ve Toplam Tutarı Gör")
    print("4. Çıkış")
    
    secim = input("Yapmak istediğiniz işlemi seçin (1-4): ")
    
    if secim == "1":
        menu_islemleri.menuyu_goster()
        
    elif secim == "2":
        urun = input("Eklenecek ürünün adını yazın: ")
        if urun in menu_islemleri.restoran_menusu:
            sepet_islemleri.sepete_ekle(urun)
        else:
            print("Maalesef bu ürün menümüzde yok.")
            
    elif secim == "3":
        
        print("\nSepetinizdeki Ürünler:", sepet_islemleri.sepetim)
        toplam = sepet_islemleri.toplam_hesapla(menu_islemleri.restoran_menusu)
        print("Toplam Ödenecek Tutar:", toplam, "TL")
        
    elif secim == "4":
        print("Bizi tercih ettiğiniz için teşekkürler, iyi günler!")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin."
