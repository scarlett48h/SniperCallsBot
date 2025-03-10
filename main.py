import os
import webbrowser
import contextlib
import io
import time
import threading

from src.http import server
from src.core import TradingCore

CONFIG = "config.ini"
PORT = 8000

def run_server():
    with contextlib.redirect_stdout(io.StringIO()):
        with contextlib.redirect_stderr(io.StringIO()):
            server.run(port=PORT, debug=False, use_reloader=False, use_debugger=False, use_evalex=False, passthrough_errors=True)

if __name__ == '__main__':
    trading_core = TradingCore(CONFIG)
    trading_core.start_trading()
    print(f"Click with pressed Ctrl key on this link: http://127.0.0.1:{PORT}")
    print(f"Also, you can copy and paste this link in your browser")
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    time.sleep(1)
    webbrowser.open(f"http://127.0.0.1:{PORT}", new = 2)
    threading.Event().wait()