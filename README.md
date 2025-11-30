
# Candidate Task: React-to-Angular Transpiler

## Objective
Build a Python script that converts a React component into an Angular component.

### What You Have:
- A sample React component (`TodoList.jsx`).
- A reference Angular component structure.
- A starter Python script (`transpiler.py`).

### What You Need to Do:
- Parse the React component.
- Generate Angular component files:
  - `TodoList.component.ts`
  - `TodoList.component.html`
- Document your approach in a README.

### Notes:
- Focus on mapping JSX to Angular template syntax.
- Map React state/props to Angular bindings.
- Even partial solutions are acceptable if you explain your approach.

### Level 2 (Interview):
- Extend your transpiler to handle hooks or nested components.


### RESULT

React-to-Angular Transpiler

This project implements a Python-based transpiler that converts a restricted subset of React functional components into Angular component files. The primary focus of this solution is the design approach, modularity, and architectural clarity rather than achieving full React–Angular parity. The output of the transpiler consists of two files: a TypeScript Angular component class and an Angular HTML template.
---

Objective

The objective of the assignment is to parse a simple React function component written using React Hooks, extract its structure, convert the JSX template into Angular template syntax, translate state and methods into Angular class equivalents, and generate the corresponding Angular component files. The assessment prioritizes clarity of reasoning, structure of the solution, and the ability to explain the underlying approach.
---

Architectural Overview

The transpiler is designed following a modular, phase-based architecture similar to traditional compiler and transpiler pipelines. The project is intentionally separated into distinct layers to make the solution easy to reason about, extend, and debug. The architectural stages are as follows:

Parsing Phase
This phase extracts meaningful information from the raw React code. The parsers use constrained, targeted regular-expression patterns that are limited to the expected syntax provided in the assignment. Separate modules handle component name extraction, state parsing (useState declarations), method extraction (arrow functions), and JSX extraction (content inside the return block).

Intermediate Representation (IR)
After parsing, all extracted elements are consolidated into a single structured dictionary. This IR contains the component name, state variables, methods, the raw JSX block, and later, the converted Angular-compatible template. The purpose of the IR is to decouple input parsing from output generation. It serves as the central data object for all subsequent transformations.

Conversion Phase
The conversion phase applies rule-based transformations to the JSX and method bodies. This includes converting JSX interpolation to Angular interpolation, transforming event handlers, converting .map() constructs to *ngFor, removing React-specific attributes such as onChange, and applying Angular-style two-way binding for text inputs. A separate converter handles translation of React setState patterns into Angular property assignments and array updates. Converters operate on IR fields rather than raw code, which maintains clarity and separation of concerns.

Generation Phase
Once the IR has been fully enriched and transformed, the final stage outputs valid Angular component files. A TypeScript generator produces the component class with state variables translated into Angular properties and methods rewritten into Angular-compatible form. The HTML generator writes the converted JSX (now Angular template syntax) into a separate .component.html file. The generation phase is deterministic: it does not perform transformation, only structured output.

This modular pipeline ensures that each stage is independent, testable, and conceptually clear. The entire design reflects a reduced, educational version of real-world transpilers.
---

Parsing Strategy

The parsing phase uses regular expressions rather than AST tooling. This decision was intentional and aligned with the constraints and expectations of the assignment. The provided React component is simple, predictable, and structurally stable, making regex-based parsing sufficient and practical. Attempting to use a full JSX AST parser in Python would introduce unnecessary complexity, external dependencies, and tooling overhead, without adding practical value for the given problem.

Each parser module is focused on a single responsibility:

The component name parser identifies function declarations.
The state parser extracts variable names, setters, and initial values from useState.
The method parser captures arrow functions and supports nested braces by matching until the terminating }; sequence.
The JSX parser extracts the return-block content for subsequent template conversion.
---

Intermediate Representation

All parsed data is merged into a single IR object before any transformations. This IR acts as a well-defined schema describing the React component in a neutral format. The IR enables clean separation between parsing and generation. It also makes the transpiler more maintainable and ready for future enhancements, such as nested components, props, or more advanced React constructs.
---

Conversion Strategy

The conversion phase applies transformation rules that map React patterns to Angular patterns. Examples include:

{value} converted to {{ value }}
onClick={addTodo} converted to (click)="addTodo()"
value={newTodo} converted to [(ngModel)]="newTodo"
.map() loops converted to Angular *ngFor constructs

React's state updates such as setTodos([...todos, newTodo]) are rewritten into Angular operations like this.todos.push(this.newTodo). The converter follows a carefully determined ordering to ensure that conversions do not interfere with each other, such as applying array conversions before setter conversions and applying the this. prefix additions at the end.

The converters operate on IR fields, not raw files, maintaining the modularity and clarity of the architecture.
---

Code Generation

The TypeScript generator produces an Angular component class based on the IR. It constructs the component decorator, initializes properties using state initial values, and inserts converted methods. The HTML generator writes the converted template into a separate file. Both generators remain free of parsing or conversion logic; they only format and output previously prepared IR data.
---

Running the Transpiler

Run the transpiler using:

python src/transpiler.py

The output Angular files will be written to the output directory.
---

Limitations

This transpiler supports only the strict patterns in the provided React component. It does not support props, child components, fragments, contextual hooks (such as useEffect), or advanced JSX constructs. These limitations are intentional and consistent with the assignment scope. With more time, the IR-based architecture allows for extensions such as AST-backed parsing, nested component tree processing, and expanded conversion rules.
---

Extensibility and Level 2 Discussion

Due to the modular phase-based architecture, the transpiler can be extended by adding new parsers, converters, or generators without altering existing components. For example:

Additional hooks can be parsed by adding new parser modules.
Props can be added to the IR and reflected in the HTML generator.
Nested components could be parsed recursively by enriching the JSX parser.
If required, this design can be adapted to use a real AST parser by replacing or augmenting the parsing phase while preserving the IR and generation phases.

The architecture was explicitly designed to demonstrate clarity, composability, and readiness for future expansion.
---

Conclusion

This project provides a structured, modular, and well-reasoned approach to building a simplified React-to-Angular transpiler. The design emphasizes clarity of thought, maintainability, and a realistic understanding of compiler-style pipelines, fulfilling the goals of the assessment while providing a foundation that can be extended in more advanced settings.
---
