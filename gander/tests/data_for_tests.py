"""Helper functions for gander.tests.test_indicators.

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

import numpy as np
import pandas as pd


def data_format(data, m):
    """Format data for test use.

    :param data: Data array to be formatted
    :param m: Number of rows in data set
    :type data: ``numpy.array()`` [``float``]
    :type m: ``int``
    """
    columns = ['open', 'high', 'low', 'close', 'volume']
    df = pd.DataFrame(data, columns=columns)
    df['date'] = pd.date_range('2019-08-20', periods=m)
    df.set_index("date", inplace=True)
    return df


def sma_test_data(window):
    """Construct test dataframes.

    Construct test dataframes that that always, for all values - yields
    moving averages of 2.0

    :param window: Moving average window, i.e number of data points to use in
     calculation of moving average. Minimum value is 2
    :type window: ``int``
    """
    m = window * 2
    data = np.ones((m, 5))
    j = 0
    for i in range(int(m / window)):
        data[j:j + int(window / 2)] = 3
        j += int(window)
    df = pd.DataFrame(data, columns=['open', 'high', 'low', 'close', 'volume'])
    df['date'] = pd.date_range('2019-08-20', periods=m)
    df.set_index("date", inplace=True)
    return df


def ema_test_data():
    r"""Construct test data frames, to test calc_ema().

    Setting :math:`a = \frac{1}{2}` makes testing easier. Bacause :math:`a =
    \dfrac{2}{n_{sma}}` and :math:`n_{sma} = \text{window}, ~ \text{window} =
    3`
    """
    m_ones = 20
    m_decay = 13
    data_ones = np.ones((m_ones, 5))
    data_decay = np.zeros((m_decay, 5))
    data_decay[:3] = 0.5

    return data_format(data_ones, m_ones), data_format(data_decay, m_decay)


def macd_test_data():
    """Construct test data for calc_macd()."""
    m = 20
    data = np.ones((m, 5))
    data[:, -1] = data[:, -1] * 2
    return data_format(data, m)


def stoch_test_data():
    """Construct test data for calc_stoch()."""
    m = 28
    data = np.ones((m, 5))
    data[14:, -2] *= 2
    return data_format(data, m)


def impulse_test_data():
    """Construct test data for calc_impulse()."""
    m = 4
    data = np.zeros((m, 5))
    df1 = data_format(data, m)
    df2 = pd.DataFrame({"ema": [2, 3, 2, 3],
                        "macdh": [2, 3, 2, 1]}, index=df1.index)
    df = pd.concat([df1, df2], axis=1)
    return df


def force_test_data():
    """Construct test data for calc_foce()."""
    m = 4
    data = np.zeros((m, 5))
    data = data_format(data, m)
    data.loc[:, "volume"] = 10.0
    data.loc[:, "close"] = [i + 1 for i in range(m)]
    return data
