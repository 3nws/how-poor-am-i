# How poor am I?

Tells you how poor you are in a certain currency given all your other currencies and XAU. 
w/ [CollectAPI](https://collectapi.com/).

## Usage

```
$ ./calc.py -b BASE_CURRENCY_CODE [-a] [FLOAT_AMOUNT] [-c] [CURRENCY_CODE] [-a] [FLOAT] [-c] [CURRENCY_CODE] ...
```
```
python3 calc.py -b BASE_CURRENCY_CODE [-a] [FLOAT_AMOUNT] [-c] [CURRENCY_CODE] [-a] [FLOAT_AMOUNT] [-c] [CURRENCY_CODE] ...
```

## Example

```
python3 calc.py -b TRY -a 225 -c TRY -a 25223 -c TRY -a 500 -c TRY -a 4.37 -c XAU -a 80.21 -c USD
```