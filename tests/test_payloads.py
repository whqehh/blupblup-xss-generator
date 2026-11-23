"""
Basic test matrix for blupblup.

Run directly:
    python tests/test_payloads.py
Or with pytest:
    pytest tests/
"""

import sys
from pathlib import Path

# Make repo root importable when running this file directly
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from payloads.builder import build_payload
from payloads.encoder import ENCODERS
from payloads.database import PAYLOAD_DB


def test_all_contexts_generate():
    for context in PAYLOAD_DB:
        p = build_payload(context, "alert", 0)
        assert isinstance(p, str) and len(p) > 0, f"empty payload for {context}"
    print("[PASS] All contexts generate a payload")


def test_all_encoders_return_string():
    raw = "<script>alert(1)</script>"
    for name, fn in ENCODERS.items():
        out = fn(raw)
        assert isinstance(out, str) and len(out) > 0, f"encoder {name} failed"
    print("[PASS] All encoders return non-empty output")


def test_url_encoder_angle_brackets():
    out = ENCODERS["url"]("<script>")
    assert "%3C" in out and "%3E" in out
    print("[PASS] URL encoder encodes angle brackets")


def test_base64_encoder_wraps_eval():
    out = ENCODERS["base64"]("alert(1)")
    assert out.startswith("eval(atob(")
    print("[PASS] Base64 encoder wraps in eval(atob(...))")


def test_html_entity_encoder():
    out = ENCODERS["html"]("<>")
    assert out == "&#60;&#62;"
    print("[PASS] HTML entity encoder converts < and >")


def test_hex_encoder():
    out = ENCODERS["hex"]("A")
    assert out == "\\x41"
    print("[PASS] Hex encoder produces \\x41 for 'A'")


def test_invalid_context_raises():
    try:
        build_payload("does_not_exist", "alert", 0)
        assert False, "expected ValueError"
    except ValueError:
        print("[PASS] Invalid context raises ValueError")


def test_action_substitution_literal():
    p = build_payload("html_tag", "confirm", 0)
    assert "confirm" in p
    print("[PASS] Action name is substituted literally")


def test_variant_index_wraps():
    n = len(PAYLOAD_DB["html_tag"])
    a = build_payload("html_tag", "alert", 0)
    b = build_payload("html_tag", "alert", n)  # wraps back to 0
    assert a == b
    print("[PASS] variant_index wraps around template list")


if __name__ == "__main__":
    test_all_contexts_generate()
    test_all_encoders_return_string()
    test_url_encoder_angle_brackets()
    test_base64_encoder_wraps_eval()
    test_html_entity_encoder()
    test_hex_encoder()
    test_invalid_context_raises()
    test_action_substitution_literal()
    test_variant_index_wraps()
    print("\nAll tests passed.")
