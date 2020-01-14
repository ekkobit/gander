"""Tests for ``gander.indicators`` module."""

from .. indicators import calc_sma, calc_ema, calc_macd, calc_stoch, \
    calc_impulse, calc_force
from . data_for_tests import sma_test_data, ema_test_data, \
    macd_test_data, stoch_test_data, impulse_test_data, force_test_data
import pytest


@pytest.fixture(scope='class', params=[2, 6, 10])  # params even numbers
def sma_fix(request):
    """Set up for testing using special test data frames.

    :param request: Access to parameters defined in pytest fixture
     ``sma_fix()``
    :type requests: ``pytest.FixtureRequest`` [int]
    """
    df = sma_test_data(request.param)
    window = request.param
    yield df, window


class TestSmaFix:
    """Tests that use ``pytest.Fixture`` ``sma_fix``."""

    def test_sma(self, sma_fix):
        """Test ``gander.indicators.calc_sma()``.

        :param sma_fix: Callable to test helpers defined in pytest fixture
        ``sma_fix()``
        :type sma_fix: ``pytest.Fixture()``
        """
        df, window = sma_fix
        new_column_name = "sma" + str(window - 1) + "_close"
        df_sma = calc_sma(df, window, "close", new_column_name)
        # Input df is constructed in a way that always gives a moving average
        # of 2.0. Check that all data frame values are 2.0
        assert (df_sma[new_column_name][(window) - 1:] == 2.0).all()


@pytest.fixture(scope='function')
def ema_fix():
    """Set up ema testing using special test data frames."""
    df_ones, df_decay = ema_test_data()
    return df_ones, df_decay


def test_ema(ema_fix):
    """Test ``gander.indicators.calc_ema()``.

    :param sma_fix: Callable to test helpers defined in pytest fixture
    ``ema_fix()``
    """
    df_ones, df_decay = ema_fix
    window = 3
    new_column_name = "ema" + str(window - 1) + "_close"
    df_ema_ones = calc_ema(df_ones, df_ones["close"], new_column_name,
                           window=window, custom_a=0.5)
    df_ema_decay = calc_ema(df_decay, df_decay["close"], new_column_name,
                            window=window, custom_a=0.5)

    # Test on ones - no decay
    assert (df_ema_ones[new_column_name].dropna() == 1).all()
    # Test exponential decay
    ema_decay = df_ema_decay[new_column_name].dropna().values
    for i in range(ema_decay.shape[0] - 1):
        assert (ema_decay[i + 1] ==
                ema_decay[i] / 2).all()


@pytest.fixture(scope='function')
def macd_fix():
    """Set up macd testing using special test data frame."""
    df = macd_test_data()
    return df


def test_macd(macd_fix):
    """Test ``gander.indicators.calc_macd()``.

    :param macd_fix: Callable to test helpers defined in pytest fixture
    ``macd_fix()``
    """
    df = macd_fix
    df = calc_ema(df, df["close"], "ema_3", window=4)
    df = calc_ema(df, df["volume"], "ema_2", window=3)
    df = calc_macd(df, df["ema_2"], df["ema_3"])
    assert (df["macd-h"].dropna() == 0.0).all()


@pytest.fixture(scope='function')
def stoch_fix():
    """Set up stoch testing using special test data frame."""
    df = stoch_test_data()
    return df


def test_stoch(stoch_fix):
    """Test ``gander.indicators.calc_stoch()``.

    :param macd_fix: Callable to test helpers defined in pytest fixture
    ``macd_fix()``
    """

    df = stoch_fix
    df_out = calc_stoch(df)
    assert (df_out["%K"].dropna() == 100.0).all()
    assert (df_out["%D"].dropna() == 100.0).all()


@pytest.fixture(scope='function')
def impulse_fix():
    """Set up impulse testing using special test data frame."""
    df = impulse_test_data()
    return df


def test_impulse(impulse_fix):
    """Test ``gander.indicators.impulse()``.

    :param impulse_fix: Callable to test helpers defined in pytest fixture
    ``macd_fix()``
    """

    df = impulse_fix
    df_out = calc_impulse(df, "ema", "macdh")
    assert list(df_out["impulse"].dropna().values) == ["green", "red", "blue"]


@pytest.fixture(scope='function')
def force_fix():
    """Set up force testing using special test data frame."""
    df = force_test_data()
    return df


def test_force(force_fix):
    """Test ``gander.indicators.force()``.

    :param force_fix: Callable to test helpers defined in pytest fixture
    ``macd_fix()``
    """

    df = force_fix
    df_out = calc_force(df, "close", "volume")
    print("\n\n", df_out)
    assert list(df_out["force"].dropna().values) == [10.0, 10.0, 10.0]
