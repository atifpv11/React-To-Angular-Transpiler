import re

def convert_interpolation(jsx):
    # {value} -> {{ value }}
    return re.sub(r"\{(\w+)\}", r"{{ \1 }}", jsx)

def convert_events(jsx):
    # onClick={addTodo} -> (click)="addTodo()"
    jsx = re.sub(r'onClick=\{(\w+)\}', r'(click)="\1()"', jsx)
    return jsx

def convert_ng_model(jsx):
    # value={newTodo} -> [(ngModel)]="newTodo"
    jsx = re.sub(r'value=\{(\w+)\}', r'[(ngModel)]="\1"', jsx)
    return jsx
#We intentionally ignore the onChange handler because Angular handles it automatically.
def remove_onchange(jsx):
    # Remove entire onChange={...} attribute
    jsx = re.sub(r'onChange=\{.*?\}', '', jsx)
    return jsx


def convert_loops(jsx):
    # Match the map loop and extract list & item name
    loop_pattern = r"\{(\w+)\.map\(\((\w+),\s*\w+\)\s*=>\s*\(([\s\S]*?)\)\)\}"
    
    match = re.search(loop_pattern, jsx)
    if match:
        list_name = match.group(1)      # todos
        item_name = match.group(2)      # todo

        # Build Angular *ngFor syntax
        angular_loop = f'<li *ngFor="let {item_name} of {list_name}">{{{item_name}}}</li>'

        # Replace entire map block with angular loop
        jsx = re.sub(loop_pattern, angular_loop, jsx)

    return jsx

def convert_jsx(jsx):
    # Run converters in proper sequence
    jsx = convert_loops(jsx)
    jsx = convert_events(jsx)
    jsx = convert_ng_model(jsx)
    jsx = remove_onchange(jsx)
    jsx = convert_interpolation(jsx)
    return jsx
