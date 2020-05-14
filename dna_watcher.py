#!/bin/python3

""" INSTRUCTIONS:
    1) Change values in `config.py`.
    2) Run with python 3 whenever the node starts up.
"""

import csv
from idena_api import IdenaAPI
import time
import datetime

from dna_config import *

# Read api key from file
api_key = None
with open(API_KEY_FILE, "r") as api_key_file:
    api_key = api_key_file.read()

api = IdenaAPI(NODE_ADDRESS, NODE_PORT, api_key=api_key)
print("Api made.")

last_balance = None
while True:
	response = api.balance(ADDRESS)
	result = None

	try:
		result = response["result"]
	except KeyError:
		print("Node error:", response)
		time.sleep(60)
	else:
		current_balance = float(result["balance"]) + float(result["stake"])
		print("Current balance:", current_balance)

		if current_balance != last_balance and last_balance != None:
			print("Writing new balance.")

			with open(CSV_FILE_LOC, "a") as csvfile:
				csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
				csvwriter.writerow([datetime.datetime.now(), current_balance])

		last_balance = current_balance
		
		time.sleep(UPDATE_SLEEP_TIME)
