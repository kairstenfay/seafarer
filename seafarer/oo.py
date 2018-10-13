import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Static methods
def _sort(df, categorical_column, sort_by=None):
    if sort_by:
        df = df.sort_values(sort_by)
    else:
        df = df.sort_values(categorical_column)
    return df


def _print():
    plt.show()


def histogram(df, categorical_column, hue=None, title=None, sort_by=None, rotation=0):
    """
    """


class CategoricalPlot:
    def __self__(self):
        self.f, self.ax = plt.subplots()

    def resize(self, width, height):
        self.f.set_size_inches(width, height)

    def _validate_dtypes(self):
        pass


class Histogram(CategoricalPlot):

    def __init__(self):
        CategoricalPlot.__init__(self)
    #
    # def plot_type(self, plot_name):
    #     # Make a map for taking user input (case-insensitive) and returning a relevant seaborn plot.
    #     # TODO - how to decide whether Seaborn or Matplotlib?

    def plot(self, df, categorical_column, title, hue=None, rotation=0):
        self.ax = sns.countplot(x=categorical_column, data=df, hue=hue, dodge=True,
                           palette=sns.color_palette("Set2"))
        self.ax.set_title(title)
        self.ax.set_xticklabels(labels=df[categorical_column].unique(),
                                rotation=rotation)

        if hue:
            plt.legend(loc='upper right')

