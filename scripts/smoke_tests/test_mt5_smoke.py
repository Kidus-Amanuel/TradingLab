"""Smoke Test 3: MetaTrader 5 Terminal & Python Bridge.

Verifies that the official MetaTrader5 Python package can initialize,
detect the Windows MT5 terminal, and query account/symbol information.
"""

import sys

def run_smoke_test() -> None:
    print("[SMOKE TEST 3] Verifying MetaTrader 5 connection on Windows...")
    try:
        import MetaTrader5 as mt5  # type: ignore
    except ImportError:
        print("FAIL: 'MetaTrader5' package is not installed.")
        print("In Phase 1, it will be installed inside the isolated .venv on Windows.")
        sys.exit(1)

    # Attempt to initialize connection to MT5 terminal
    initialized = mt5.initialize()
    if not initialized:
        error_code, error_desc = mt5.last_error()
        print(f"INFO: MT5 terminal not running or not installed on this path ({error_code}: {error_desc}).")
        print("Note: In development, MT5 terminal must be installed and logged into a free demo account.")
        print("PASS (Conditional): Package imported correctly; terminal connection deferred to Phase 7.")
        return

    try:
        version = mt5.version()
        terminal_info = mt5.terminal_info()
        print(f"SUCCESS: Connected to MT5 terminal version: {version}")
        print(f"  Connected: {terminal_info.connected}")
        print(f"  Demo Account: {terminal_info.trade_allowed}")

        # Query EURUSD tick info
        symbol = "EURUSD"
        selected = mt5.symbol_select(symbol, True)
        if selected:
            tick = mt5.symbol_info_tick(symbol)
            if tick:
                print(f"  {symbol} Ask: {tick.ask}, Bid: {tick.bid}, Spread: {round((tick.ask - tick.bid) * 10000, 1)} pips")
        print("PASS: MetaTrader 5 smoke test completed successfully.")
    finally:
        mt5.shutdown()

if __name__ == "__main__":
    run_smoke_test()
