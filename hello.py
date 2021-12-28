# Muhammed Ali Çalkılıç
sozlesme_sayisi = 10000

def teminat(sozlesme_buyuklugu, baslangic_tutari, fiyat, islem_tipi, gun_sonu_uzlasma_fiyati):
    if baslangic_tutari < 130:
        print("Başlangıc tutarı 130TRY'den büyük olmalıdır")
        exit(1)

    
    islem_tutari = sozlesme_sayisi * sozlesme_buyuklugu
    toplam_baslangic_teminati = sozlesme_sayisi * baslangic_tutari
    kaldirac_orani = ((islem_tutari*fiyat)/toplam_baslangic_teminati)
    toplam_surdurme_teminati = toplam_baslangic_teminati * 0.75
    gun = 0
    kar_zarar = []
    gun_sonu_teminat_bakiyesi = []
    teminat_cagri = False
    fiyat_listesi = []
    fiyat_listesi.append(fiyat)
    while(gun < len(gun_sonu_uzlasma_fiyati)):
        fiyat_listesi.append(gun_sonu_uzlasma_fiyati[gun])
        if islem_tipi==1:
            #Long
            kaldiracli_teminat = toplam_baslangic_teminati + toplam_baslangic_teminati*kaldirac_orani
            toplam_usd_kaldiracli = kaldiracli_teminat / fiyat_listesi[gun]
            bozdurma = (toplam_usd_kaldiracli * gun_sonu_uzlasma_fiyati[gun])
            bakiye = toplam_baslangic_teminati + bozdurma - kaldiracli_teminat
            gun_sonu_teminat_bakiyesi.append(bakiye)
        
        elif islem_tipi==0:
            #short
            kaldiracli_teminat = toplam_baslangic_teminati + toplam_baslangic_teminati*kaldirac_orani
            toplam_usd_kaldiracli = kaldiracli_teminat /  gun_sonu_uzlasma_fiyati[gun]
            bozdurma = (toplam_usd_kaldiracli * fiyat_listesi[gun])
            bakiye = toplam_baslangic_teminati + bozdurma - kaldiracli_teminat
            gun_sonu_teminat_bakiyesi.append(bakiye)
        
        else:
            print("Yanlış İşlem Tipi!")
            exit(1)
            
        
        kar_zarar.append(bakiye - toplam_baslangic_teminati)

        
        #bir sonraki gün artık şuanki bakiyemiz
        toplam_baslangic_teminati = bakiye

        
        kaldirac_orani = (islem_tutari*gun_sonu_uzlasma_fiyati[gun])/toplam_baslangic_teminati
        toplam_surdurme_teminati = toplam_baslangic_teminati * 0.75

        if (toplam_baslangic_teminati - toplam_surdurme_teminati) < 0:
            teminat_cagri = True
        else:
            teminat_cagri = False

        gun +=1
    
    return islem_tutari, toplam_baslangic_teminati, kaldirac_orani, toplam_surdurme_teminati,teminat_cagri,kar_zarar







gun_sonu_test = [3.7610,3.7470,3.8359,3.7700]

# long = 1
# short = 0
long_short = 1

islem_tutari, toplam_baslangic_teminati, kaldirac_orani, toplam_surdurme_teminati,teminat_cagri,kar_zarar = teminat(1000,129,3.7565,long_short,gun_sonu_test)

print("İşlem Tutarı: {}\nToplam Başlangıc Teminatı: {}\nKaldıraç Oranı: {}\nToplam sürdürme Teminati: {}\nTeminat Çağrısı: {}".format(islem_tutari, toplam_baslangic_teminati, kaldirac_orani, toplam_surdurme_teminati,teminat_cagri))
print("K/Z: {}".format(kar_zarar))


    