
<----------------------------------------------This project was built as an assignment of Compiler Construction (CSE-313) taken by Bijoy Rahman Arif during Summer 2020-------------------------------->

<-------------------------------------------------------------------------------Author: Mahmud Un Nabi Mridul (1720307)-------------------------------------------------------------------------------->


Requirements:
    language : python 3.8.5 -64bit
    package  : PLY

I have tried to make this project as perfect as possible. You must read the rest of the part of this file, otherwise you dont have to run my code.

Project Structure:

    lex.py ---> it contains all the regular expression for detecting tokens

    yacc_parser.py ---> it contains CFG and all the corresponding actions

Pros and Cons:
    cons:
        1. I have implemented CFG of if else structure but didnt do the action part.
        2. I have implemented the code only for 'int' and 'bool' to be returned for simplicity when executed. But that doesnt mean that I cant implement the rest of the part
        3. You can only use variable of type 'int' as the other implementation of variable type left unimplemented.
        4. You cant instantiate a variable like this : 
                                                        int a,b; 
                                                        or 
                                                        int a,b = 1,2; 
           Instead you have to instantiate like this :
                                                        int a;
                                                        int b;
                                                        int a = 1;
                                                        int b = 2;
    pros:
        1. I have included a lot of error handling related code. You can try instantiate a variable twice. you will get error message.
        2. All the rules of CFG were constructed by pruning the original grammar of c language to meet the requirement of this project.
        3. I tried to keep the code easier to understand.

YOU MUST READ THE 'pros and cons' PART BEFORE PROCEDING TO THE NEXT)

How to run: (

    1. Run lex.py.
    2. Go to the yacc_parser.py file. 
    3. In yacc_parser.py , there is a variable named 'toBeParsed' in line 5.
    4. Insert your function as a string surrounding with triple-quotes and assign it to 'toBeParsed' variable
    5. Run yacc_parser.py
    6. you will see the output "function returned [something]' in your terminal
    7. To see all the CFG in human readable format, you can open parser.out file
    

Test Cases that are succesful:

int  main(){
 int a = 123;
 int b = 234;
 return a+b;
}

output : function returned 357

int  main(){
 int a = 123;
 int b = 234;
 int z = (a+b)*12-34+(29/34);
 return a+b-z;
}

output : function returned -3893


bool  main(){
 int a = 123;
 int b = 234;
 int z = (a+b)*12-34+(29/34);
 return a==z;
}

output : funtion returned false


Test cases that does not return error: (any test case that includes if else statement will still be parsed but the output will be erroneous )

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

output : Exception : Multiple return statement.      

The output is like that because corresponding action part of if else statement left unimplemented.
