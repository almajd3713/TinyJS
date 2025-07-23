

grammer_rules: dict[str, list[str]] = {
    # Variable values
    "VARIABLE": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
    "DIGIT": [str(i) for i in range(256)],
    
    # Arithmetics and operators
    "ARITHMETIC_OPERATOR": ["+", "-", "*", "/", "%", "**"],
    "RELATIONAL_OPERATOR": ["===", "!=", "<", ">", "<=", ">="],
    "LOGICAL_OPERATOR_PREFIX": ["&&", "||"],
    "LOGICAL_OPERATOR_INFIX": ["&", "|"],
    "LOGICAL_OPERATOR": ["LOGICAL_OPERATOR_PREFIX", "LOGICAL_OPERATOR_INFIX"],
    "OPERATOR": ["ARITHMETIC_OPERATOR"],

    # Formatting
    "TAB": ["\t"],
    "PARENTHESIS_OPEN": ["("],
    "PARENTHESIS_CLOSE": [")"],
    "EQUALS": ["="],
    "COLON": [":"],
    "COMMA": [","],

    # Keywords
    "VAR": ["var"],
    "LET": ["let"],
    "DEFINE_VAR": ['VAR', 'LET'],
    "IF": ["if"],
    "ELSE": ["else"],
    "FOR": ["for"],
    "WHILE": ["while"],
    "OF": ["of"],
    "PRINT": ['console.log', 'console.info'],
    
    # Terms and Expressions
    "TERM": ["EXPRESSION_IDENTIFIER", "DIGIT"], # Expression identifier for existing variables, else pick a random digit
    "EXPRESSION": ['TERM SPACE OPERATOR SPACE TERM'],
    "EXPRESSION_ENCLOSED": ['PARENTHESIS_OPEN EXPRESSION PARENTHESIS_CLOSE'],
    "EXPRESSION_DISPLAY": [
        'EXPRESSION_IDENTIFIER SPACE OPERATOR SPACE EXPRESSION_IDENTIFIER', 
        'EXPRESSION_IDENTIFIER SPACE OPERATOR SPACE DIGIT'
    ],
    
    "IDENTIFIER_INITIALIZATION": ["NEW_LINE IDENTIFIER_INITIALIZATION INITIALIZATION", "NEW_LINE INITIALIZATION"],
    "INITIALIZATION": ['DEFINE_VAR SPACE VARIABLE SPACE EQUALS SPACE DIGIT'],
    
    "SIMPLE_ARITHMETIC_EXPRESSION": [
        'SIMPLE_ARITHMETIC_EXPRESSION ARITHMETIC_OPERATOR EXPRESSION_ENCLOSED',
        'EXPRESSION_ENCLOSED'
    ],
    
    "ASSIGNMENT_SIMPLE": ['NEW_LINE VARIABLE SPACE EQUALS SPACE EXPRESSION'],
    "ASSIGNMENT_COMPLEX": [
        'NEW_LINE DEFINE_VAR SPACE VARIABLE SPACE EQUALS SPACE SIMPLE_ARITHMETIC_EXPRESSION SPACE'
        'NEW_LINE DEFINE_VAR SPACE VARIABLE SPACE EQUALS SPACE EXPRESSION SPACE',
        ''
    ],
    
    'DISPLAY_SIMPLE': ['NEW_LINE PRINT PARENTHESIS_OPEN DISPLAY_IDENTIFIER PARENTHESIS_CLOSE'],
    'DISPLAY_COMPLEX': ['NEW_LINE PRINT PARENTHESIS_OPEN EXPRESSION_DISPLAY PARENTHESIS_CLOSE'],
    
    
    # Levels of complexity
    "LEVEL_1.1": ['IDENTIFIER_INITIALIZATION ASSIGNMENT_SIMPLE DISPLAY_COMPLEX'],
    "LEVEL_1.2": ['IDENTIFIER_INITIALIZATION ASSIGNMENT_COMPLEX DISPLAY_COMPLEX'],
    
    "ALL": ['LEVEL_1.1', 'LEVEL_1.2'],
}

def get_grammer(): return grammer_rules