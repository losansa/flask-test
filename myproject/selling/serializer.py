from selling.model import QuotesName, Quote


def convert_quotes_names_to_dict(quotes_names):
    return list(map(convert_quote_name_to_dict, quotes_names))


def convert_quote_name_to_dict(quote_name: QuotesName):
    dictionary = {
        'id': quote_name.id,
        'name': quote_name.name
    }
    dictionary['quotes'] = convert_quotes_to_dict(quote_name.quotes)
    return dictionary


def convert_quotes_to_dict(quotes):
    return list(map(convert_quote_to_dict, quotes))


# def convert_quotes_to_dict(quotes):
#     arr = []
#     for quote in quotes:
#         arr.append(convert_quote_to_dict(quote))
#     return arr

def convert_quote_to_dict(quote: Quote):
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
