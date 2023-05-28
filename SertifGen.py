from PIL import Image
import os
# import qrcode
import csv
import base64
import inkex
from inkex.command import inkscape



class SertifGen(inkex.base.TempDirMixin, inkex.base.InkscapeExtension):
    def add_arguments(self, pars):
        pars.add_argument("--csv-input", type=str, default="")
        pars.add_argument("--target", type=str, default="")


        # why we're still here
        pars.add_argument("--main", type=str, default="")
        pars.add_argument("--id", type=str, default="")


    def effect(self):
        # data = "sertifPanitia.csv"
        data = self.options.csv_input

        with open(data, newline='') as fi:
            reader = csv.reader(fi)
            DATA = list(reader)

        fi.close

        raw = self.document


        modifiedIngredients = os.path.join(self.tempdir, "tempSertif.svg")

        for i in DATA[1:]:
                
            cooked = raw
            
            for y in range(len(DATA[0])):
                toReplace = "{_" + DATA[0][y] + "_}"
                print(toReplace, end=" => ")
                cooked = cooked.replace(toReplace, i[y])
                with open("ReadyDebug.txt", "a") as wrt:
                    wrt.write(toReplace)

            with open(modifiedIngredients, "w") as wrt:
                wrt.write(cooked)
            

            wrt.close()
            cli_process = inkscape(modifiedIngredients, actions=f'export-filename:{i[0]}.pdf;export-do;FileClose')
            
            self.debug(cli_process)
            # print("Done : " + i[0])

            # print("===================================")
        return True


    def load(self, stream):
        return str(stream.read(), "utf-8")
    
    def save(self, stream):
        # doing nothing
        pass

if __name__ == '__main__':
    SertifGen().run()