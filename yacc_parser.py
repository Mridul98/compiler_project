import ply.yacc as yacc
from lex import tokens


toBeParsed = '''

int  main(){
 int a = 123;
 int b = 234;
 int z = (a+b)*12-34+(29/34);
 if(a<b){
     return a;
 } else {
     return b;
 }
 return a+b-z;
}

'''

variable_dict = dict()
statement_sequence = []
return_counter = 0
def p_function(p):
    '''
    function : type FUNCDEF LBRACKET RBRACKET LCURLY statements RCURLY
    '''
    if p[1] == 'int':
        if isinstance(p[6],int):
           print('function returned ',p[6])
        else:
            raise Exception('return type should be type of int') 
        
    if p[1] == 'bool':
        if isinstance(p[6],bool):
            print('function returned ',p[6])
        else: 
            raise Exception('return type should be type of boolean')

    if return_counter == 0:
        raise Exception('No return statement detected')
    
def p_statements(p):
    '''
    statements : statements allstatement
    '''
    
    p[0] = p[2]


def p_statements_empty(p):
    '''
    statements : empty
    '''

def p_allstatements_to_statement(p):
    '''
    allstatement : statement
                 
    '''
    p[0] = p[1]
def p_allstatement_to_condstmt(p):
    '''
    allstatement : condstatement
    '''
def p_allstatement_to_returnstmt(p):
    '''
    allstatement : returnstatement
    '''
    p[0] = p[1]
    
    

def p_returnstmt(p):
    '''
    returnstatement : RETURNTYPE simpleExpression SEMICOLON
    '''
    
   
    global return_counter
    if  return_counter == 0:

        #print('function returned ',p[2])
        p[0] = p[2]
        return_counter = 1
    else:
        raise Exception("Mulitple return statement")

def p_condstatement(p):
    '''
    condstatement : IF LBRACKET simpleExpression RBRACKET LCURLY ifstart statements ifend RCURLY
                  
    '''
    global return_counter
    if return_counter == 1:
        raise Exception('early return') 
    
        

def p_condstatement_withelse(p):
    '''
    condstatement : IF LBRACKET simpleExpression RBRACKET LCURLY ifstart statements ifend RCURLY ELSE LCURLY elsestart statements elseend RCURLY
                  
    '''
    global return_counter
    
    if return_counter == 1:
        raise Exception('early return') 
    
  
        
def p_statement(p):
    # tmp = 3; 
    '''
    statement : FUNCDEF ASSIGNMENTOPS expression SEMICOLON
    '''
    global return_counter
    if return_counter == 1:
        raise Exception('early return') 
    
    if p[1] not in variable_dict.keys():
        raise Exception(p[1],' was not initialized')

    else:
       
        variable_dict[p[1]] = p[3]


    variable_dict[p[1]] = p[3]
    r = p[1]+' '+p[2]+' '+str(p[3])+' '+p[4]
    statement_sequence.append(r)
    p[0] = statement_sequence

def p_statement_ressign(p):
    #int tmp = 23;
    '''
    statement : type FUNCDEF ASSIGNMENTOPS expression SEMICOLON
    '''
    global return_counter
    if return_counter == 1:
        raise Exception('early return') 
    
    if p[2] in variable_dict.keys():
        raise Exception("Duplicate Variable detected")
    else:
        variable_dict[p[2]] = p[4]

    r = p[1]+' '+p[2]+' '+p[3]+' '+str(p[4])+ p[5]
    statement_sequence.append(r)
    p[0] = statement_sequence
   
def p_statement_just_declare(p):
    #int tmp;
    '''
    statement : type FUNCDEF SEMICOLON
    '''
    global return_counter
    if return_counter == 1:
        raise Exception('early return') 
    
    if p[2] in variable_dict.keys():
        raise Exception('Duplicate Variable ',p[2])
    else:
        variable_dict[p[2]] = None

    r = p[1]+' '+p[2]+' '+p[3]
    statement_sequence.append(r)
    p[0] = statement_sequence

def p_statement_assign(p):
    #int tmp = a;
    '''
    statement : type FUNCDEF ASSIGNMENTOPS FUNCDEF SEMICOLON       
    '''
    global return_counter
    if return_counter == 1:
        raise Exception('early return') 
    
    if p[2] in variable_dict.keys():
        raise Exception("Duplicate Variable ",p[2])

    if p[4] not in variable_dict.keys():
        raise Exception('Undefined variable ',p[4])
    
    if variable_dict[p[4]] == None:
        raise Exception(p[4],' has not been initialized')
    
    variable_dict[p[2]] = variable_dict[p[4]]

    r = p[1]+' '+p[2]+' '+p[3]+' '+p[4]+' '+p[5]
    statement_sequence.append(r)
    p[0] = statement_sequence

    

def p_statement_hybrid_equal(p):
    '''
    statement : FUNCDEF hybridEqual expression SEMICOLON
    '''
    global return_counter
    if return_counter == 1:
        raise Exception('early return') 
    
    
    print(p[2])
    if p[1] not in variable_dict.keys():
        raise Exception('Undefined Variable ',p[1])
        
    else:
        if variable_dict[p[1]] == None:
            raise Exception('Uninitialized Variable ',p[1])
        else:

            if p[2] == '+=':
                
                variable_dict[p[1]] = variable_dict[p[1]] + p[3]
                
            if p[2] == '-=':
                variable_dict[p[1]] = variable_dict[p[1]] - p[3]
               
            if p[2] == '*=':
                variable_dict[p[1]] = variable_dict[p[1]] * p[3]
               

            if p[2] == '/=':
                variable_dict[p[1]] = variable_dict[p[1]] / p[3]
                r = '(/=',p[1],' ',p[3],')'
              
        
            if p[2] == '%=':
                variable_dict[p[1]] = variable_dict[p[1]] % p[3]

            r = p[1]+' '+p[2]+' '+str(p[3])+' '+p[4]
            statement_sequence.append(r)
            p[0] = statement_sequence
              



def p_hybridEqual(p):
    '''
    hybridEqual : PLUSEQUAL
                | MINUSEQUAL
                | DIVEQUAL
                | MULEQUAL
    '''
    p[0] = p[1]

def p_simpleExpression(p):
    '''
    simpleExpression : simpleExpression LOGICOROPS andExpression
    '''
    if p[1] or p[3] == True:
        p[0] = True
       
    else:
        p[0] = False
      
def p_simpleExpression_to_andExpression(p):
    '''
    simpleExpression : andExpression
    '''
    p[0] = p[1]
def p_andExpression(p):
    '''
    andExpression : andExpression LOGICANDOPS relExpression
    '''
    if p[1] and p[3] == True:
        p[0] = True
        
    else:
        p[0] = False
      
def p_andExpression_to_relExpression(p):
    '''
    andExpression : relExpression
    '''
    p[0] = p[1]
def p_relExpression_greater(p):
    '''
    relExpression : expression GREATERTHAN expression
    '''
    if p[1] > p[3]:
        p[0] = True
       
    else:
        p[0] = False
      

def p_relExpression_greaterequal(p):
    '''
    relExpression : expression GREATERTHANEQUAL expression
    '''
    if p[1] >= p[3]:
        p[0] = True
        
    else:
        p[0] = False
      
def p_relExpression_less(p):
    '''
    relExpression : expression LESSTHAN expression
    '''
    if p[1] < p[3]:
        p[0] = True
       
    else:
        p[0] = False
       
def p_relExpression_lessequal(p):
    '''
    relExpression : expression LESSTHANEQUAL expression
    '''
    if p[1] <= p[3]:
        p[0] = True
       
    else:
        p[0] = False
       

def p_relExpression_equalequal(p):
    '''
    relExpression : expression EQUALEQUAL expression
    '''
    if p[1] == p[3]:
        p[0] = True
       
    else:
        p[0] = False
        

def p_relExpression_notequal(p):
    '''
    relExpression : expression  NOTEQUAL expression
    '''
    if p[1] != p[3]:
        p[0] = True
        
    else:
        p[0] = False
     
def p_relExpression_to_expression(p):
    '''
    relExpression : expression
    ''' 
    p[0] = p[1]
def p_expression_plus(p):
    '''
    expression : expression PLUS terms
    '''
    p[0] = p[1] + p[3]
    

def p_expression_minus(p):
    '''
    expression : expression MINUS terms
    '''
    p[0] = p[1] - p[3]
    

def p_expression_terms(p):
    '''
    expression : terms
    '''
    p[0] = p[1]


def p_terms_mul(p):
    '''
    terms : terms MUL factor
    '''
    p[0] = p[1] * p[3]
  

def p_terms_div(p):
    '''
    terms : terms DIV factor
          
    '''
    p[0] = int(p[1] / p[3])
  
def p_terms_mod(p):
    '''
    terms : terms MOD factor
    '''
    p[0] = p[1] % p[3]
  
def p_terms_factor(p):
    '''
    terms : factor
    '''
    p[0] = p[1]


def p_factor_number(p):
    '''
    factor : NUMBER
    '''
    p[0] = p[1]

def p_factor_funcdef(p):
    '''
    factor : FUNCDEF
    '''
    if p[1] not in variable_dict.keys():
        raise Exception('Undefined variable ',p[1])

    if variable_dict[p[1]] == None:
        raise Exception(p[1],' has not been initialized')

    p[0] = variable_dict[p[1]]


def p_terms_factor_group(p):
    '''factor : LBRACKET expression RBRACKET
    '''
    p[0] = p[2]
    


def p_typedef(p):
    '''
    type : INTTYPE 
         | FLOATTYPE
         | DOUBLETYPE
         | VOIDTYPE
         | BOOLTYPE
    '''
    
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_if_start(p):
    'ifstart : empty'
    
    
def p_if_end(p):
    'ifend : empty'
    
    
def p_else_start(p):
    'elsestart : empty'

  
    
def p_else_end(p):
    'elseend : empty'

    
    

def p_error(p):
    print('syntax error in input',p)
    raise Exception('syntax error in input ',p)
    




parser = yacc.yacc()


result = parser.parse(toBeParsed)

# print('variable dictionary: ',variable_dict)
# for i in statement_sequence:
#     print(i)