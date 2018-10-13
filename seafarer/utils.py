from seafarer.oo import Histogram
from seafarer.colors import ihme_palettes


def plot(plot_type, df, x, y=None, title=None, rotation=0, dropna=False, custom_palette=None):
    # Drop NaNs
    if dropna:
        for column in [x, y]:
            if column:
                df = df[(df[column].notnull())]

    plot_object = None

    # Choose plot type
    if plot_type.lower() == 'histogram':
        plot_object = Histogram()

    else:
        raise ValueError("The " + plot_type + " plot is not yet implemented.")

    # Assign custom palette
    if custom_palette:
        if type(custom_palette) is not str and type(custom_palette) is not list:
            raise TypeError("custom_palette must be a string or a list")

        if type(custom_palette) is str:
            plot_object.color_palette(ihme_palettes(custom_palette))

        elif type(custom_palette) is list:
            plot_object.color_palette(custom_palette)

    # Plot
    plot_object.plot(df=df, categorical_column=x, title=title, rotation=rotation)
    return


if __name__ == '__main__':
    plot("histogram", df=df, x='Age', title="Title", rotation=45,
         dropna=True)
