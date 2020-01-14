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
