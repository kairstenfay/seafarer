import matplotlib.pyplot as plt
import seaborn as sns

# TODO - Make a map for taking user input (case-insensitive) and returning a relevant seaborn plot.


# Static methods
def _sort(df, categorical_column, sort_by=None):
    if sort_by:
        df = df.sort_values(sort_by)
    else:
        df = df.sort_values(categorical_column)
    return df


def _print():
    plt.show()


class CategoricalPlot(object):
    """
    """

    def __init__(self):
        self.f, self.ax = plt.subplots()
        self._colors = sns.color_palette("Set2")
        self._legend_position = "upper right"

    @resize.setter
    def resize(self, width, height):
        self.f.set_size_inches(width, height)

    def _validate_dtypes(self):
        pass

    @
    def _set_color_palette(self, custom_palette):
        self._colors = custom_palette

    def set_color_palette(self, custom_palette):
        self._set_color_palette(custom_palette)

    def get_color_palette(self):
        return self._colors

    def _move_legend(self, legend_position):
        self._legend_position = legend_position

    def legend_position(self, legend_position):
        self._move_legend(legend_position)


class Histogram(CategoricalPlot):
    """
    """

    def __init__(self):
        CategoricalPlot.__init__(self)
        # TODO - how to decide whether Seaborn or Matplotlib?

    def plot(self, df, categorical_column, title, hue=None, rotation=0):
        self.ax = sns.countplot(x=categorical_column, data=df, hue=hue, dodge=True,
                                palette=self.get_color_palette())
        self.ax.set_title(title)
        self.ax.set_xticklabels(labels=df[categorical_column].unique(),
                                rotation=rotation)

        if hue:
            plt.legend(loc=self._legend_position)
