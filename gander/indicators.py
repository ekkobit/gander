"""Popular indicators for stock data."""

import pandas as pd
import numpy as np


def calc_sma(df, window, column, new_column_name):
    """Calculate simple moving averages.

    Calculate SMA for data frame columns and expand data
    frame with simple moving averages.

    :param df: Input/output data frame
    :param window: Number of data points to use in moving average
    :param column: which columns in data frame to perform calculations on
    :param trim: Whether or not to trim NaN values
    :type df: ``pandas.DataFrame()`` [``float``]
    :type window: ``int``
    :type column: ``str``
    :returns: Input dataframe with added sma column
    :rtype: ``pandas.DataFrame()`` [``float``]
    """
    df[new_column_name] = df[column].rolling(window).mean()
    return df


def calc_ema(df, column, new_column_name, window=10, custom_a=None):
    r"""Calculate exponential moving average.

    :param df: Input data frame
    :param window: Number of data points to use in average
    :param column: One column dataframe to perform calculations on
    :param new_column_name: Name for new column of ema
    :param custom_a: Custom a for the geometric series
     :math:`a + ar + ar^2 + ... + ar^{n - 1}`.
    :type df: ``pandas.DataFrame()`` [``float``]
    :type window: ``int``
    :type column: ``pandas.DataFrame()`` [``float``]
    :type new_column_name: ``str``
    :type custom_a: ``float``
    :returns: Input dataframe with added ema column
    :rtype: ``pandas.DataFrame()`` [``float``]
    """
    a = custom_a if custom_a is not None else 2 / (window)
    data = column.dropna()
    old_ema = np.mean(data[:window])
    ema_values = [old_ema]

    for i in range(len(data) - window):
        price = data[i + window]
        ema = a * price + (1 - a) * old_ema
        ema_values.append(ema)
        old_ema = ema

    diff = len(df) - len(data)
    new_df = pd.DataFrame(ema_values, columns=[new_column_name],
                          index=df.index[diff + window - 1:])
    df = pd.concat([df, new_df], axis=1, sort=True)

    return df


def calc_macd(df, ema_short, ema_long, window=9):
    """Create MACD fast-, signal line and Histogram from short and long EMAs.

    :param df: Input data frame
    :param ema_short: Short term EMA data
    :param ema_long: Long term EMA data
    :type df: ``pandas.DataFrame()`` [``float``]
    :type ema_short: ``pandas.DataFrame()`` [``float``]
    :type ema_long: ``pandas.DataFrame()`` [``float``]
    :returns: Input dataframe with added macd columns
    :rtype: ``pandas.DataFrame()`` [``float``]
    """
    df['fast'] = ema_short - ema_long
    df = calc_ema(df, df["fast"], "signal", window=window)
    df['macd-h'] = df['fast'] - df['signal']
    return df


def calc_stoch(df, stoch_window=15, ema_window=4):
    """Add two columns to the dataframe, a %K and a %D line.

    :param df: Data frame to do and add calculations to
    :param stoch_window: Number of data points in the stochastic, including
     current data point.
    :param ema_window: number data points in ema smoothing of %K, %D ---
     including current data point
    :type df: ``pandas.DataFrame()`` [``float``]
    :type stoch_window: ``int``
    :type ema_window: ``int``
    :returns: Input dataframe with added stochastic columns
    :rtype: ``pandas.DataFrame()`` [``float``]
    """
    data = df.copy()
    highs = data["close"].rolling(stoch_window).max()
    lows = df.loc[:, "open":"close"].rolling(stoch_window).min().min(axis=1)
    data["%K"] = ((data["close"] - lows) / (highs - lows)) * 100
    data = calc_ema(data, data["%K"], "%D", window=ema_window)
    data = calc_ema(data, data["%D"], "%%D", window=ema_window)
    return data


def calc_impulse(df, ema, macdh):
    """Calculate color according to the impulse system by Elder.

    :param df: Data frame to do and add calculations to
    :param ema: Pandas dataframe column. Normally ema13.
    :param macd-h: Pandas dataframe column
    :type ema: ``str``
    :type macdh: ``str``
    :type df: ``pandas.DataFrame()`` [``float``]
    :returns: Input dataframe with added impulse column
    :rtype: ``pandas.DataFrame()`` [``float``]
    """
    data = df[[ema, macdh]].dropna()
    impulse = []
    for i in range(len(data) - 1):
        if data[ema][i+1] > data[ema][i] and data[macdh][i+1] > data[macdh][i]:
            impulse.append("green")
        elif data[ema][i+1] < data[ema][i] \
                and data[macdh][i+1] < data[macdh][i]:
            impulse.append("red")
        else:
            impulse.append("blue")

    df_impulse = pd.DataFrame({"impulse": impulse}, index=data.index[1:])
    df_out = pd.concat([df, df_impulse], axis=1, sort=True)

    return df_out


def calc_force(df, close, volume, col_name="force"):
    """Calculate force indicator (Elder).

    :param df: Data frame to do and add calculations to
    :param close: Pandas dataframe column name close price
    :param volume: Pandas dataframe column name volume
    :param col_name: Pandas dataframe column name for new force calculations
    :type df: ``pandas.DataFrame()`` [``float``]
    :type close: ``str``
    :type volume: ``str``
    :type col_name: ``str``
    :returns: Input dataframe with added force column
    :rtype: ``pandas.DataFrame()`` [``float``]
    """
    df[col_name] = df[close].diff() * df[volume]
    return df


def calc_tr(df, high, low, close, col_name="tr"):
    """Calculate True Range.

    :param df: Data frame to do and add calculations to
    :param high: Pandas dataframe column name high price
    :param low: Pandas dataframe column name low price
    :param close: Pandas dataframe column name close price
    :param col_name: Pandas dataframe column name for new tr calculations.
     Default "tr"
    :type df: ``pandas.DataFrame()`` [``float``]
    :type high: ``str``
    :type low: ``str``
    :type close: ``str``
    :type col_name: ``str``
    :returns: Input dataframe with added force column
    :rtype: ``pandas.DataFrame()`` [``float``]
    """
    tr = [np.nan]

    for i in range(len(df) - 1):
        high_low = abs(df[high][i + 1] - df[low][i + 1])
        high_last_close = abs(df[high][i + 1] - df[close][i])
        low_last_close = abs(df[low][i + 1] - df[close][i])
        tr.append(max([high_low, high_last_close, low_last_close]))
    df[col_name] = tr
    return df
