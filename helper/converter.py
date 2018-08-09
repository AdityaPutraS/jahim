import datetime

def encodeTanggal(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day
def decodeTanggal(tanggal):
    tahun = int(tanggal /10000)
    bulan = int((tanggal % 10000)/100)
    hari = int(tanggal % 100)
    return datetime.date(tahun,bulan,hari)
