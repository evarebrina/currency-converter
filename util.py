import urllib.request
import json


def get_usd_currency() -> float:
    with urllib.request.urlopen("https://api.exchangeratesapi.io/latest?base=USD&symbols=RUB") as response:
        data = response.read()
    return json.loads(data.decode("utf-8")).get("rates").get("RUB")
