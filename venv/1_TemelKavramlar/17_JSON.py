#JSON:javascript object notation
'''
{} ->object/nesne
key -> property/özellik
value -> değer
[] ->array(list)
Python     JSON
list       array
str        string
int        number
float      number
True       true
None       null


'''
# Json object
# {'ad': 'Nur', 'cinsiyet': 'K', 'dogumTarihi': '1980', 'soyad': 'Öztürk'}

# list of json object
# [
#     {'ad': 'Nur', 'cinsiyet': 'K', 'dogumTarihi': '1980', 'soyad': 'Öztürk'},
#     {'ad': 'Ali', 'cinsiyet': 'E', 'dogumTarihi': '1965', 'soyad': 'Yılmaz'}
# ]
import json

dict_ogrenci = {
    'ad': 'Nur',
    'cinsiyet': 'K',
    'dogumTarihi': 1980,
    'soyad': 'Öztürk',
    'mezun_mu': True,
    'okullar': None
}
json_ogrenci = json.dumps(dict_ogrenci, ensure_ascii=False)
print(
    json_ogrenci)  # {"ad": "Nur", "cinsiyet": "K", "dogumTarihi": 1980, "soyad": "\u00d6zt\u00fcrk", "mezun_mu": true, "okullar": null}
# ensure_ascii = False iken karakter sorunu çözülür. {"ad": "Nur", "cinsiyet": "K", "dogumTarihi": 1980, "soyad": "Öztürk", "mezun_mu": true, "okullar": null}


# dict_ogr = json.load(open("ogrenci.json", encoding="utf8"))
# print(type(dict_ogr))  # <class 'dict'>
# print(
#     dict_ogr)  # {'ad': 'Nur', 'cinsiyet': 'K', 'dogumTarihi': 1980, 'soyad': 'Öztürk', 'mezun_mu': True, 'okullar': None}
# print(dict_ogr["ad"])

# www.mernis.gov.tr/tcknsorgula/12345678901  -> {"ad": "Nur"}


dict_ogrenci_list = [
    {'ad': 'Nur', 'cinsiyet': 'K', 'dogumTarihi': '1980', 'soyad': 'Öztürk'},
    {'ad': 'Ali', 'cinsiyet': 'E', 'dogumTarihi': '1965', 'soyad': 'Yılmaz'}
]
json.dump(dict_ogrenci_list, open("students.json", "a", encoding="utf8"), ensure_ascii=False)





