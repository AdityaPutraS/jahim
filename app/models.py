from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    displayName = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    barang = db.relationship('Inventori', backref='pemilik',cascade='all,delete', lazy=True)
    pinjam = db.relationship('Pinjam',backref='peminjam',cascade='all,delete',lazy=True)
    def __repr__(self):
        return '<User : {}>'.format(self.displayName)

class Inventori(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namaBarang = db.Column(db.String(120), index=True, unique=True)
    jumlahBarang = db.Column(db.Integer, index=True)
    namaHimpunan = db.Column(db.String(120), db.ForeignKey('user.displayName'))

    def __repr__(self):
        return '<Pemilik : {}>'.format(self.namaBarang)

class Pinjam(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    namaPeminjam = db.Column(db.String(120), db.ForeignKey('user.displayName'))
    namaBarang = db.Column(db.String(120),index=True)
    namaPemilik = db.Column(db.String(120))
    jumlahPinjam = db.Column(db.Integer, index=True)
    awalPinjam = db.Column(db.Integer)
    akhirPinjam = db.Column(db.Integer)

    def __repr__(self):
        return '<Peminjam : {}'.format(self.namaPeminjam)
