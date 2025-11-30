import re

def parse_states(react_code):
    """
    Extract all useState declarations from the React component.
    
    Pattern matched:
    const [todos, setTodos] = useState(['Learn React']);
    const [newTodo, setNewTodo] = useState('');
    """

    pattern = r"const\s+\[(\w+),\s*(\w+)\]\s*=\s*useState\((.*?)\)"
    
    matches = re.findall(pattern, react_code, re.DOTALL)
    
    state_vars = []

    for match in matches:
        state_name = match[0]       # e.g. todos
        setter_name = match[1]      # e.g. setTodos
        initial_value = match[2].strip()  # e.g. ['Learn React'] or ''

        state_vars.append({
            "name": state_name,
            "setter": setter_name,
            "initial": initial_value
        })

    return state_vars
