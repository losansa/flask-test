from app import db
from selling.model import QuotesName


def get_all_qoutes_names():
    query = db.session.query(QuotesName)  # SELECT * FROM public.quotes_name
    return query.all()
