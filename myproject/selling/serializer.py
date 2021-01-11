from selling.model import QuotesName, Quote


def convert_quotes_names_to_json(quotes_names):
    return dict(map(convert_quote_name_to_json, quotes_names))


def convert_quote_name_to_json(quote_name: QuotesName):
    json_dict = {
        'id': quote_name.id,
        'name': quote_name.name
    }
    json_dict['quotes'] = convert_quotes_to_json(quote_name.quotes)
    return json_dict


def convert_quotes_to_json(quotes):
    return dict(map(convert_quote_to_json, quotes))


# def convert_quotes_to_json(quotes):
#     arr = []
#     for quote in quotes:
#         arr.append(convert_quote_to_json(quote))
#     return arr

def convert_quote_to_json(quote: Quote):
    return {
        'id': quote.id,
        'date_time': quote.date_time,
        'q_open': quote.q_open,
        'q_high': quote.q_high,
        'q_low': quote.q_low,
        'q_adj_close': quote.q_adj_close,
        'q_close': quote.q_close,  
        'q_volume': quote.q_volume, 
    }
