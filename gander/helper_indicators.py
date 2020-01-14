"""Helper functions for gander.indicators."""


def pick_columns(df, window, indicator, columns):
    """Set up a data frame of raw data to do calculations on.

    :param df: Input data frame
    :param window: Number of data points to use in average
    :param indicator: Abbriviated name of indicator, e.g `sma`
    :param columns: which columns in data frame to perform calculations on
    :type df: ``pandas.DataFrame()`` [``float``]
    :type window: ``int``
    :type indicator: ``str``
    :type columns: ``list`` [``str`` or ``None``]
    """
    if columns is not None:
        df_raw = df[columns]
        col_names = [indicator + '_' + name + '_' + str(window) for name in
                     list(columns)]
    else:
        df_raw = df.loc[:, 'open':'volume']
        col_names = [indicator + '_' + name + '_' + str(window) for name in
                     list(df_raw.columns)]

    return df_raw, col_names
