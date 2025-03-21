from app.extensions import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "author": self.author}

class Asset(db.Model):
    __tablename__ = "asset"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    no_assets = db.Column(db.String(30), nullable=True)
    tanggal_diterima = db.Column(db.String(30), nullable=True)
    nama = db.Column(db.String(30), nullable=True)
    quantity = db.Column(db.String(30), nullable=True)
    harga_assets = db.Column(db.Numeric, nullable=True)
    tanggal_input = db.Column(db.String(30), nullable=True)
    vendor = db.Column(db.String(255), nullable=True)
    jenis = db.Column(db.String(255), nullable=True)
    user_id = db.Column(db.BigInteger, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "no_assets": self.no_assets,
            "tanggal_diterima": self.tanggal_diterima,
            "nama": self.nama,
            "quantity": self.quantity,
            "harga_assets": str(self.harga_assets),  # Konversi ke string agar JSON bisa membaca
            "tanggal_input": self.tanggal_input,
            "vendor": self.vendor,
            "jenis": self.jenis,
            "user_id": self.user_id
        }
