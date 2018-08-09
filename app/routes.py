from flask import *
from app import app,db
from app.models import *
from app.forms import LoginForm,RegisterForm
from sqlalchemy import desc

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('home.html')
@app.route('/profile/<namaHimp>',methods=['GET','POST'])
def profile(namaHimp):
    akunHimpunan = User.query.filter_by(displayName=namaHimp).first()
    if(akunHimpunan is None):
        #return tidak ketemu
        return 404
    else:
        #ketemu
        listBarang,listPinjam = [],[]
        akunBarang = Inventori.query.filter_by(namaHimpunan=namaHimp).first()
        akunPinjam = Pinjam.query.filter_by(namaPeminjam=namaHimp).first()
        #cek apakah dia punya barang untuk dipinjam
        if(akunBarang is None):
            pass #skip
        else:
            #tambahkan ke listBarang
            for barang in akunBarang.query.all():
                data = {'namaBarang':barang.namaBarang,'jumlahBarang':barang.jumlahBarang}
                listBarang.append(data)
        #cek apakh dia ada minjem barang
        if(akunPinjam is None):
            pass #skip
        else:
            #tambahkan ke listPinjam
            for pinjam in akunPinjam.query.all():
                data = {'namaBarang' : pinjam.namaBarang,'namaPemilik':pinjam.namaPemilik,'jumlahPinjam':pinjam.jumlahPinjam,'awalPinjam':pinjam.awalPinjam,'akhirPinjam':pinjam.akhirPinjam}
                listPinjam.append(data)
        dataProfile = {'namaHimpunan':namaHimp,'listBarang':listBarang ,'listPinjam':listPinjam}
        return jsonify(dataProfile)
@app.route('/daftarBarang', methods=['POST'])
def daftarBarang():
    #mendaftarkan barang pemilik
    data = request.json
    if(data is None):
        return Response(status=123)
    else:
        namaHimp = data['namaHimpunan']
        namaBarang = data['namaBarang']
        jumlah = data['jumlah']
        akunHimp = User.query.filter_by(displayName=namaHimp).first()
        if(akunHimp is None):
            return Response(status=404)
            #error, ga ketemu
        else:
            barangBaru = Inventori(namaBarang=namaBarang,jumlahBarang=jumlah,pemilik=akunHimp)
            db.session.add(barangBaru)
            db.session.commit()
            return Response(status=200)
@app.route('/recent', methods=['GET','POST'])
def recent():
    #cari 5 item terakhir
    latest = Inventori.query.order_by(desc(Inventori.id)).limit(5).all()
    #return data json ke 5 item tersebut, latest berisi seperti berikut
    #latest = [<Inventori 5>,<Inventori 4>,<Inventori 3>,<Inventori 2>,<Inventori 1>]
    namaBarang, jumlah, harga, namaHimp = [], [], [], []
    for barang in latest:
        namaBarang.append(barang.namaBarang)
        jumlah.append(barang.jumlahBarang)
        namaHimp.append(barang.namaHimpunan)
    recentJson = jsonify({'namaBarang' : namaBarang, 'jumlah' : jumlah, 'namaHimp' : namaHimp})
    #return recentJson ke front end untuk diolah
    return recentJson,200
@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    tipe = data['tipe']
    if(tipe=='Barang'):
        #cari Barang
        namaBarang = data['cari']
        cekBarang = Inventori.query.filter_by(namaBarang=namaBarang).first()
        if(cekBarang is None):
            #barang tidak ditemukan
            pass
        else:
            #barang ketemu, return sama data himpunannya juga
            akunHimpunan = User.query.filter_by(cekBarang.namaHimpunan).first()
            namaHimpunan = akunHimpunan.displayName
            jumlah = cekBarang.jumlahBarang
            pass
    elif(tipe=='Username'):
        #cari user
        namaHimpunan = data['cari']
        akunHimpunan = User.query.filter_by(displayName=namaHimpunan)
        if(akunHimpunan is None):
            #akun tidak ditemukan
            pass
        else:
            #ketemu
            pass
    else:
        #tipe tidak valid, return error
        pass
@app.route('/login', methods=['GET','POST'])
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
        if(akun.password):
            #sukses, return sukses
            pass
        else:
            #return pass salah
            pass
    return 200
@app.route('/register',methods=['GET','POST'])
def register():
    data = request.data
    username = data['username']
    displayname = data['displayname']
    password = data['password']
    #cari di db apakah usernamenya sudah ada
    cekUsername = User.query.filter_by(username=username).first()
    cekDisplay = User.query.filter_by(displayName=displayname).first()
    if(cekAkun is None):
        #cek apakah displayname sudah dipakai
        if(cekDisplay is None):
            #aman, tambah ke database
            akunBaru = User(username=username,displayName=displayname,password=password) #TODO:encrypt password
            db.session.add(akunBaru)
            db.session.commit()
        else:
            #return displayname udah ada
            pass
    else:
        #return username sudah ada
        pass
    return 200
