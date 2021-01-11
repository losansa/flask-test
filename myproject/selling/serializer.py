from selling.model import QuotesName, Quote


def convert_quotes_names_to_json(quotes_names):
    return list(map(convert_quote_name_to_json, quotes_names))


def convert_quote_name_to_json(quote_name: QuotesName):
    json_dict = {
        'id': quote_name.id,
        'name': quote_name.name
    }
    json_dict['quotes'] = convert_quotes_to_json(quote_name.quotes)
    return json_dict


def convert_quotes_to_json(quotes):
    return list(map(convert_quote_to_json, quotes))


# def convert_quotes_to_json(quotes):
#     arr = []
#     for quote in quotes:
#         arr.append(convert_quote_to_json(quote))
#     return arr

def convert_quote_to_json(quote: Quote):
    return {
        'id': quote.id,
        'max_value': quote.max_value,
        'min_value': quote.min_value,
    }
