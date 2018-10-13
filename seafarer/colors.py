palette_names = {'gbd_super_regions': ['#D32B47', "#22973D", "#FCA048", "#1ABAB5", "#CD4AA2", "#BEEA6B", "#005E5B"]}
# TODO - refactor into config file or central location shared b/w python and r


def ihme_palettes(palette_name):
    try:
        return palette_names[palette_name.lower()]
    except KeyError:
        print("Warning: The color palette \"" + palette_name + "\" has not been implemented. " +
              "Using default color palette \"Set2\" (seaborn) instead.\n" +
              "Please choose from an existing palette: \n")

        for key in palette_names.keys():
            print("\t- " + key)
