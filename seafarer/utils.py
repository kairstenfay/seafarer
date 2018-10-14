from seafarer.models import Histogram, SwarmBoxPlot, ViolinPlot, ScatterPlot
from seafarer.colors import ihme_palettes
import matplotlib.pyplot as plt
import re

plot_types = {
              'histogram': Histogram(),
              'swarmboxplot': SwarmBoxPlot(),
              'violinplot': ViolinPlot(),
              'scatterplot': ScatterPlot()
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


def make_plot(plot_type, df, x, dropna=False, custom_palette=None, hue=None,
              legend_position="upper right", width=11.5, height=8.5, **yarg):
    """
    Plots a figure of the given plot type using the given DataFrame.

    :param plot_type: (string) describes the plot to be created. Raises ValueError if the plot
                      is not in the list of implemented plot types.
    :param df: (pandas DataFrame) the data to be plotted.
    :param x: (string) describes which column on the DataFrame to use as the x-axis. Raises a
              KeyError if the given column does not exist in the DataFrame.
    :param y: (string, optional) describes which column on the DataFrame to use as the y-axis.
              Raises a KeyError if the given column does not exist in the DataFrame.
    :param dropna: (bool, optional) if True, removes NaNs from the x-axis and y-axis.
    :param custom_palette: (list or strings, optional)
    :param hue:
    :param legend_position:
    :param width:
    :param height:
    :return plot_object: #TODO
    """
    plt.subplots(figsize=(width, height))

    # Validate column names
    if x not in df.columns:
        raise KeyError("The given column \"" + x + "\" is not present in the given DataFrame.")
    for y in yarg:
        if yarg[y] not in df.columns:
            raise KeyError("The given column \"" + yarg[y] + "\" is not present in the given DataFrame.")

    # Choose plot type
    try:
        plot_object = plot_types[re.sub('[ -_]', '', plot_type.lower())]

    except KeyError:
        print("The " + plot_type + " plot is not yet implemented.\n" +
              "Please choose from the following list: \n")
        for key in plot_types.keys():
            print("\t- " + key)

    # Optionally resize
    # if width and height:
    #     plot_object.resize(width, height)

    # Optionally drop NaNs
    if dropna:
        for y in yarg:
            for column in [x, yarg[y]]:
                if column:
                    df = df[(df[yarg[y]].notnull())]

    # Assign custom palette
    if custom_palette:
        if type(custom_palette) is not str and type(custom_palette) is not list:
            raise TypeError("custom_palette must be a string or a list")

        if type(custom_palette) is str:
            plot_object.color_palette = ihme_palettes(custom_palette)

        elif type(custom_palette) is list:
            plot_object.color_palette = custom_palette

    # Plot
    for y in yarg:
        plot_object.plot(df=df, x=x, y=yarg[y], hue=hue)

    # Position legend
    if hue:
        plt.legend(loc=legend_position)

    return plot_object


def edit_labels(xlabel=None, ylabel=None):
    """

    :param xlabel: (string, optional) the name for the x-axis label
    :param ylabel: (string, optional) the name for the y=axis label
    """
    # Add title, labels
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)


if __name__ == '__main__':

    # Example run
    plot = make_plot("histogram", df=df, x='Age', dropna=True)
    plot.title("Title!")
    plot.xticklabels(df=df, x='Age', rotation=45)

    edit_labels(xlabel=None, ylabel=None)
