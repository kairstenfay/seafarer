import matplotlib.pyplot as plt
import seaborn as sns


class CategoricalPlot(object):
    """
    # TODO abstract again for all types of plots?
    """

    def __init__(self):
        self.f, self.ax = plt.subplots()
        self._color_palette = sns.color_palette("Set2"),
        self._legend_position = "upper right"

    def resize(self, width, height):
        self.f.set_size_inches(width, height)

    def _validate_dtypes(self):
        pass

    @property
    def color_palette(self):
        return self._color_palette

    @color_palette.setter
    def color_palette(self, custom_palette):
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

    def plot(self, df, categorical_column, title, hue=None, rotation=0):
        self.ax = sns.countplot(x=categorical_column, data=df, hue=hue, dodge=True,
                                palette=self.color_palette)
        self.ax.set_title(title)
        self.ax.set_xticklabels(labels=df[categorical_column].unique(),
                                rotation=rotation)

        if hue:
            plt.legend(loc=self._legend_position)
