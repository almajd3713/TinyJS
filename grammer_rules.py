

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
    "SEMICOLON": [";", ""],

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
    "EXPRESSION": ['TERM SPACE OPERATOR SPACE TERM SEMICOLON'],
    "EXPRESSION_ENCLOSED": ['PARENTHESIS_OPEN EXPRESSION PARENTHESIS_CLOSE'],
    "EXPRESSION_DISPLAY": [
        'EXPRESSION_IDENTIFIER SPACE OPERATOR SPACE EXPRESSION_IDENTIFIER SEMICOLON', 
        'EXPRESSION_IDENTIFIER SPACE OPERATOR SPACE DIGIT'
    ],
    
    "IDENTIFIER_INITIALIZATION": ["IDENTIFIER_INITIALIZATION INITIALIZATION SEMICOLON", "INITIALIZATION SEMICOLON"],
    "INITIALIZATION": ['VARIABLE SPACE EQUALS SPACE DIGIT SEMICOLON NEW_LINE'],
    
    "SIMPLE_ARITHMETIC_EXPRESSION": [
        'SIMPLE_ARITHMETIC_EXPRESSION ARITHMETIC_OPERATOR EXPRESSION_ENCLOSED',
        'EXPRESSION_ENCLOSED'
    ],
    
    "ASSIGNMENT_SIMPLE": ['VARIABLE SPACE EQUALS SPACE EXPRESSION SEMICOLON NEW_LINE'],
    "ASSIGNMENT_COMPLEX": [
        'VARIABLE SPACE EQUALS SPACE SIMPLE_ARITHMETIC_EXPRESSION SEMICOLON NEW_LINE'
        'VARIABLE SPACE EQUALS SPACE EXPRESSION SEMICOLON NEW_LINE',
        ''
    ],
    
    'DISPLAY_SIMPLE': ['PRINT PARENTHESIS_OPEN DISPLAY_IDENTIFIER PARENTHESIS_CLOSE SEMICOLON NEW_LINE'],
    'DISPLAY_COMPLEX': ['PRINT PARENTHESIS_OPEN EXPRESSION_DISPLAY PARENTHESIS_CLOSE SEMICOLON NEW_LINE'],
    
    
    # Levels of complexity
    "LEVEL_1.1": ['IDENTIFIER_INITIALIZATION ASSIGNMENT_SIMPLE DISPLAY_COMPLEX'],
    "LEVEL_1.2": ['IDENTIFIER_INITIALIZATION ASSIGNMENT_COMPLEX DISPLAY_COMPLEX'],
    
    "ALL": ['LEVEL_1.1', 'LEVEL_1.2'],
}

def get_grammer(): return grammer_rules