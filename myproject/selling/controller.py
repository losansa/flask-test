from flask import Blueprint
from flask.json import jsonify

from selling import repository, serializer

route_registrator = Blueprint('hello', __name__)


@route_registrator.route('/')
def get_all_qoutes_names():
    all_quote_names = repository.get_all_qoutes_names()
    # all_quote_names = serializer.convert_quotes_names_to_dict(all_quote_names)
    return jsonify(serializer.convert_quotes_names_to_dict(all_quote_names))
