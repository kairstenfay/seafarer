def histogram(df, categorical_column, hue=None, title=None, sort_by=None, rotation=0):
    """
    Creates seaborn histograms using categorical data.

    Parameters
    ----------
        df : a pandas DataFrame containing the data of interest

        categorical_column: a string representing the name of a column on df that will be used as
                            the x-axis data. Assumed to be categorical.
        title : a string that will be used as the plot's title
        hue : (optional) a string representing the name of a column on df that will be used for
              grouping within each given categorical column.

        sort_by : (optional) a string representing the name of a column on df that will be used to
                  sort df in ascending order. The default argument (None) uses the categorical
                  column for sorting.

    """
    if sort_by:
        df = df.sort_values(sort_by)
    else:
        df = df.sort_values(categorical_column)


    ax = sns.countplot(x=categorical_column, data=df, hue=hue, dodge=True,
                       palette=sns.color_palette("Set2"))
    ax.set_title(title)
    ax.set_xticklabels(labels=df[categorical_column].unique(), rotation=rotation)

    if hue:
        plt.legend(loc='upper right')
    plt.show()


class SeabornPlot(object):

    def __self__(self):
        self.f, self.ax = plt.subplots()
        self.f.set_size_inches(len(df[categorical_column].unique()) * .9,
                               len(df[categorical_column].unique()) * .9)

    def plot_type(self, plot_name):
        # Have a map here for taking user input (case-insensitive) and returning a relevant seaborn plot.
        # TODO - how to decide whether Seaborn or Matplotlib?