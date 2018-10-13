from seafarer.oo import Histogram
from seafarer.colors import ihme_palettes
import matplotlib.pyplot as plt


# Static methods
def sort(df, categorical_column, sort_by=None, ascending=True):
    if sort_by:
        df = df.sort_values(sort_by, acending=ascending)
    else:
        df = df.sort_values(categorical_column, ascending=ascending)
    return df


def _plt_funcs():
    plt.show()
    plt.xlabel("group")


def make_plot(plot_type, df, x, y=None, title=None, rotation=0, dropna=False, custom_palette=None):

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
            plot_object.color_palette = ihme_palettes(custom_palette)

        elif type(custom_palette) is list:
            plot_object.color_palette = custom_palette

    # Plot
    plot_object.plot(df=df, categorical_column=x, title=title, rotation=rotation)
    return


if __name__ == '__main__':
    make_plot("histogram", df=df, x='Age', title="Title", rotation=45,
         dropna=True)
