#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymisp import ExpandedPyMISP
from keys import misp_url, misp_key, misp_verifycert
from phone_iso3166.country import *

# This script is a really simple example on how to extract call spam numbers in Telecom MISP events
# I then create a file with the phone numbers

f = open('fraud_numbers.txt','w')
f.write('number,country_iso2\n')

if __name__ == '__main__':

    misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)
    events = misp.search(tags=['Fraud', 'Fraud_Call_Spam'], return_format='json')

    if not events:
        print('No results for this query')
        exit(0)

    numbers = set()
    for event in events:
        for e in event['Event']['Attribute']:
            number = e['value'].replace('+','')
            if number.isnumeric():
                numbers.add(number)


    for n in numbers:
        c = phone_country(n)
        f.write(n+','+c)
        f.write('\n')

    f.close()
