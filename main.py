#!/usr/bin/env python3
"""
blupblup XSS Payload Generator
Authorized security testing and educational use only.

Entry point: parses CLI arguments, shows legal disclaimer, dispatches to
payload builder + encoder, and writes output locally when requested.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

from payloads.builder import build_payload
from payloads.encoder import ENCODERS
from safety.disclaimer import show_disclaimer
from safety.killswitch import install_killswitch

CONTEXTS = ["html_tag", "attr_dq", "attr_sq", "js_string", "url_href"]
ACTIONS = ["alert", "confirm", "prompt"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="blupblup",
        description="XSS Payload Generator — for authorized security testing only.",
        epilog=(
            "Examples:\n"
            "  python main.py --context html_tag --action alert --count 3 --output\n"
            "  python main.py --context attr_dq --action alert --encode url\n"
            "  python main.py --help\n"
            "This tool generates payload strings ONLY. It does not send requests to any target."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--context", choices=CONTEXTS, default="html_tag",
                        help="Injection context (default: html_tag)")
    parser.add_argument("--action", choices=ACTIONS, default="alert",
                        help="JS action to invoke (default: alert)")
    parser.add_argument("--encode", choices=list(ENCODERS.keys()), default="raw",
                        help="Encoding variant (default: raw)")
    parser.add_argument("--count", type=int, default=1,
                        help="Number of payload variants to generate (default: 1)")
    parser.add_argument("--output", action="store_true",
                        help="Save payloads to output/ directory")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview only — do not write files")
    return parser.parse_args()


def generate(context: str, action: str, encode: str, count: int) -> list[str]:
    encoder = ENCODERS[encode]
    from payloads.database import PAYLOAD_DB
    available = len(PAYLOAD_DB[context])
    if count > available:
        print(f"[i] Only {available} unique variants exist for context '{context}'. "
              f"Generating {available} instead of {count}.")
        count = available
    return [encoder(build_payload(context, action, variant_index=i)) for i in range(count)]


def save_output(payloads: list[str], context: str, encode: str, action: str) -> Path:
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    path = output_dir / f"{stamp}_payloads.json"
    data = {
        "tool": "blupblup",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "context": context,
        "action": action,
        "encoding": encode,
        "payloads": payloads,
    }
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


def main() -> int:
    args = parse_args()

    if not show_disclaimer():
        print("[!] Authorization not confirmed. Exiting.")
        return 1

    install_killswitch()

    if args.count < 1 or args.count > 100:
        print("[!] --count must be between 1 and 100.")
        return 1

    try:
        payloads = generate(args.context, args.action, args.encode, args.count)
    except KeyboardInterrupt:
        print("\n[!] Interrupted. Exiting cleanly.")
        return 130

    print(f"\n[+] Generated {len(payloads)} payload(s) "
          f"(context={args.context}, encoding={args.encode}):\n")
    for i, p in enumerate(payloads, 1):
        print(f"  {i}. {p}")

    if args.dry_run:
        print("\n[dry-run] No files written.")
        return 0

    if args.output:
        path = save_output(payloads, args.context, args.encode, args.action)
        print(f"\n[+] Saved to {path}")
    else:
        print("\n[i] Payloads not saved. Use --output to save to output/ directory.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
