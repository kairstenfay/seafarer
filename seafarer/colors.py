palette_names = {'gbd_super_regions': ['#D32B47', "#22973D", "#FCA048", "#1ABAB5", "#CD4AA2", "#BEEA6B", "#005E5B"]}
# TODO - refactor into config file or central location shared b/w python and r


def palette(palette_name):
    try:
        return palette_names[palette_name.lower()]
    except KeyError as e:
        print("The color palette " + palette_name + " has not been implemented. \
              Please choose from an existing palette: \n")
        print(palette_names.keys())



