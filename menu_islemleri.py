restoran_menusu = {
    "Kebap": 250,
    "Lahmacun": 80,
    "Ayran": 30,
    "Künefe": 120
}

def menuyu_goster():
    print("\n--- RESTORAN MENÜSÜ ---")
    for yemek, fiyat in restoran_menusu.items():
        
        print(yemek, ":", fiyat, "TL")
    print("-----------------------")
