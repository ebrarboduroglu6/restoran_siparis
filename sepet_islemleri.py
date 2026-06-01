sepetim = []

def sepete_ekle(yemek_adi):
    sepetim.append(yemek_adi)
    
    print("-> " + yemek_adi + " sepete eklendi.")

def toplam_hesapla(menu_sozlugu):
    toplam = 0
    for urun in sepetim:
        if urun in menu_sozlugu:
            toplam += menu_sozlugu[urun]
    return toplam
