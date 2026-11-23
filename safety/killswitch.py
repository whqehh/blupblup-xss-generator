"""
Kill switch — clean Ctrl+C handling.

Installs a SIGINT handler so that Ctrl+C exits with code 130 instead of
throwing an unhandled traceback. Any in-memory partial results should be
flushed by the caller if needed (the generator is fast enough here that
partial state is not meaningful).
"""

import signal
import sys


def _handle_sigint(signum, frame):
    print("\n[!] Interrupted by user. Exiting cleanly.")
    sys.exit(130)


def install_killswitch() -> None:
    """Install a SIGINT handler that exits cleanly with code 130."""
    signal.signal(signal.SIGINT, _handle_sigint)
