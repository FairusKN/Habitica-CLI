"""
Entry Point of this program.
"""

import sys

if __name__ == "__main__":
    try:
        from cli import core

        core()
    except KeyboardInterrupt:
        print("\n🛑 Interrupted by user.")
        sys.exit(0)
