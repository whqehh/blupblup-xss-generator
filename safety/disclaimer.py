"""
Legal disclaimer and authorization confirmation gate.
"""

DISCLAIMER = """
============================================================
  blupblup — XSS Payload Generator
============================================================
  WARNING: This tool is for AUTHORIZED security testing
  and educational use ONLY.

  Unauthorized use against systems you do not own or have
  written permission to test may violate the
  Computer Crimes Act 1997 (Malaysia) and similar laws
  in other jurisdictions.

  This tool generates payload strings locally. It does NOT
  send any requests to any target.

  The authors assume NO liability for misuse.
============================================================
"""


def show_disclaimer() -> bool:
    """
    Show the legal disclaimer and require explicit confirmation.
    Returns True if the user confirms authorization, False otherwise.
    """
    print(DISCLAIMER)
    response = input(
        "Do you confirm you have explicit written authorization "
        "for the target environment? (yes/no): "
    ).strip().lower()
    return response == "yes"
