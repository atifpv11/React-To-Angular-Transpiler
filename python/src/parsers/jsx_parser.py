import re

def extract_jsx(react_code):
    """
    Extract the JSX content inside the return(...) block.

    Matches:
    return (
        <div>...</div>
    );
    """

    # Regex to capture everything between return ( ... )
    pattern = r"return\s*\(\s*([\s\S]*?)\s*\);"

    match = re.search(pattern, react_code)

    if match:
        jsx_content = match.group(1).strip()
        return jsx_content
    
    return None
