
"""
Starter Python script for React-to-Angular transpiler.

Steps:
1. Read the React component file.
2. Parse JSX and identify component structure.
3. Map React constructs to Angular equivalents.
4. Generate Angular component files.
"""

# Hints:
# - You can use regex or an AST parser for JSX.
# - Focus on converting tags and event bindings.
# - Example: onClick -> (click), value -> [(ngModel)].

react_file = 'react/TodoList.jsx'
angular_ts_file = 'angular_reference/TodoList.component.ts'
angular_html_file = 'angular_reference/TodoList.component.html'

# Read React file
with open(react_file, 'r') as f:
    react_code = f.read()

# TODO: Implement parsing logic here
print("React code loaded. Start implementing conversion logic.")

from parsers.component_name_parser import parse_component_name
from parsers.state_parser import parse_states
from parsers.method_parser import parse_methods
from parsers.jsx_parser import extract_jsx

from converters.jsx_to_angular import convert_jsx
from converters.method_converter import convert_method_body

from generators.ts_generator import generate_ts_component
from generators.html_generator import generate_html_template




#Parsing
component_name = parse_component_name(react_code)
print("Component name:", component_name)

state_vars = parse_states(react_code)
print("Parsed state variables:", state_vars)

methods = parse_methods(react_code)
print("Parsed methods:", methods)

jsx_block = extract_jsx(react_code)
print("Extracted JSX:\n", jsx_block)

# Build Intermediate Representation (IR)
ir = {
    "componentName": component_name,
    "state": state_vars,
    "methods": methods,
    "jsx": jsx_block
}

print("IR Generated:\n", ir)

#Convert JSX to Angular Syntax HTML
converted_jsx = convert_jsx(ir["jsx"])
ir["converted_jsx"] = converted_jsx

# Convert method bodies
for m in ir["methods"]:
    m["body"] = convert_method_body(m["body"], state_vars)

# Generate Angular files
ts_output = generate_ts_component(ir)
html_output = generate_html_template(ir)

with open(f"output/{component_name}.component.ts", "w") as f:
    f.write(ts_output)

with open(f"output/{component_name}.component.html", "w") as f:
    f.write(html_output)

print("Angular files generated successfully!")