# Example rules for mapping
RULES = [
    {"color": "yellow", "pattern": "numeric", "meaning": "quantity input"},
    {"color": "blue", "pattern": "yesno", "meaning": "decision field"}
]

def match_rule(color, text):
    if color == "yellow" and any(c.isdigit() for c in text):
        return "quantity input"
    elif color == "blue" and text.lower() in ["yes", "no"]:
        return "decision field"
    return "unknown"
