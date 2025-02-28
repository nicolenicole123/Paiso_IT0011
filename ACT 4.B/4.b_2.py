import csv

currency_rates = {}
with open("currency.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        code, name, rate = row
        currency_rates[code] = float(rate)


usd_amount = float(input("How much dollar do you have? "))
currency_code = input("What currency you want to have? ").upper()


if currency_code in currency_rates:
    converted_amount = usd_amount * currency_rates[currency_code]
    print(f"\nDollar: {usd_amount} USD")
    print(f"{currency_code}: {converted_amount:.6f}")
else:
    print("Currency not found.")
