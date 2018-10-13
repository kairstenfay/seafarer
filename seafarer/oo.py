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

    def __init__(self, color_palette=sns.color_palette("Set2"), legend_position="upper right"):
        self.f, self.ax = plt.subplots()
        self._color_palette = color_palette
        self._legend_position = legend_position

    def resize(self, width, height):
        self.f.set_size_inches(width, height)

    def _validate_dtypes(self):
        pass

    @property
    def colors(self):
        return self._color_palette

    @colors.setter
    def colors(self, custom_palette):
        self._color_palette = custom_palette

    @property
    def legend_position(self):
        return self._legend_position

    @legend_position.setter
    def legend_position(self, legend_position):
        self._legend_position = legend_position


class Histogram(CategoricalPlot):
    """
    """

    def __init__(self):
        CategoricalPlot.__init__(self)
        # TODO - how to decide whether Seaborn or Matplotlib?

    def plot(self, df, categorical_column, title, hue=None, rotation=0):
        self.ax = sns.countplot(x=categorical_column, data=df, hue=hue, dodge=True,
                                palette=self.colors)
        self.ax.set_title(title)
        self.ax.set_xticklabels(labels=df[categorical_column].unique(),
                                rotation=rotation)

        if hue:
            plt.legend(loc=self._legend_position)
