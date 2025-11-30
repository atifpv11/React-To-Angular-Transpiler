import re

def convert_method_body(body, state_vars):
    """
    Convert React setState logic into Angular property updates.
    Only handles simple patterns for this assignment.
    """

    # Convert setState for simple values
    for state in state_vars:
        name = state["name"]
        setter = state["setter"]

        # Convert array updates: setTodos([...todos, newTodo])
        body = re.sub(
            rf"{setter}\(\[\.\.\.{name},\s*(\w+)\]\)",
            rf"{name}.push(\1)",
            body
        )

        # Convert setX('value') -> this.x = 'value'
        body = re.sub(
            rf"{setter}\((.*?)\)",
            rf"{name} = \1",
            body
        )

        # Add "this." to bare variable references
        body = re.sub(
            rf"\b{name}\b",
            rf"this.{name}",
            body
        )

    return body
