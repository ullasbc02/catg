# catg

<img src="logo.png" alt="Logo" width="200"/>

New Programming language with Python

---

## 🟢 What Is a **Lexer**?

A **lexer** (short for **lexical analyzer**) is the first stage of a compiler or interpreter.
Its job is to **scan the raw code** (text) and break it into **tokens** — meaningful chunks that the parser can understand.

---

## 💡 Real-World Analogy

Imagine this sentence:

```
let x = 5 + 3;
```

A lexer would turn this into:

```
[LET] [ID:x] [EQUALS] [INT:5] [PLUS] [INT:3] [SEMICOLON]
```

Like breaking down a sentence into labeled parts:

* "let" → keyword
* "x" → identifier
* "=" → operator
* "5" → integer
* "+" → operator
* "3" → integer
* ";" → punctuation

---

## 🧱 What Does a Lexer Do?

| Task                    | Example                                           |
| ----------------------- | ------------------------------------------------- |
| Reads characters        | `l`, `e`, `t`, ` `, `x`, `=` ...                  |
| Groups them into tokens | `let`, `x`, `=`, `5`, `+`, `3`, `;`               |
| Labels them with types  | `LET`, `ID`, `EQUALS`, `INT`, `PLUS`, `SEMICOLON` |

---

## 🧠 Why Do We Need a Lexer?

Because:

* It's **much easier** to analyze structured tokens than raw text
* Lexing separates low-level concerns (characters, symbols) from high-level logic (expressions, statements)

---

## 📦 Output of a Lexer: **Token Stream**

The lexer turns this:

```catg
print 5 + 2;
```

Into this:

```text
PRINT    ('print')
INT      (5)
PLUS     ('+')
INT      (2)
SEMICOLON (';')
```
---

## 🔁 Summary

| Concept | Description                                                 |
| ------- | ----------------------------------------------------------- |
| Lexer   | Turns source code text into tokens                          |
| Token   | A labeled piece of code (e.g., keyword, number, identifier) |
| Why?    | So the parser can work with structure instead of raw text   |

---
Excellent — after the **lexer**, the **parser** is the next big player in a programming language’s engine. Let’s go step by step:

---

## 🟩 What Is a **Parser**?

A **parser** is the part of a compiler or interpreter that takes the stream of tokens (from the lexer) and checks if the **structure** of the code is valid according to the grammar.

It also **builds a tree** — called a **parse tree** or **syntax tree** — that represents how the code is organized.

---

## 🧠 In Simple Words:

* **Lexer** → breaks text into words (tokens)
* **Parser** → checks grammar and builds sentence structure (tree)

---

### 🧾 Example: Input Code

```catg
let x = 5 + 2;
```

### ✅ Lexer Output (Tokens):

```
LET  ID(x)  EQUALS  INT(5)  PLUS  INT(2)  SEMICOLON
```

### ✅ Parser Output:

A tree that looks like this:

```
assignment
├── let
├── x
├── =
└── expr
    ├── 5
    ├── +
    └── 2
```

---

## 📦 What Does the Parser Actually Do?

| Task                  | Example                                  |
| --------------------- | ---------------------------------------- |
| Reads tokens          | `LET`, `ID`, `=`, `INT`, `+`, `INT`, `;` |
| Follows grammar rules | Is this a valid assignment?              |
| Builds tree structure | Represents how parts fit together        |
| Detects syntax errors | e.g., missing `;` or unmatched `(`       |

---

## 🧱 Parser + Grammar

You define the parser rules in your ANTLR `.g4` file. For example:

```antlr
assignment: 'let' ID '=' expr ;
expr: expr '+' expr | INT | ID ;
```

ANTLR will:

* Generate the parser class (`catgParser`)
* Use this to check if the token sequence fits the rules
* Create a **ParseTree**

---

## 🧠 Why Is This Important?

* **No logic is done here** — parser doesn’t calculate `5 + 2`
* It just says: “Yes, this is a valid `assignment` statement”
* Then you (in the visitor) will write the logic to actually **run or evaluate** the code

---

## 🔁 Summary

| Component | Role                                        |
| --------- | ------------------------------------------- |
| Lexer     | Breaks raw code into tokens                 |
| Parser    | Checks structure (syntax) and builds a tree |
| Visitor   | Walks the tree and adds meaning (semantics) |

---



