import matplotlib.pyplot as plt
import seaborn as sns


class BasePlot(object):
    """
    """

    def __init__(self, width=8, height=6):
        self.f, self.ax = plt.subplots()
        # self.f.set_size_inches(width, height)
        self._color_palette = sns.color_palette("Set2"),
        # self._legend_position = "upper right"

    # def resize(self, width, height):
    #     self.f.set_size_inches(width, height)

    @property
    def color_palette(self):
        return self._color_palette

    @color_palette.setter
    def color_palette(self, custom_palette):
        self._color_palette = custom_palette

    def title(self, title):
        """

        :param title: (string, optional) the title of the plot
        """
        self.ax.set_title(title)

    def xticklabels(self, df, x, rotation):
        """

        :param df:
        :param x:
        :param rotation: (int, optional) the degree to which the x-axis labels should be rotated.
        """
        self.ax.set_xticklabels(labels=df[x].unique(),
                                rotation=rotation)

    # @property
    # def legend_position(self):
    #     return self._legend_position
    #
    # @legend_position.setter
    # def legend_position(self, legend_position):
    #     self._legend_position = legend_position


class Histogram(BasePlot):
    """
    """

    def __init__(self):
        BasePlot.__init__(self)

    def plot(self, df, x, hue=None, **kwargs):  # TODO: burn kwargs?
        self.ax = sns.countplot(x=x, data=df, hue=hue, dodge=True,
                                palette=self.color_palette)
        return self.ax

    def _validate_dtypes(self):
        pass


class SwarmBoxPlot(BasePlot):

    def __init__(self):
        BasePlot.__init__(self)

    def plot(self, df, x, y, hue=None):
        sns.despine(bottom=True)

        # Make box pots
        self.ax = sns.boxplot(data=df, x=x, y=y,
                              linewidth=8, fliersize=0, width=.7, hue=hue,
                              palette=self.color_palette)

        for patch in self.ax.artists:
            r, g, b, a = patch.get_facecolor()
            patch.set_facecolor((r, g, b, .3))

        # Swarm plot
        self.ax = sns.swarmplot(data=df, x=x, y=y,
                                hue=hue, palette=self.color_palette)


class ViolinPlot(BasePlot):
    def __init__(self):
        BasePlot.__init__(self)

    def plot(self, df, x, y, hue=None):
        sns.set_context(rc={'patch.linewidth': 0.0})

        self.ax = sns.violinplot(data=df, x=x, y=y, hue=hue,  # scale="area",
                                 palette=self.color_palette, linewidth=1.5,
                                 inner="quartile")

        # Show the mean
        means = df.copy(deep=True).groupby(by=y, as_index=False).mean()
        sns.pointplot(x=x, y=y, data=means, color="black", join=None,
                      markers="D", scale=1)


class ScatterPlot(BasePlot):
    def __init__(self):
        BasePlot.__init__(self)

    def plot(self, df, x, y, hue=None):
        self.ax = sns.scatterplot(data=df, x=x, y=y, marker='o', hue=hue,
                                  alpha=0.75, palette=self.color_palette)
