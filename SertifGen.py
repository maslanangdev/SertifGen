from PIL import Image
import os
import qrcode
import csv
import base64

data = input("insert csv data : ")

if data == '':
    data = "sertifPanitia.csv"

with open(data, newline='') as fi:
    reader = csv.reader(fi)
    DATA = list(reader)

fi.close

ranged = len(DATA)

with open("basicTemp.svg", 'r') as infile:
    raw = infile.read()

for i in DATA[1:]:
        
    cooked = raw
    
    for y in range(len(DATA[0])):
        toReplace = "{_" + DATA[0][y] + "_}"
        print(toReplace, end=" => ")
        cooked = cooked.replace(toReplace, i[y])
        print(i[y])

    with open("modified.svg", "w") as wrt:
        wrt.write(cooked)
    wrt.close()
    os.system(f'inkscapecom --export-filename="output/{i[0]}.pdf" modified.svg')
    print("Done : " + i[0])

    print("===================================")



infile.close()