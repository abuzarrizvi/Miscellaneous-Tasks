import os

options = "--crop-h 390 --crop-w 600 --crop-x 10 --crop-y 5 --format png --javascript-delay 3000"
path_wkthmltoimage = r'wkhtmltoimage'



#command = " wkhtmltoimage " + options + " " + "dailyiqpiechart.html" + " " + "fsd10.jpg"
command = " C:\\ProgramData\\wkhtmltopdf\\bin\\wkhtmltoimage.exe " + options + " " + "stock.html" + " " + "fsd10.jpg"

os.system(command)
