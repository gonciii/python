def turkce_karakterleri_cevir(metin: str):
    metin = metin.replace("ö", "o").replace("ü", "u").replace("ç", "c").replace("ğ", "g").replace("ş", "s").replace("ı",
                                                                                                                    "i")
    return metin


def mail_olustur(ad: str, soyad: str, uzanti: str):
    # ad = turkce_karakterleri_cevir(ad)
    # soyad = turkce_karakterleri_cevir(soyad)
    mail = turkce_karakterleri_cevir(f"{ad}.{soyad}@{uzanti}".lower().replace(' ', ""))
    return mail

