"""Safety package for blupblup — disclaimer and kill switch."""

from safety.disclaimer import show_disclaimer
from safety.killswitch import install_killswitch

__all__ = ["show_disclaimer", "install_killswitch"]
