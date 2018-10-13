from seafarer.oo import Histogram
from seafarer.colors import ihme_palettes
import matplotlib.pyplot as plt

plot_types = {'histogram': Histogram(),
              'countplot': Histogram()
              }


# Static methods
def sort(df, sort_column, ascending=True):
    """
    Sorts a given DataFrame by a given column and returns it.

    :param df: (pandas DataFrame) the data to be sorted.
    :param sort_column: (string) describes which column on the given DataFrame to sort. Raises KeyError if the column
                        does not exist in the DataFrame.
    :param ascending: (boolean, optional) if True, sorts the given DataFrame in ascending order on the given column
    :return df: (pandas DataFrame) the data, now sorted on the given sort column.
    """
    if sort_column not in df.columns:
        raise KeyError("The sorting column is not present in the given DataFrame.")

    return df.sort_values(sort_column, ascending=ascending)


def _plt_funcs():
    plt.show()


def save_plot(file_path):
    """
    Saves a generated plot to a given file path.

    :param file_path: (string) describes the local file path for the saved plot.
    """
    plt.savefig(file_path, bbox_inches="tight")


def make_plot(plot_type, df, x, y=None, title=None, rotation=0, dropna=False,
              custom_palette=None, xlabel=None, ylabel=None):
    """
    Plots a figure of the given plot type using the given DataFrame.

    :param plot_type: (string) describes the plot to be created. Raises ValueError if the plot
                      is not in the list of implemented plot types.
    :param df: (pandas DataFrame) the data to be plotted.
    :param x: (string) describes which column on the DataFrame to use as the x-axis. Raises a
              KeyError if the given column does not exist in the DataFrame.
    :param y: (string, optional) describes which column on the DataFrame to use as the y-axis.
              Raises a KeyError if the given column does not exist in the DataFrame.
    :param title: (string, optional) the title of the plot
    :param rotation: (int, optional) the degree to which the x-axis labels should be rotated.
    :param dropna: (bool, optional) if True, removes NaNs from the x-axis and y-axis.
    :param custom_palette: (list or strings, optional)
    :param xlabel: (string, optional) the name for the x-axis label
    :param ylabel: (string, optional) the name for the y=axis label
    """

    # Validate column names
    if x not in df.columns:
        raise KeyError("The given column \"" + x + "\" is not present in the given DataFrame.")
    if y:
        if y not in df.columns:
            raise KeyError("The given column \"" + y + "\" is not present in the given DataFrame.")

    # Choose plot type
    try:
        plot_object = plot_types[plot_type.lower()]

    except ValueError:
        print("The " + plot_type + " plot is not yet implemented.\n" +
              "Please choose from the following list: \n")
        for key in plot_types.keys():
            print("\t- " + key)

    # Optionally drop NaNs
    if dropna:
        for column in [x, y]:
            if column:
                df = df[(df[column].notnull())]

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

    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)


if __name__ == '__main__':

    # Example run
    make_plot("histogram", df=df, x='Age', title="Title", rotation=45,
              dropna=True)
