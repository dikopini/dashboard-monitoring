from bs4 import BeautifulSoup
import requests


def ekstraksi_data():
    """
    Tanggal: 05 Januari 2022
    Waktu: 10:11:10 WIB
    Magnitudo: 3.5
    Kedalaman: 10 km
    Lokasi: LS = 1.34 - BT = 120.48
    Pusat Gempa: Pusat gempa berada di darat 20 km barat daya Tambarana-Kab. Poso
    Dirasakan: Dirasakan (Skala MMI): II-III Poso
    :return:
    """

    try:
        content = requests.get('https://bmkg.go.id/')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span', {'class':'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')

        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text

            i = i+1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'LS': ls, 'BT': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan

        return hasil
    else:
        return None


def tampilkan_hasil(result):
    if result is None:
        print('Tidak dapat menenmukan data gempa terkini')
        return

    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat {result['koordinat']['LS']}, {result['koordinat']['BT']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")