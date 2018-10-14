import seaborn as sns

palette_names = {
                'gbd_super_regions': ['#D32B47', "#22973D", "#FCA048", "#1ABAB5", "#CD4AA2", "#BEEA6B", "#005E5B"],
                'seq_ihme-green-1': ['#27472F', '#176E2D', '#22973D', '#BEEA6B', '#E2F6A7']
                }
# TODO - refactor into config file or central location shared b/w python and r


def ihme_palettes(palette_name):
    """
    Takes a given string and returns the associated IHME color palette.

    :param palette_name: (string) the name of the desired IHME color palette.
    :return palette_names: (list) a list of hex values that correspond to the given palette name.
    """
    try:
        return palette_names[palette_name.lower()]
    except KeyError:
        print("Warning: The color palette \"" + palette_name + "\" has not been implemented. " +
              "Using default color palette \"Set2\" (seaborn) instead.\n" +
              "Please choose from an existing palette: \n")

        for key in palette_names.keys():
            print("\t- " + key)
        return sns.color_palette('Set2')
