#!/usr/bin/env python3

import requests
import typing as t
import typer

from config import *

BASE_URL_EXCHANGE = f"https://api.collectapi.com/economy/exchange"
BASE_URL_GOLD = f"https://api.collectapi.com/economy/goldPrice"


def main(
    base_currency: t.Annotated[str, typer.Option("-b")],
    amounts: t.Annotated[t.Optional[t.List[float]], typer.Option("-a")]=None,
    currencies: t.Annotated[t.Optional[t.List[str]], typer.Option("-c")]=None,
):
    if amounts and currencies:
        total = 0
        for amount, currency in zip(amounts, currencies):
            if currency == base_currency:
                total += amount
                continue
            res = requests.get((BASE_URL_GOLD if currency == "XAU" else BASE_URL_EXCHANGE) + f"?int={amount}&base={currency}&to={base_currency}", headers={
                "Authorization": API_KEY,
                "Content-Type": "application/json"
            })
            if currency == "XAU":
                calcd = amount * float(res.json()["result"][0]["selling"])
            else:
                calcd = float(res.json()["result"]["data"][0]["calculated"])
            total += calcd
        print(round(total, 2), base_currency)

if __name__ == "__main__":
    typer.run(main)
