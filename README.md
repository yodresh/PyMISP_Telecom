# PyMISP Telecom

The goal of this repository is to document how to use the PyMISP lib with simple examples to interact with Telecom Data / Objects via PyMISP.

This project uses PyMISP : https://github.com/MISP/PyMISP and MISP : https://github.com/MISP/MISP. 

Please refer to the PyMISP readme for lib install tutorial.

The list of scripts contain:
* extract_SS7_GT.py : Extract all the offensive GTs from SS7 objects published, write the result into a CSV file
* publish_SS7_event.py : Publish a SS7 event with an SS7-attack object
* publish_iot_event.py : Publish a IoT Malware event with simple attributes
* extract_call_spam.py : Extract fraudulent numbers reported into MISP

These efforts are made to support the GSMA T-ISAC initiative (https://www.gsma.com/security/t-isac/)

We are using PyMISP within POST Luxembourg for our Telecom Intrusion Detection System (TIDS) Solution to fetch and enrich dectection data.

## CO Finance by EU - Part of the PISAX project
![image](https://user-images.githubusercontent.com/1607556/121492977-a77beb80-c9d7-11eb-917c-432ecf4392aa.png)
