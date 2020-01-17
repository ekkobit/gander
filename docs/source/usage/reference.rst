.. Gander function reference.

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

#########
Reference
#########

Gander is a python library aimed at technical analysis of securities markets,
such as the stock market. Gander contains functions for creating popular
technical indicators, as well as plotting functions. Plotting functions are
built using the Matplotlib library.

===================================================
Adding technical indicators to a Pandas DataFrame
===================================================

.. role:: python(code)
    :language: python

Simple Moving Average (SMA)
---------------------------

.. autofunction:: gander.indicators.calc_sma

Exponential Moving Average (EMA)
--------------------------------

.. autofunction:: gander.indicators.calc_ema

Moving Average Convergence Divergence (MACD)
--------------------------------------------

.. autofunction:: gander.indicators.calc_macd

Stochastic Oscillator (STOCH)
-----------------------------

.. autofunction:: gander.indicators.calc_stoch

Impulse System
--------------

.. autofunction:: gander.indicators.calc_impulse

Force Index Oscillator
----------------------

.. autofunction:: gander.indicators.calc_force

True Range (TR)
---------------

.. autofunction:: gander.indicators.calc_tr

========
Plotting
========

Candlesticks
------------

.. autofunction:: gander.plotting.candles

MACD
----

.. autofunction:: gander.plotting.macds

Force Index
-----------

.. autofunction:: gander.plotting.force

Stochastic Oscillator
---------------------

.. autofunction:: gander.plotting.stochs
