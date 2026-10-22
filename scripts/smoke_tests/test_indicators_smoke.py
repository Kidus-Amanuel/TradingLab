"""Smoke Test 2: Indicator Computation.

Verifies calculation of EMA (Exponential Moving Average) and ATR (Average True Range).
Supports pandas-ta-classic or native pandas/numpy fallback.
"""

import sys

def run_smoke_test() -> None:
    print("[SMOKE TEST 2] Verifying Indicator Engine...")
    try:
        import pandas as pd
        import numpy as np
    except ImportError:
        print("FAIL: 'pandas' or 'numpy' is not installed in the current environment.")
        print("In Phase 1, dependencies will be installed inside the isolated .venv.")
        sys.exit(1)

    # Synthetic sample OHLCV dataset
    data = {
        "open":  [100, 102, 101, 103, 105, 104, 106, 108, 107, 109, 111, 110, 112, 115, 114],
        "high":  [103, 104, 103, 106, 107, 106, 109, 110, 109, 112, 113, 112, 116, 118, 116],
        "low":   [ 99, 100,  99, 101, 103, 102, 104, 106, 105, 107, 109, 108, 111, 113, 112],
        "close": [102, 101, 103, 105, 104, 106, 108, 107, 109, 111, 110, 112, 115, 114, 116],
        "volume":[500, 600, 550, 700, 800, 650, 900, 850, 750, 950,1000, 900,1100,1200,1050],
    }
    df = pd.DataFrame(data)

    try:
        # Check if pandas_ta is available
        import pandas_ta as ta  # type: ignore
        df["ema_5"] = ta.ema(df["close"], length=5)
        df["atr_5"] = ta.atr(df["high"], df["low"], df["close"], length=5)
        engine_used = "pandas_ta"
    except (ImportError, Exception):
        # Native pandas mathematical fallback
        df["ema_5"] = df["close"].ewm(span=5, adjust=False).mean()
        high_low = df["high"] - df["low"]
        high_close = (df["high"] - df["close"].shift()).abs()
        low_close = (df["low"] - df["close"].shift()).abs()
        tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        df["atr_5"] = tr.rolling(5).mean()
        engine_used = "native pandas fallback"

    latest_close = df["close"].iloc[-1]
    latest_ema = df["ema_5"].iloc[-1]
    latest_atr = df["atr_5"].iloc[-1]

    print(f"SUCCESS: Calculated indicators using [{engine_used}].")
    print(f"  Latest Close: {latest_close:.2f}")
    print(f"  5-Period EMA: {latest_ema:.2f}")
    print(f"  5-Period ATR: {latest_atr:.2f}")
    
    assert not np.isnan(latest_ema), "EMA computation resulted in NaN"
    assert not np.isnan(latest_atr), "ATR computation resulted in NaN"
    print("PASS: Indicator smoke test completed successfully.")

if __name__ == "__main__":
    run_smoke_test()
