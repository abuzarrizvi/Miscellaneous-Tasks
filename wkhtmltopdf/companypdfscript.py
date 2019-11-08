import sys
import os


options = '-d 300 -L 1.5mm -R 1.5mm -T 1.5mm -B 1.5mm --page-width 213mm --page-height 105.13mm --javascript-delay 2000'
command = " wkhtmltopdf " + options + " " + "companypdf.html" + " " + "companypdf.pdf"
#command = " C:\\ProgramData\\wkhtmltopdf\\bin\\wkhtmltopdf.exe " + options + " " + html_path + " " + file_path
#logger.info(command)
os.system(command)