
import os
import csv

import inkex
from inkex.command import inkscape


# there's plan to add qrcode support using qrcode package but maybe later
# import qrcode
# import base64
# from PIL import Image


class SertifGen(inkex.base.TempDirMixin, inkex.base.InkscapeExtension):
    def add_arguments(self, pars):
        pars.add_argument("--csv-input", type=str, default="")
        pars.add_argument("--target", type=str, default="")
        pars.add_argument("--export-path", type=str, default="")


        # why we're still here (basically useless but needed)
        pars.add_argument("--main", type=str, default="")
        pars.add_argument("--id", type=str, default="")


    def effect(self):

        data = self.options.csv_input
        exportPath = self.options.export_path
        targetFormat = self.options.target

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
                cooked = cooked.replace(toReplace, i[y])

            with open(modifiedIngredients, "w") as wrt:
                wrt.write(cooked)
            
            wrt.close()

            cli_process = inkscape(modifiedIngredients, actions=f'export-filename:{exportPath}/{i[0]}.{targetFormat};export-do;FileClose')
            
            if len(cli_process) > 0:
                self.debug(_("Inkscape returned this messages while exporting, maybe your file(s) is successfully exported but with some warnings : "))
                self.debug(cli_process)

        return True


    def load(self, stream):
        return str(stream.read(), "utf-8")
    
    def save(self, stream):
        # doing nothing
        pass

if __name__ == '__main__':
    SertifGen().run()