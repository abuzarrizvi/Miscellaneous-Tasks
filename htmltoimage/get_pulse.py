import json
import traceback
import logging
import socket

import base64
import urllib.request
import urllib.parse
import uuid
import requests



payload = {'username': 'l134129@lhr.nu.edu.pk', 'token': 'aoisdhfjiasd51f6a8sd4fadsfhasduf'}
pulse_response = requests.post('http://127.0.0.1:8000/v2/heatmaps/', data=payload)


user_pulse = pulse_response.json()
user_pulse = user_pulse['result']
pulse_30 = user_pulse['heatmap_30']

data =  {'alerts': {'alert_3': [0.503, '#93A4BA'], 'alert_22': [0.251, '#D24556'], 'alert_8': [10.804, '#6C35C0'], 'alert_11': [2.01, '#7ED6FF'], 'alert_20': [0, '#30374E'], 'alert_15': [3.015, '#009524'], 'alert_24': [0.503, '#F1681E'], 'alert_5': [4.774, '#4DC929'], 'alert_23': [1.256, '#A64E00'], 'alert_9': [9.799, '#006FF1'], 'alert_10': [1.005, '#00C7C3'], 'alert_18': [0, '#AEA6E8'], 'alert_13': [2.513, '#F68CAD'], 'alert_12': [36.683, '#F59223'], 'alert_14': [0.251, '#E5A784'], 'alert_17': [6.533, '#1A3A96'], 'alert_16': [0, '#B846CA'], 'alert_19': [1.256, '#F4C600'], 'alert_21': [18.844, '#B83E78']}, 'articles_count': 398}

pie_data = {
                    "alert_3": 0,
                    "alert_5": 0,
                    "alert_8": 0,
                    "alert_9": 0,
                    "alert_10": 0,
                    "alert_11": 0,
                    "alert_12": 0,
                    "alert_13": 0,
                    "alert_14": 0,
                    "alert_15": 0,
                    "alert_16": 0,
                    "alert_17": 0,
                    "alert_18": 0,
                    "alert_19": 0,
                    "alert_20": 0,
                    "alert_21": 0,
                    "alert_22": 0,
                    "alert_23": 0,
                    "alert_24": 0
                }

for pulse in pulse_30:
	company_article_count = pulse['articles_count']
	print(company_article_count)

	for key,value in pulse['alerts'].items():
		pie_data[key] = pulse['alerts'][key] + round(((pulse['alerts'][key]*company_article_count)/100), 3)
		
	print(pie_data)
	print("///////////////////////////////////////////////////////////")
print(pie_data)
