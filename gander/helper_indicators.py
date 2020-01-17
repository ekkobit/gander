"""Helper functions for gander.indicators.

Copyright (C) 2020  Ekkobit AS

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Questions may be directed to resonate@ekkobit.com
"""


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
