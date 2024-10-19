import numpy as np
import logging

from Domain import Given

logger = logging.getLogger(__name__)


def _sma(window_size, ticks_frame, column):
    ticks_frame[f'SMA{window_size}'] = ticks_frame[column].rolling(window_size).mean()
    ticks_frame.dropna(inplace=True)  # Drop null values
    logging.debug(ticks_frame)
    return ticks_frame


def in_consolidation(given: Given):
    df = given.__dict__.get("df")
    return (round(abs(df['fast_sma'] - df['slow_sma']), 1) <= 0.05).all()


def calculate_consolidation_range(given: Given):
    df = given.__dict__.get("df")
    last_x_rows = df.copy().tail(9)
    last_x_rows['high_low_diff'] = last_x_rows['high'] - last_x_rows['low']
    cr = last_x_rows['high_low_diff'].mean()
    given.add("consolidation_range", cr)
    return cr


def calculate_sma(given: Given, sma_name, period):
    df = given.__dict__.get("df")
    df[sma_name] = df['close'].rolling(period).mean()
    df.dropna(inplace=True)


def is_bearish_crossover(given: Given):
    df = given.__dict__.get("df")
    crossover = df.iloc[-1]['crossover']
    return crossover == 'bearish crossover'


def is_bullish_crossover(given: Given):
    df = given.__dict__.get("df")
    crossover = df.iloc[-1]['crossover']
    return crossover == 'bullish crossover'


def detect_crossover(given: Given, fast_sma='fast_sma', slow_sma='slow_sma'):
    df = given.__dict__.get("df")
    df['crossover'] = np.vectorize(_find_crossover)(df[fast_sma], df[slow_sma])


def _find_crossover(fast_sma, slow_sma):
    if fast_sma > slow_sma and (fast_sma - slow_sma) > 0.05:  # SMA 20 > SMA 50
        return 'bullish crossover'
    elif fast_sma < slow_sma and (slow_sma - fast_sma) > 0.05:  # SMA 20 < SMA 50
        return 'bearish crossover'

    return None


def detect_consolidation(fast_sma, slow_sma):
    if abs(fast_sma - slow_sma) <= 0.02:
        return 'consolidation'

    return None
