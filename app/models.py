from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    displayname = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    barang = db.relationship('Inventori', backref='author', lazy='dynamic')
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Inventori(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namabarang = db.Column(db.String(120), index=True, unique=True)
    jumlahbarang = db.Column(db.Integer, index=True)
    harga = db.Column(db.Integer, index=True)
    idHimpunan = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Nama {}>'.format(self.namabarang)
