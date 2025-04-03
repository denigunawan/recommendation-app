from app.extensions import db
import pandas as pd

class DaftarPerusahaan(db.Model):
    __tablename__ = "daftar_perusahaan"

    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    listing_date = db.Column(db.String(50), nullable=False)
    shares = db.Column(db.BigInteger, nullable=False)
    listing_board = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "listing_date": self.listing_date,
            "shares": self.shares,
            "listing_board": self.listing_board
        }
    
def save_to_db(dataframe):
    for _, row in dataframe.iterrows():
        perusahaan = DaftarPerusahaan(
            code=row['code'],
            name=row['name'],
            listing_date=pd.to_datetime(row['listing_date']).date(),
            shares=int(row['shares']),
            listing_board=row['listing_board']
        )
        db.session.merge(perusahaan)
    db.session.commit()

# -------------- sectors
class Sector(db.Model):
    __tablename__ = "sectors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
def save_to_db_sectors(dataframe):
    for _, row in dataframe.iterrows():
        sector = Sector(
            id=row['id'],
            name=row['name']
        )
        db.session.merge(sector)
    db.session.commit()
# -------------- lq45
class LQ45(db.Model):
    __tablename__ = "lq45"

    code = db.Column(db.String(10), db.ForeignKey('daftar_perusahaan.code'), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    listing_date = db.Column(db.Date, nullable=False)
    shares = db.Column(db.BigInteger, nullable=False)
    listing_board = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "listing_date": self.listing_date.strftime('%Y-%m-%d'),
            "shares": self.shares,
            "listing_board": self.listing_board
        }
def save_to_db_lq45(dataframe):
    for _, row in dataframe.iterrows():
        lq = LQ45(
            code=row['code'],
            name=row['name'],
            listing_date=pd.to_datetime(row['listing_date']).date(),
            shares=int(row['shares']),
            listing_board=row['listing_board']
        )
        db.session.merge(lq)
    db.session.commit()

# -------------- INFORMASI SAHAM
# -------------- Informasi Saham
class InformasiSaham(db.Model):
    __tablename__ = "informasi_saham"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(10), db.ForeignKey('daftar_perusahaan.code'))
    date = db.Column(db.Date, nullable=False)
    previous = db.Column(db.Numeric(15, 2))
    open_price = db.Column(db.Numeric(15, 2))
    first_trade = db.Column(db.Numeric(15, 2))
    high = db.Column(db.Numeric(15, 2))
    low = db.Column(db.Numeric(15, 2))
    close = db.Column(db.Numeric(15, 2))
    change = db.Column(db.Numeric(15, 2))
    volume = db.Column(db.BigInteger)
    value = db.Column(db.BigInteger)
    frequency = db.Column(db.BigInteger)
    index_individual = db.Column(db.Numeric(15, 2))
    offer = db.Column(db.Numeric(15, 2))
    offer_volume = db.Column(db.BigInteger)
    bid = db.Column(db.Numeric(15, 2))
    bid_volume = db.Column(db.BigInteger)
    listed_shares = db.Column(db.BigInteger)
    tradeable_shares = db.Column(db.BigInteger)
    weight_for_index = db.Column(db.Numeric(10, 5))
    foreign_sell = db.Column(db.BigInteger)
    foreign_buy = db.Column(db.BigInteger)
    delisting_date = db.Column(db.Date, nullable=True)
    non_regular_volume = db.Column(db.BigInteger)
    non_regular_value = db.Column(db.BigInteger)
    non_regular_frequency = db.Column(db.BigInteger)

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "date": self.date.strftime('%Y-%m-%d'),
            "previous": str(self.previous),
            "open_price": str(self.open_price),
            "first_trade": str(self.first_trade),
            "high": str(self.high),
            "low": str(self.low),
            "close": str(self.close),
            "change": str(self.change),
            "volume": self.volume,
            "value": self.value,
            "frequency": self.frequency,
            "index_individual": str(self.index_individual),
            "offer": str(self.offer),
            "offer_volume": self.offer_volume,
            "bid": str(self.bid),
            "bid_volume": self.bid_volume,
            "listed_shares": self.listed_shares,
            "tradeable_shares": self.tradeable_shares,
            "weight_for_index": str(self.weight_for_index),
            "foreign_sell": self.foreign_sell,
            "foreign_buy": self.foreign_buy,
            "delisting_date": self.delisting_date.strftime('%Y-%m-%d') if self.delisting_date else None,
            "non_regular_volume": self.non_regular_volume,
            "non_regular_value": self.non_regular_value,
            "non_regular_frequency": self.non_regular_frequency
        }

def save_to_db_informasi_saham(dataframe):
    for _, row in dataframe.iterrows():
        informasi = InformasiSaham(
            code=row['code'],
            date=pd.to_datetime(row['date']).date(),
            previous=row['previous'],
            open_price=row['open_price'],
            first_trade=row['first_trade'],
            high=row['high'],
            low=row['low'],
            close=row['close'],
            change=row['change'],
            volume=row['volume'],
            value=row['value'],
            frequency=row['frequency'],
            index_individual=row['index_individual'],
            offer=row['offer'],
            offer_volume=row['offer_volume'],
            bid=row['bid'],
            bid_volume=row['bid_volume'],
            listed_shares=row['listed_shares'],
            tradeable_shares=row['tradeable_shares'],
            weight_for_index=row['weight_for_index'],
            foreign_sell=row['foreign_sell'],
            foreign_buy=row['foreign_buy'],
            delisting_date=pd.to_datetime(row['delisting_date'], errors='coerce').date() if pd.notna(row['delisting_date']) else None,
            non_regular_volume=row['non_regular_volume'],
            non_regular_value=row['non_regular_value'],
            non_regular_frequency=row['non_regular_frequency']
        )
        db.session.merge(informasi)
    db.session.commit()