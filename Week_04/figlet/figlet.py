from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()
random_font = random.choice(fonts)

if len(sys.argv) == 3 and sys.argv[1] == "-f":
    args = sys.argv[2]
    if not args in fonts:
        sys.exit("Invalid usage")
    else:
        s = input("Input: ")
        figlet.setFont(font=args)
        print(figlet.renderText(s))
elif len(sys.argv) == 1:
    s = input("Input: ")
    figlet.setFont(font=random_font)
    print(figlet.renderText(s))
else:
    sys.exit("Invalid usage")
