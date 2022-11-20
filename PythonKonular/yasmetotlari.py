def dogum_tarihi_hesapla(dogum_tarihi:str)->int:
  from datetime import datetime as dt
  dogum_tarihi_date=dt.strptime(dogum_tarihi,"%Y-%m-%d")
  simdiki_zaman = dt.now()
  fark=simdiki_zaman - dogum_tarihi_date
  return round(fark.days/365)


def emeklilik_yasi_hesapla(ad: str, cinsiyet: str, dogum_tarihi: str) -> str:
from datetime import datetime as dt
    emeklilik_yasi = 65
    if cinsiyet == "k":
        emeklilik_yasi = 58
    kisinin_yasi = yas_hesapla(dogum_tarihi)
    emeklilige_kalan_yil = emeklilik_yasi - kisinin_yasi
    sonuc = f"Sevgili {ad.capitalize()}, {dt.date.today().year} tarihi itibariyle emekliliğine {emeklilige_kalan_yil} yıl kaldı."
    return sonuc

