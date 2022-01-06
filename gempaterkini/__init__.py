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
    hasil = dict()
    hasil['tanggal'] = '05 Januari 2022'
    hasil['waktu'] = '10:11:10 WIB'
    hasil['magnitudo'] = 3.5
    hasil['lokasi'] = {'LS': 1.34, 'BT': 120.48}
    hasil['pusat gempa'] = 'Pusat gempa berada di darat 20 km barat daya Tambarana-Kab. Poso'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Poso'

    return hasil


def tampilkan_hasil(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS = {result['lokasi']['LS']}, BT = {result['lokasi']['BT']}")
    print(f"Pusat Gempa {result['pusat gempa']}")
    print(f"Dirasakan {result['dirasakan']}")

#if __name__ == '__main__':
#    print('ini adalah package gempaterkini')