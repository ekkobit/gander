It's commonplace to use EMAs to analyze market trends. It is, however, not
a very sensitive indicator.  MACD, or Moving Average Convergence Divergence, uses
the difference between two EMAs to create a more sensitive indicator. A MACD
indicator usually consists of two lines, a fast line, a signal line and a
histogram. The fast line is the difference between two EMAs of closing prices,
usually EMAs with :math:`n_{sma} = 12` and :math:`n_{sma} = 26` - often referred
to as a 12 -and a 26 period EMA, though mathematically speaking, EMAs don't
really have periods. They are created from approximations of
infinite series, as explained in the section on :ref:`ema`.
The signal line is an EMA of the fast line, usually with :math:`n_{sma} = 9` and
the histogram is simply the difference between the fast line and the signal
line. So there you have it:

.. math::
    \begin{align}
      \mathit{MACD}_{fast} &= \mathit{EMA}_{12} - \mathit{EMA}_{26} \\
      \mathit{MACD}_{signal} &= \mathit{EMA}_{9}(\mathit{MACD}_{fast}) \\
      \mathit{MACD}_{histogram} &= \mathit{MACD}_{fast} - \mathit{MACD}_{signal}
    \end{align}

How to read MACD
----------------

- When the fast line crosses over the signal line a bullish trend is likely
  ahead. Buy long and place stop below latest bottom.

- When the fast line crosses below the signal line a bearish trend is likely
  ahead. Buy long and place stop below latest top.

- The MACD histogram also gives buy and sell signals, but is better for long
  term charts, like weekly charts. On daily charts buy signals come flying left
  and right. MACD histogram is actually an oscillator, but we include it here
  as a matter of heritage. It's so closely linked to the MACD fast -and signal
  line.

    - Buy when histogram stops falling and starts rising. Place stop below last
      bottom.

    - Sell short when histogram stops rising and starts falling. Place stop
      above last top.

    - A three month record high histogram, signals prices are likely to rise
      even higher.

    - A three month record low histogram, signals prices are likely to fall even
      lower.

    - A new histogram high during uptrend signals good uptrend health.

    - A new histogram low during downtrend signals good downtrend health.

    - Price going one way and MACD histogram the other, signals a trend is not
      as strong as it seems, e.g prices go up but histogram falls.
