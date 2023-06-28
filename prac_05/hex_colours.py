"""

"""

COLOUR_NAME_TO_CODE = {"Acid Green": "#b0bf1a", "Amber": "#ffbf00", "Apricot": "#fbceb1", "Aqua": "#00ffff",
                       "Ash Grey": "#b2beb5", "Beige": "#f5f5dc", "Black": "#000000", "Gray": "#bebebe",
                       "Indigo": "#4b0082", "Maroon": "#b03060"}


def main():
    colour_name = str(input("Enter colour name: ")).lower().capitalize()
    print(colour_name)

    while colour_name != "":
        try:
            print(colour_name, "is", COLOUR_NAME_TO_CODE[colour_name])
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").lower().capitalize()


main()
