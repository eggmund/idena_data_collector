#!/bin/python3

""" INSTRUCTIONS:
    1) Install pycoingecko using `pip install --user pycoingecko`
    2) Install numpy and matplotlib through the same method.
    3) Update values in `dna_config.py` to your shtuff.
    4) Run with python 3.
"""

import csv
import time
from numpy import *
from matplotlib.pyplot import *
from pycoingecko import CoinGeckoAPI
import datetime

from dna_config import *

datetimes = []
dna = []

with open(CSV_FILE_LOC, "r") as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        if row:
            datetimes.append(datetime.datetime.fromisoformat(row[0]).timestamp())
            dna.append(float(row[1]))



datetimes = array(datetimes, dtype=float)
dna = array(dna, dtype=float)
print("%a\n%a" % (datetimes, dna))

coef = polyfit(datetimes, dna, 1)
p = poly1d(coef)
print(p)

cg = CoinGeckoAPI()
dna_price = cg.get_price(ids="idena", vs_currencies=["usd", "gbp"])["idena"]

dna_per_day = coef[0] * 60 * 60 * 24    # gradient is in units dna/second, so multiply to get dna/day
print("DNA/day: %.4f. $%.2f/day, £%.2f/day." % (dna_per_day, dna_per_day * dna_price["usd"], dna_per_day * dna_price["gbp"]))


xlabel("Datetime")
ylabel("DNA")
plot(datetimes, dna, "x", label="Data")
plot(datetimes, dna, label="Data")

x = linspace(min(datetimes), max(datetimes), 1000)
plot(x, p(x), label="Best fit")

legend(loc="best")
show()
