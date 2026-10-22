"""Smoke Test 1: CCXT Public Market Data Fetch.

Verifies that CCXT can connect to exchange public endpoints and retrieve
historical OHLCV candle data without requiring API keys or authentication.
"""

import sys

def run_smoke_test() -> None:
    print("[SMOKE TEST 1] Verifying CCXT market data ingestion...")
    try:
        import ccxt
    except ImportError:
        print("FAIL: 'ccxt' is not installed in the current environment.")
        print("In Phase 1, it will be installed inside the isolated .venv.")
        sys.exit(1)

    # Initialize public Binance client (no credentials needed for public OHLCV)
    exchange = ccxt.binance({
        "enableRateLimit": True,
        "timeout": 10000,
    })

    symbol = "BTC/USDT"
    timeframe = "1h"
    limit = 5

    try:
        print(f"Fetching last {limit} bars of {symbol} ({timeframe}) from Binance...")
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        
        if not ohlcv or len(ohlcv) == 0:
            print("FAIL: Received empty candle response.")
            sys.exit(1)

        print(f"SUCCESS: Received {len(ohlcv)} candles.")
        print("Sample latest candle [Timestamp, Open, High, Low, Close, Volume]:")
        print(f"  {ohlcv[-1]}")
        print("PASS: CCXT smoke test completed successfully.")
    except Exception as exc:
        print(f"FAIL: CCXT query failed: {exc}")
        sys.exit(1)

if __name__ == "__main__":
    run_smoke_test()
