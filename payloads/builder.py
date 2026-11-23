"""
Context-aware payload builder.
Picks a template from the database and substitutes the action placeholder.
"""

from payloads.database import PAYLOAD_DB


def build_payload(context: str, action: str, variant_index: int = 0) -> str:
    """
    Build a raw (unencoded) payload for the given context and action.

    :param context: One of html_tag, attr_dq, attr_sq, js_string, url_href
    :param action:  JS function to invoke (e.g., 'alert')
    :param variant_index: Which template to use (wraps around)
    :return: Raw payload string
    :raises ValueError: if context is unknown
    """
    if context not in PAYLOAD_DB:
        raise ValueError(f"Unknown context: {context}")

    templates = PAYLOAD_DB[context]
    template = templates[variant_index % len(templates)]
    return template.format(action=action)
