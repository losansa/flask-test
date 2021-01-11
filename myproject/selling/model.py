from app import db


class QuotesName(db.Model):
    __tablename__ = 'quotes_name'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    quotes = db.relationship('Quote', lazy='joined')


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    min_value = db.Column(db.Float)
    max_value = db.Column(db.Float)
    name_id = db.Column(db.Integer,
                        db.ForeignKey('quotes_name.id', ondelete='CASCADE'),
                        nullable=False)
