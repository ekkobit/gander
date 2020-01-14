"""Plotting of stock data."""

import numpy as np
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection


def candles(df, ax, cwidth=0.6, lwidth=1, columns=None, colors=None,
            impulse=None):
    r"""Draw a candle chart in the figure main ax.

    :param df: Input data frame
    :param ax: Axes instance of subplot to plot candles in
    :param cwidth: width of candle, 1 is full width, 0 is no width
    :param lwidth: width of grid line width
    :param columns: Dictionary of appropriate column names. Defaults are:

     .. code-block:: python

       cols = {"open": "open",
               "close": "close",
               "high": "high",
               "low": "low"
               }

    :param colors: Colors to use for candles when impulse=None (Deafault).
     First color in list is for when closing price is higher than opening
     price. Second color is for when closing price is lower than opening price.
     Default is ["green", red]
    :param impulse: Impulse system data, either "red", "green" or "blue"
    :type df: ``pandas.DataFrame()`` [``float``]
    :type ax: ``matplotlib.axes.Axes``
    :type cwidth: ``float`` or ``int``
    :type lwidth: ``float`` or ``int``
    :type columns: ``dict`` [``str``]
    :type colors: ``list`` [``str``]
    :type impulse: ``pandas.DataFrame()`` [``str``]
    """
    if columns is not None:
        cols = columns
    else:
        cols = {"open": "open",
                "close": "close",
                "high": "high",
                "low": "low"
                }

    m = len(df)
    xpos = range(m)

    if colors is not None:
        upcolor = colors[0]
        downcolor = colors[1]
    else:
        upcolor = "green"
        downcolor = "red"

    candles = []
    facecol = []
    edgecol = []

    # Build dimensions for candles and wicks and decide fill-color
    for i in range(m):
        candle_height = abs(df[cols["close"]][i] - df[cols["open"]][i])
        if df[cols["close"]][i] < df[cols["open"]][i]:
            y_pos = df[cols["close"]][i]
            wick_top_base = df[cols["open"]][i]
            wick_bottom_base = df[cols["close"]][i]
            if impulse is None:
                facecol.append(downcolor)
                edgecol.append(downcolor)
                linecol = downcolor
        else:
            y_pos = df[cols["open"]][i]
            wick_top_base = df[cols["close"]][i]
            wick_bottom_base = df[cols["open"]][i]
            if impulse is None:
                facecol.append(upcolor)
                edgecol.append(upcolor)
                linecol = upcolor

        if impulse is not None:
            if df[cols["close"]][i] < df[cols["open"]][i]:
                facecol.append('white')
            else:
                facecol.append(impulse[i])

            edgecol.append(impulse[i])
            linecol = impulse[i]

        wick_top_tip = df[cols["high"]][i]
        wick_bottom_tip = df[cols["low"]][i]

        # Build candles in the form of rectangles, append to list of candles
        candle = mpatches.Rectangle([xpos[i]-(cwidth/2), y_pos],
                                    cwidth, candle_height)
        candles.append(candle)

        # Plot wick lines
        ax.plot([xpos[i], xpos[i]], [wick_top_base, wick_top_tip],
                linestyle='-', color=linecol, linewidth=lwidth)
        ax.plot([xpos[i], xpos[i]], [wick_bottom_base, wick_bottom_tip],
                linestyle='-', color=linecol, linewidth=lwidth)

    # Make a collection from candle-rectangles and add to ax
    collection = PatchCollection(candles, facecolors=facecol,
                                 edgecolors=edgecol, linewidth=lwidth)
    ax.add_collection(collection)


def macds(df, ax, fast, signal, macdh):
    """Plot macd fast- and signal line and histogram.

    :param df: Input data frame
    :param ax: Axes instance of subplot to plot macd in
    :param figsize: Size of figure in inches
    :param fast: Name of data frame column, fast line
    :param signal: Name of data frame column, signal line
    :param macdh: Name of data frame column, macd histogram
    :type df: ``pandas.DataFrame()`` [``float``]
    :type ax: ``matplotlib.axes.Axes``
    :type fast: ``str``
    :type signal: ``str``
    :type macdh: ``str``
    """
    m = len(df)
    xpos = range(m)

    max_macdh = df[fast].max()
    min_macdh = df[fast].min()
    axis_max = max(np.abs(max_macdh), np.abs(min_macdh))
    padding = axis_max * 0.1
    ax.set_ylim(ymin=-axis_max - padding, ymax=axis_max + padding)
    ax.plot(xpos, df[fast], 'k-')
    ax.plot(xpos, df[signal], 'r--')

    # Build MACD-Histogram
    bins = []
    bin_color = []
    bin_width = 0.6

    for i in range(m):
        if df[macdh][i] < 0:
            ypos = df[macdh][i]
            bin_color.append('white')
        else:
            ypos = 0
            bin_color.append('lightblue')

        bin_height = abs(df[macdh][i])

        # Build bins in the form of rectangles, append to list of bins
        binn = mpatches.Rectangle([xpos[i]-(1/2)*bin_width, ypos],
                                  bin_width, bin_height)
        bins.append(binn)

    # Make a collection from macd-rectangles and add to ax
    collection = PatchCollection(bins, facecolors=bin_color,
                                 edgecolors='black', linewidth=1)
    ax.add_collection(collection)


def force(df, ax, force):
    """Draw force with differential coloring below and above zero.

    :param df: Input data frame
    :param ax: Axes instance of subplot to plot macd in
    :param force: Name of data frame column, force
    :type df: ``pandas.DataFrame()`` [``float``]
    :type ax: ``matplotlib.axes.Axes``
    :type force: ``str``
    """
    m = len(df)
    xpos = range(m)
    xpos_new = [xpos[0]]
    force_new = [df[force][0]]

    max_force = df[force].max()
    min_force = df[force].min()
    axis_max = max(np.abs(max_force), np.abs(min_force))
    padding = axis_max * 0.1
    ax.set_ylim(ymin=-axis_max - padding, ymax=axis_max + padding)

    ax.plot(xpos, df[force], 'k-', alpha=0.3)

    for i in range(m - 1):
        if df[force][i+1] * df[force][i] < 0:
            force_new.append(0)
            m = df[force][i+1] - df[force][i]
            x_intercept = ((m*xpos[i+1])-df[force][i+1])/m
            xpos_new.append(x_intercept)
            xpos_new.append(xpos[i+1])
            force_new.append(df[force][i+1])
        else:
            force_new.append(df[force][i+1])
            xpos_new.append(xpos[i+1])

    xpos_new.append(xpos[-1])
    force_new.append(df[force][-1])

    force_pos = np.array(force_new) >= 0
    force_neg = np.array(force_new) <= 0

    ax.fill_between(xpos_new, force_new, y2=0, where=force_pos, color='green',
                    alpha=0.3)
    ax.fill_between(xpos_new, force_new, y2=0, where=force_neg, color='red',
                    alpha=0.3)
    ax.plot(xpos, [0 for pos in xpos], "k-", alpha=0.3)


def stochs(df, ax, raw, smooth):
    """Plot stochastic.

    :param df: Input data frame
    :param ax: Axes instance of subplot to plot macd in
    :param raw: Name of data frame column, raw stachastic (%K)
    :param smooth: Name of data frame column, smoothed raw stachastic (%D)
    :type df: ``pandas.DataFrame()`` [``float``]
    :type ax: ``matplotlib.axes.Axes``
    :type raw: ``str``
    :type smooth: ``str``
    """
    m = len(df)
    xpos = range(m)
    ax.plot(xpos, df[raw], 'k-')
    ax.plot(xpos, df[smooth], 'r-')
    ax.plot(xpos, np.ones(m) * 50, '--', color='gray')
    ax.plot(xpos, np.ones(m) * 80, '-', color='gray')
    ax.plot(xpos, np.ones(m) * 20, '-', color='gray')
    ax.set_ylim(ymin=0, ymax=100)


def weekly_labels(df, dates, seperator="-", step=5):
    """Get labels and ticks appropriate for weekly plot.

    :param df: Input data frame
    :type df: ``pandas.DataFrame()`` [``float``]
    :returns: ticks and labels
    :rtype ticks: ``list`` [``int``]
    :rtype labels: ``list`` [``int``]
    """
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    raw_labels = [dates[i].split(seperator) for i in range(len(df))]
    labels = []
    ticks = []
    old_year = int(raw_labels[0][0])
    for i in range(len(raw_labels)):
        if (i + 1) % step == 0:
            new_year = int(raw_labels[i][0])
            new_month = int(raw_labels[i][1])
            if new_year > old_year:
                labels.append(str(new_year))
                old_year = new_year
            else:
                labels.append(raw_labels[i][2] + "/" + months[new_month - 1])
            ticks.append(i)
    return ticks, labels


def daily_labels(df, dates, seperator="-", step=5):
    """Get labels and ticks appropriate for weekly plot.

    :param df: Input data frame
    :type df: ``pandas.DataFrame()`` [``float``]
    :returns: ticks and labels
    :rtype ticks: ``list`` [``int``]
    :rtype labels: ``list`` [``int``]
    """
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    raw_labels = [df.index[i].split(seperator) for i in range(len(df))]
    labels = []
    ticks = []
    old_year = int(raw_labels[0][0])
    old_month = int(raw_labels[0][1])
    major_previous_tick = False
    for i in range(len(raw_labels)):
        if (i + 1) % step == 0:
            new_year = int(raw_labels[i][0])
            new_month = int(raw_labels[i][1])
            if new_year > old_year and not major_previous_tick:
                labels.append(str(new_year))
                old_year = new_year
                major_previous_tick = True
            elif new_month != old_month and not major_previous_tick and \
                    new_month != 1:
                labels.append(months[new_month - 1])
                old_month = new_month
                major_previous_tick = True
            else:
                labels.append(raw_labels[i][2])
                major_previous_tick = False
            ticks.append(i)
    return ticks, labels
