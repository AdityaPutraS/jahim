from flask import *
from app import app,db
from app.models import *
from app.forms import LoginForm,RegisterForm
from sqlalchemy import desc

@app.route('/')
def index():
    return render_template('main.html',judul = 'Main')
@app.route('/main')
def main():
    return render_template('main.html',judul = 'Main')
@app.route('/recent')
def recent():
    #cari 5 item terakhir
    latest = Inventori.query.order_by(desc(Inventori.id)).limit(5).all()
    #return data json ke 5 item tersebut, latest berisi seperti berikut
    #latest = [<Inventori 5>,<Inventori 4>,<Inventori 3>,<Inventori 2>,<Inventori 1>]
    namaBarang, jumlah, harga, namaHimp = [], [], [], []
    for barang in latest:
        namaBarang.append(barang.namabarang)
        jumlah.append(barang.jumlahbarang)
        harga.append(barang.harga)
        namaHimp.append(User.query.get(barang.idHimpunan).displayname)
    recentJson = jsonify({'namaBarang' : namaBarang, 'jumlah' : jumlah, 'harga' : harga, 'namaHimp' : namaHimp})
    #return recentJson ke front end untuk diolah
    return recentJson
@app.route('/search', methods=['POST'])
def search():
    data = request.data
    tipe = data['tipe']
    if(tipe=='Barang'):
        #cari Barang
        namabarang = data['cari']
        cekBarang = Inventori.query.filter_by(namabarang=namabarang).first()
        if(cekBarang is None):
            #barang tidak ditemukan
            pass
        else:
            #barang ketemu, return sama data himpunannya juga
            akunHimpunan = User.query.get(cekBarang.idHimpunan)
            namaHimpunan = akunHimpunan.displayname
            harga = cekBarang.harga
            jumlah = cekBarang.jumlahbarang
            pass
    elif(tipe=='Username'):
        #cari user
        namaHimpunan = data['cari']
        akunHimpunan = User.query.filter_by(displayname=namaHimpunan)
        if(akunHimpunan is None):
            #akun tidak ditemukan
            pass
        else:
            #ketemu, langsung return id himpunannya
            #niatnya, ngereturn dict {'id' : idnya}, terus front end ngasih link http://linkaplikasi/user/idnya, biar di redrect ke halaman usernya
            idHimpunan = akunHimpunan.id
            pass
    else:
        #tipe tidak valid, return error
        pass
@app.route('/login', methods=['POST'])
def login():
    data = request.data
    username = data['username']
    password = data['password']
    #cari di db
    akun = db.query.filter_by(username=username).first()
    if(akun is None):
        #return error user not found
        pass
    else:
        #cek apakah password bener
        if(akun.password_hash):
            #sukses, return sukses
            pass
        else:
            #return pass salah
            pass
    return 200
@app.route('/register',methods=['POST'])
def register():
    data = request.data
    username = data['username']
    displayname = data['displayname']
    password = data['password']
    #cari di db apakah usernamenya sudah ada
    cekUsername = User.query.filter_by(username=username).first()
    cekDisplay = User.query.filter_by(displayname=displayname).first()
    if(cekAkun is None):
        #cek apakah displayname sudah dipakai
        if(cekDisplay is None):
            #aman, tambah ke database
            akunBaru = User(username=username,displayname=displayname,password_hash=password) #TODO:encrypt password
            db.session.add(akunBaru)
            db.session.commit()
        else:
            #return displayname udah ada
            pass
    else:
        #return username sudah ada
        pass
    return 200
