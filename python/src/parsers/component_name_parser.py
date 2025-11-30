import re

def parse_component_name(react_code):
    """
    Extract the React component name from a function component like:
    function TodoList() {
    """
    match = re.search(r"function\s+(\w+)\s*\(", react_code)
    if match:
        return match.group(1)
    return None
