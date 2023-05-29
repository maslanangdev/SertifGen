# SertifGen
an Inkscape Extension to batch generate sertificate, it might be similar with [Maren Hachmann's NextGenerator ](https://gitlab.com/Moini/nextgenerator) but with more straightforward usage

## How to Install
copy `SertifGen.inx` and `SertifGen.py` to inkscape extensions directory, it's usually located in `%appdata%\Roaming\inkscape\extensions` on Windows or `/usr/share/inkscape/extensions` on Linux. Or you can check it through `Edit -> Preferences -> System`

## How to Use
* prepare the CSV file, you can create it from spreadsheet editor like `LibreOffice Calc` (recommended)
* the first row should contains variables name
* prepare your design in inkscape, use text tool to define the variables and match it with your first row of csv. For example if there's a row named `name` in your data then use `{_name_}` in your design
* then in Inkscape, go to `Extensions -> Export -> SertifGen` then browse for your csv file, choose your output format, define your export path, then hit `Apply`
* your Inkscape might be not responding while exporting your file(s), it's okay (for now)
* if there's something still confuse you, there's examples files that I prepared for demonstration purpose

## I have a problem, and a feature request
you can open an [issue](https://github.com/maslanangdev/SertifGen/issues/new) on this repository, any bug reports or feature requests (as long as it make sense for me) is appreciated

_*anyway sorry for my bad english_
