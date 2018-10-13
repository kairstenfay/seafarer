import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

sns.set(style="whitegrid", font_scale=1.5)


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

    f, ax = plt.subplots()
    f.set_size_inches(len(df[categorical_column].unique()) * .9,
                      len(df[categorical_column].unique()) * .9)
    ax = sns.countplot(x=categorical_column, data=df, hue=hue, dodge=True,
                       palette=sns.color_palette("Set2"))
    ax.set_title(title)
    ax.set_xticklabels(labels=df[categorical_column].unique(), rotation=rotation)

    if hue:
        plt.legend(loc='upper right')
    plt.show()


def scatterplot(df, numerical_column, categorical_column, title=None):
    """
    Creates seaborn scatterplots with conditional means overlaid on the points.

    Parameters
    ----------
        df : a pandas DataFrame containing the data of interest

        numerical_column: a string reprsenting the name of a column on df that will be used as
                          the y-axis data. Must be numerical.

        categorical_column: a string reprsenting the name of a column on df that will be used as
                            the x-axis data. Assumed to be categorical.

        title : a string that will be used as the plot's title
    """

    # Initialize the figure
    f, ax = plt.subplots()
    f.set_size_inches(12, 8)
    sns.despine(bottom=True)

    # Make box pots
    ax = sns.boxplot(data=df, x=numerical_column, y=categorical_column, linewidth=8,
                     fliersize=0, width=.7, palette=sns.color_palette("Set2"))
    for patch in ax.artists:
        r, g, b, a = patch.get_facecolor()
        patch.set_facecolor((r, g, b, .3))

    # Swarm plot
    ax = sns.swarmplot(data=df, x=numerical_column, y=categorical_column,
                       palette=sns.color_palette("Set2")).set_title(title)


def violinplot(df, numerical_column, categorical_column, title=None):
    """
    Creates seaborn scatterplots with conditional means overlaid on the points.

    Parameters
    ----------
        df : a pandas DataFrame containing the data of interest

        numerical_column: a string reprsenting the name of a column on df that will be used as
                          the y-axis data. Must be numerical.

        categorical_column: a string reprsenting the name of a column on df that will be used as
                            the x-axis data. Assumed to be categorical.
        title : a string that will be used as the plot's title
    """
    # Initialize the figure
    f, ax = plt.subplots()
    f.set_size_inches(12, 8)
    sns.despine(bottom=True)

    sns.set_context(rc={'patch.linewidth': 0.0})

    ax = sns.violinplot(data=df, y=categorical_column, x=numerical_column,  # scale="area",
                        palette=sns.color_palette("Set2"), linewidth=1.5,
                        inner="quartile")

    # Show the mean
    means = df.copy(deep=True).groupby(by=categorical_column, as_index=False).mean()
    sns.pointplot(y=categorical_column, x=numerical_column,
                  data=means, color="black", join=None,
                  markers="D", scale=1).set_title(title)


def stacked_barchart(df, x, y):
    sub_df = df[[x, y]]
    sub_df = sub_df[(sub_df[x].notnull()) & (sub_df[y].notnull())]
    sub_df['count'] = 1

    num_groups = len(sub_df[y].unique().tolist())

    sub_df = sub_df.groupby([x, y]).agg('count')
    sub_df = sub_df.unstack(level=1)
    sub_df.columns = sub_df.columns.droplevel()

    original_columns = sub_df.columns.tolist()

    sub_df['total'] = 0
    for column in original_columns:
        print(column)
        sub_df.loc[sub_df[column].isnull(), column] = 0
        sub_df['total'] += sub_df[column]

    for column in original_columns:
        sub_df[column] /= sub_df['total']
        sub_df[column] *= 100

    for i in range(2, num_groups):
        sub_df['level_' + str(i)] = sub_df[original_columns[2 - i]] + sub_df[original_columns[3 - i]]

    plt.bar(sub_df.index, sub_df[original_columns[0]], color=sns.color_palette('Set2')[0],
            edgecolor='white', width=.85)

    counter = 0
    floor = 0
    while counter < num_groups - 1:
        floor += sub_df[original_columns[counter]]

        # Plot series
        plt.bar(sub_df.index, sub_df[original_columns[counter + 1]], bottom=floor,
                color=sns.color_palette('Set2')[::-1][counter + 1], edgecolor='white',
                width=barWidth)
        counter += 1
    return sub_df


def t_test(a, b, numerical_column):
    """
    Perorms a two-tailed t-test for statistical significance and prints results to the console.

    Parameters
    ----------
        a : a pandas DataFrame
        b : a pandas DataFrame
        numerical_column : a string depicting a numerical column that exists on both a and b.
                           Used for comparing statistical significance.
    """
    t, p = stats.ttest_ind(a[numerical_column], b[numerical_column])

    if (t < 0):
        print("The first argument has a lower value than the second.")
    else:
        print("The first argument has a higher value than the second.")

    print(np.around(p, 4))
    if p < 0.05:
        print("Statistically significant two-tailed p-value")