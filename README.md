# SingleVariableExpressionParser [![Build Status](https://travis-ci.com/AliEzzatOdeh/SingleVariableExpressionParser.svg?branch=master)](https://travis-ci.com/AliEzzatOdeh/SingleVariableExpressionParser)

Python package for parsing single variable mathmatical expressions.

Table of supported math operations:

| Operation      | Syntax        | # of operands   |
| -------------  |:-------------:| ---------------:|
| Addition       |     +         |       2         |
| Subtraction    |     sub       |       2         |
| Multiplication |     *         |       2         |
| Division       |     /         |       2         |
| L.Parantheses  |     (         |       >=1       |
| R.Parantheses  |     )         |       >=1       |
| sin            |     sin       |       1         |
| cos            |     cos       |       1         |
| tan            |     tan       |       1         |
| seq            |     seq       |       1         |
| csc            |     csc       |       1         |
| cot            |     cot       |       1         |
| power          |     ^         |       2         |
| square root    |     sqr       |       1         |
| minus          |     -         |       1         |


## Install

To install the package using `pip`:

`pip install single-variable-expression-parser-ALIEZZAT`

## Usage

Import the module as the following:

```
from math_expression_parser.single_variable_parser import SingleVariableParser
```
Then it should be used as:

```
parser = SingleVariableParser()
parser.set_math_function_text('sqr(16)+1') # For constant expression
result = parser.compute_function_at_value(0) # Here input has no effect on result since it is constant
print(result) # 5 will be printer 

parser = SingleVariableParser()
parser.set_math_function_text('x*2+x^2+5')
result = parser.compute_function_at_value(4) # Value of x will be 4
print(result) # 29 will be printed
```

## Running unit tests

Run `python3 -m unittest discover` to execute the unit tests via `unittest`.
