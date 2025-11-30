import re

def parse_methods(react_code):
    """
    Extract arrow function methods from the React component.
    
    Matches patterns like:
    const addTodo = () => {
        ...
    };
    """

    # Regex to capture "const methodName = () => { ... }"
    pattern = r"const\s+(\w+)\s*=\s*\(\s*\)\s*=>\s*\{([\s\S]*?)\};"

    matches = re.findall(pattern, react_code)

    methods = []

    for match in matches:
        method_name = match[0]    # e.g. addTodo
        method_body = match[1].strip()  # everything inside { ... }

        methods.append({
            "name": method_name,
            "body": method_body
        })

    return methods
