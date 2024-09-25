import numpy as np


def _sma(window_size, ticks_frame, column):
    ticks_frame[f'SMA{window_size}'] = ticks_frame[column].rolling(window_size).mean()
    ticks_frame.dropna(inplace=True) # Drop null values
    print(ticks_frame)
    return ticks_frame


def detect_crossover(df, fastPeriod=20, slowPeriod=50):
    df['fast_sma'] = df['close'].rolling(fastPeriod).mean()
    df['slow_sma'] = df['close'].rolling(slowPeriod).mean()
    df.dropna(inplace=True)
    # df['prev_fast_sma'] = df['fast_sma'].shift(1)

    df['crossover'] = np.vectorize(find_crossover)(df['fast_sma'], df['slow_sma'])
    # bullish_signal = df[df['crossover'] == 'bullish crossover'].copy()
    # bearish_signal = df[df['crossover'] == 'bearish crossover'].copy()
    crossover = df.iloc[-1]['crossover']
    # print (df.iloc[-1])
    if crossover == 'bullish crossover':
        return df, "bullish"
    elif crossover == 'bearish crossover':
        return df, "bearish"
    else:
        return df, None

def find_crossover(fast_sma, slow_sma):
    if fast_sma > slow_sma and (fast_sma - slow_sma) <= 0.05:
        return 'bearish crossover'
    elif fast_sma < slow_sma and (slow_sma - fast_sma) <= 0.05:
        return 'bullish crossover'

    return None

