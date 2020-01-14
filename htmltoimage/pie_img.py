import os

options = "--crop-h 348 --crop-w 428 --crop-x 139 --crop-y 60 --format png --javascript-delay 2000"
path_wkthmltoimage = r'wkhtmltoimage'

command = " wkhtmltoimage " + options + " " + "dailyiqpiechart.html" + " " + "fsd10.jpg"

os.system(command)
