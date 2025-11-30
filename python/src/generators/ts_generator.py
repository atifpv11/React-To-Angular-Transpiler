def generate_ts_component(ir):
    """
    Generate the Angular TypeScript component file (.ts)
    using the IR contents.
    """

    component_name = ir["componentName"]
    class_name = component_name + "Component"

    # Generate state variables
    ts_state_lines = []
    for state in ir["state"]:
        name = state["name"]
        initial = state["initial"]

        # Determine type (simple heuristic)
        if initial.startswith("["):
            var_type = "string[]"
        else:
            var_type = "string"

        ts_state_lines.append(f"  {name}: {var_type} = {initial};")

    ts_state = "\n".join(ts_state_lines)

    # Generate methods
    ts_methods_lines = []
    for method in ir["methods"]:
        method_name = method["name"]
        method_body = method["body"]

        # Indent method body
        indented_body = "\n    ".join(method_body.split("\n"))

        ts_methods_lines.append(
            f"  {method_name}() {{\n    {indented_body}\n  }}"
        )

    ts_methods = "\n\n".join(ts_methods_lines)

    # Build the full TypeScript component
    ts_output = f"""import {{ Component }} from '@angular/core';

@Component({{
  selector: 'app-{component_name.lower()}',
  templateUrl: './{component_name}.component.html',
}})
export class {class_name} {{
{ts_state}

{ts_methods}
}}"""

    return ts_output
