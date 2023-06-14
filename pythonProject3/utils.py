import json
import requests
from config import keys

class ConvertionExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: float):

        if quote == base:
            raise ConvertionExeption(f'Невозможно сконвертировать одинаковую валюту {base}.')

        try:
            quote_tiker = keys[quote.lower()]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')

        try:
            base_tiker = keys[base.lower()]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tiker}&tsyms={base_tiker}')
        total_base = json.loads(r.content)[keys[base]] * amount
        return total_base





