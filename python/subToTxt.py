from pysubparser import parser

#subtitles = parser.parse('NetPlus\\data\\testZippage\\sous-titres-adezipper-Copie\\buffy\\Buffy-2x01WhenSheWasBad.EN.sub', encoding='ansi')
subtitles = parser.parse('NetPlus\\data\\testZippage\\sous-titres-adezipper-Copie\\desperatehousewives\Desperate.Housewives.612.2hd.EN.TAG.ass', encoding='ansi')

for subtitle in subtitles:
    print(subtitle)