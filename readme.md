# blupblup — XSS Payload Generator

A context-aware Cross-Site Scripting (XSS) payload generation tool for **authorized security testing and education**.

> ⚠️ **This tool generates payload strings only.** It does NOT send requests to any target, does NOT scan websites, and does NOT exploit anything. It is a payload *crafting* utility.

**Course:** Ethical Hacking (IKB31603)
**Institution:** UniKL MIIT
**Attack Category:** Web Application Attack (XSS Payload Generator)
**Team:** Nurul Izzany, Nureen Farhah, Adam Borhan, Muhammad Syakirin

---

## 1. Tool Description

`blupblup` generates context-aware XSS payloads with multiple encoding/obfuscation variants. Users select an injection context (e.g., inside `<script>`, inside a double-quoted attribute, inside a JS string) and the tool produces payloads tailored to break out of that context.

All output is saved **locally** to the `output/` directory. No network communication occurs.

### Features
- Context-aware payload generation (5 contexts)
- Encoding variants: raw, HTML entities, URL encoding, Base64, hex
- Customizable output count
- `--dry-run` preview mode
- Local-only output with timestamped filenames
- Kill switch (Ctrl+C) with clean exit
- Legal disclaimer + authorization confirmation gate

---

## 2. Attack Lifecycle Mapping

| Phase | How blupblup fits |
|---|---|
| **Reconnaissance** | Tester identifies candidate injection points (manually, or with authorized tools) |
| **Weaponization** | blupblup generates context-appropriate payloads for each candidate point |
| **Delivery** | Tester manually injects payloads into an **authorized** test environment (e.g., local DVWA) |
| **Exploitation / Verification** | Tester observes whether payload executes (e.g., `alert(1)` popup) |
| **Reporting** | Findings documented and disclosed responsibly |

> blupblup covers the **Weaponization** phase. It is intentionally not an automated scanner.

---

## 3. Installation

**Requires Python 3.10+**

```bash
git clone https://github.com/<your-username>/blupblup-xss-generator.git
cd blupblup-xss-generator
pip install -r requirements.txt
