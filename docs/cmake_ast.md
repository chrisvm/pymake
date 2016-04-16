CMake CMakeLists.txt ast
========================

AST Nodes
---------

`Word`

- (One) `Type`
  `type: Variable | String | Number | CompoundLiteral | VariableDereference`
- (One) `String` `contents`

`Body`

- (Many) (`FunctionCall`, `IfStatement`, `ForeachStatement`, `WhileStatement`)

`FunctionCall`

- (One) `Word` `name`
- (Many) `Word` `arguments`

`FunctionDefinition`

- (One) `FunctionCall` `header`
- (One) `Body` `body`
- (One) `FunctionCall` `footer`

`MacroDefinition`

- (One) `FunctionCall` `header`
- (One) `Body` `body`
- (One) `FunctionCall` `footer`

`IfStatement`

- (One) `FunctionCall` `header`
- (One) `Body` `body`

`ElseIfStatement`

- (One) `FunctionCall` `header`
- (One) `Body` `body`

`ElseStatement`

- (One) `FunctionCall` `header`
- (One) `Body` `body`

`IfBlock`

- (One) `IfStatement` `if_statement`
- (Many) `ElseIfStatement` `else_ifs`
- (One Optional) `ElseStatement` `else_statement`
- (One) `FunctionCall` `footer`

`ForeachStatement`

- (One) `FunctionCall` `foreach_function`
- (One) `Body` `body`
- (One) `FunctionCall` `footer`

`WhileStatement`

- (One) `FunctionCall` `while_function`
- (One) `Body` `body`
- (One) `FunctionCall` `footer`

Each node also has a `line` and `col` member to indicate where it can be
found in the source file.

Word type aliases are stored in `WordType` inside `ast`.

Traversing the AST
------------------

CMake-AST provides a helper module `ast_visitor` to make traversing the AST
less verbose. It will traverse every single node by default. Listeners
matching the signature `def handler (name, node, depth)` can be passed as
the following keyword arguments to `recurse (body, **kwargs)`:

| Keyword         | Handles Node Type    |
|:---------------:|:--------------------:|
| `toplevel`      | `ToplevelBody`       |
| `while_stmnt`   | `WhileStatement`     |
| `foreach`       | `ForeachStatement`   |
| `function_def`  | `FunctionDefinition` |
| `macro_def`     | `MacroDefinition`    |
| `if_block`      | `IfBlock`            |
| `if_stmnt`      | `IfStatement`        |
| `elseif_stmnt`  | `ElseIfStatement`    |
| `else_stmnt`    | `ElseStatement`      |
| `function_call` | `FunctionCall`       |
| `word`          | `Word`               |