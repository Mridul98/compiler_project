import ply.lex as lex
from ply.lex import TOKEN
""" 
THESE ARE THE TOKENS FOR THIS PROJECT.

    tokens: 
            Arithmetic Operators: + - * / % 
            Increment and Decrement Operators: ++ --
            Assignment Operators: += = -= *= /= %=
            Logical Operators && || !

                                



"""

tokens = (

    'ASSIGNMENTOPS',
    'INCOPS',
    'DECOPS',
    
    'LOGICANDOPS',
    'LOGICOROPS',
    'LOGICNOTOPS',
    'FUNCDEF',
    'NUMBER',
    'LCURLY',
    'RCURLY',
    'LBRACKET',
    'RBRACKET',
    'RETURNTYPE',
    'INTTYPE',
    'FLOATTYPE',
    'DOUBLETYPE',
    'VOIDTYPE',
    'BOOLTYPE',
    'SEMICOLON',
    'COMMA',
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'MOD',
    'PLUSEQUAL',
    'MINUSEQUAL',
    'MULEQUAL',
    'DIVEQUAL',
    'IF',
    'ELSE',
    'GREATERTHAN',
    'GREATERTHANEQUAL',
    'LESSTHAN',
    'LESSTHANEQUAL',
    'EQUALEQUAL',
    'NOTEQUAL'


    )


variables = dict()

#regular expressions for the tokens
t_PLUSEQUAL = r'\+\='
t_MINUSEQUAL = r'\-\='
t_MULEQUAL = r'\*\='
t_DIVEQUAL = r'\/\='
t_ASSIGNMENTOPS = r'\='
t_INCOPS =  r'\+\+'
t_DECOPS =  r'--'

t_LOGICANDOPS =  r'&&'
t_LOGICOROPS = r'\|\|'
t_LOGICNOTOPS = r'!'
t_ignore  = ' \n'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LBRACKET = r'\('
t_RBRACKET = r'\)'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIV = r'\/'
t_MOD = r'\%'
t_MUL = r'\*'
t_IF = r'if'
t_ELSE = r'else'
t_GREATERTHAN = r'\>'
t_GREATERTHANEQUAL = r'\>\='
t_LESSTHAN = r'\<'
t_LESSTHANEQUAL = r'\<\='
t_EQUALEQUAL = r'\=\='
t_NOTEQUAL = r'\!\='

def returnType(typeID):
    typeList = ('float','int','double','void','return','bool')
    reservedKeyWords = ('if','else')
    if typeID in typeList:
        return typeID.upper()+'TYPE'
    if typeID in reservedKeyWords and typeID == 'if':
        return 'IF'
    if typeID in reservedKeyWords and typeID == 'else':
        return 'ELSE'
    return 'FUNCDEF'

def t_FUNCDEF(t):
    r'[a-zA-Z_]+'
    t.type = returnType(t.value)
    return t


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_newline(t):
     r'\n+'
     pass

def t_error(t):
    print("illegal character ",t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

data = """
{
 2 += 3
 int == != <= >= < > || && if else return
"""
lexer.input(data)
# tokenList = []
# while True:
#     tok = lexer.token()
#     tokenList.append(tok)
#     if not tok:
#         break
#     print(tok,len(tokenList))