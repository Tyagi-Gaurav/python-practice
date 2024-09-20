
def sma(window_size, ticks_frame, column):
    ticks_frame[f'SMA{window_size}'] = ticks_frame[column].rolling(window_size).mean()
    ticks_frame.dropna(inplace=True) # Drop null values
    # print(ticks_frame)
    return ticks_frame


def detect_crossover(df, colA, colB):
    df['sma_delta'] = df[colA] - df[colB]
    row = df.loc[df.sma_delta == df.sma_delta.min()]

    if row['sma_delta'].count() >= 1:
        sma_delta = row.iloc[0]['sma_delta']
        sma_20 = row.iloc[0]['SMA20']
        sma_50 = row.iloc[0]['SMA50']
        print (f"SMA 20: {sma_20}, SMA 50: {sma_50}, sma_delta: {sma_delta}")
        if round(abs(sma_delta), 4) <= 0.0001:
            print(f"{colA} going under {colB} at")
            print(row)
            return True
    return False
