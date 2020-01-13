import imgkit

import os
import imgkit


options = {
    'format': 'png',
    'javascript-delay': '2000',
    'crop-h': '343',
    'crop-w': '400',
    'crop-x': '146',
    'crop-y': '60',
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ]
}
path_wkthmltoimage = r'C:\ProgramData\wkhtmltopdf\bin\wkhtmltoimage.exe'
#path_wkthmltoimage = r'wkhtmltoimage'
config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)

imgkit.from_file('dailyiqpiechart.html','fsd1.jpg', options=options, config=config)