from PIL import Image
import os
import qrcode
import csv
import base64
import inkex
from inkex.command import inkscape



class SertifGen(inkex.base.TempDurMixin, inkex.base.InkscapeExtension):
    def add_arguments(self, pars):
        pars.add_argument("--csv-path", type=str, default="")
        pars.add_argument("--target", type=str, default="")

    def effect(self):
        data = "sertifPanitia.csv"

        with open(data, newline='') as fi:
            reader = csv.reader(fi)
            DATA = list(reader)

        fi.close

        ranged = len(DATA)

        raw = self.document

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


if __name__ == '__main__':
    SertifGen.run()