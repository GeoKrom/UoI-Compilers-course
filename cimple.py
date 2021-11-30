## Ονοματεπώνυμο : Λάμπρος Βλαχόπουλος , ΑΜ : 2948 , username : cse52948 
## Ονοματεπώνυμο : Γιώργος Κρομμύδας   , ΑΜ : 3260 , username : cse63260  

import sys 

global list

list=['program','declare','if','else','while','switchcase','forcase',
    'incase','case','default','not','and','or','function',
    'procedure','call','return','in','inout','input','print']

########### GLOBAL VARIABLES #################
scopeList = [""]
nesting = 1
currentScope = 0
List_after_delete_scope = []
argumentuniqeID = 0
entityuniquqeID = 0
functionL = {}
listofFuncPars = []
functionsList = []
procedureList = []
procedureL = {}
inFunction = False
foundreturn = False
###########
T_i = 0 
counter_next_quad = 0
quadList = []
main_program_name = ""
have_sub_program = False
list_of_variables = []
subProgramType = ""
subprogram_name = ""

####################### LECTICAL ANALYSIS #######################

class Token:
 
    def __init__(self, tokenType, tokenString, lineNo):
    
        self.tokenType=tokenType
        self.tokenString=tokenString
        self.lineNo=lineNo

counter_for_lines = 1

def lexical_analyze():

    global  counter_for_lines
    
    tokenString= []        ## token
    counter_for_letters = 0      # letter counter
    
    char = infile.read(1)      # Read first character
    
    # start of lex automaton
    #The while loop contains the whitespace characters(" ", \t, \n)
    while True:
    	 if char == " " or char == "\t":
            char = infile.read(1)
    	 elif char.isspace():
    	 	if char == "\n":
    	 		counter_for_lines += 1
    	 		return lexical_analyze()
    	 else:       
            break

    # Digit state of automaton
    if (char.isdigit()):
        tokenString.append(char)
        
        char = infile.read(1)
        
        while(char.isdigit()):
            tokenString.append(char)
            char = infile.read(1)

        infile.seek(infile.tell()-1) # Look the next character and turn the pointer to previous one
        
        if char.isalpha():
        	t = ''.join(tokenString)
        	print("Error : There is a string which starts with numbers (",t,") in line: ", counter_for_lines)
        	sys.exit()
                
        number = ''.join(tokenString)
        if (int(number) < -(pow(2,32)-1) or int(number) > (pow(2,32) - 1) ):  # Check if the number is valid for the language
            print("The number ",number, "is out of bounds of 2^32 - 1")
            sys.exit()
          
        return Token("number", number.strip(), counter_for_lines)
        sys.exit()
        
        
    # identifier/keywordString state of automaton
    elif (char.isalpha()):
        counter_for_letters += 1
        tokenString.append(char)
        char = infile.read(1)
        
        while (char.isalpha() or char.isdigit()): # Continue read the word until EOF
            tokenString.append(char)
            counter_for_letters += 1
            char = infile.read(1)

        infile.seek(infile.tell()-1)   
        tokenString =''.join(tokenString)
       
        if counter_for_letters <= 30:
             if(tokenString.strip() in list): 
                type = "identifier"
             else:
                type = "keyword"
             return Token(type,tokenString.strip(),counter_for_lines)
             sys.exit()
        else:
            print("The string", tokenString.strip(), " is out of bounds. It should have less than 30 characters\n")
            sys.exit()
    
    # addOperator  state of automaton
    elif char == "+":
        addOperator="+"
        return Token("addOperator",addOperator.strip(),counter_for_lines)
        sys.exit()

    elif char == "-":
        addOperator="-"       
        return Token("addOperator",addOperator.strip(),counter_for_lines)
        sys.exit()
    
    # mulOperator state of automaton  
    elif char == "*":
        mulOperator="*"
        return Token("mulOperator",mulOperator.strip(),counter_for_lines)
        sys.exit()
     
    elif char == "/":
        mulOperator="/"
        return Token("mulOperator",mulOperator.strip(),counter_for_lines)
        sys.exit()
    
    # groupSymbol state of automaton
    elif char == "{":
        groupSymbol = "{"
        return Token("groupSymbol", groupSymbol.strip(), counter_for_lines)
        sys.exit()
        
    elif char == "}":
        groupSymbol = "}"
        return Token("groupSymbol", groupSymbol.strip(), counter_for_lines)
        sys.exit()
        
    elif char == "(":
        groupSymbol = "("
        return Token("groupSymbol", groupSymbol.strip(), counter_for_lines)
        sys.exit()
        
    elif char == ")":
        groupSymbol = ")"
        return Token("groupSymbol", groupSymbol.strip(), counter_for_lines)
        sys.exit()

    elif char == "[":
        groupSymbol = "["
        return Token("groupSymbol", groupSymbol.strip(), counter_for_lines)
        sys.exit()
     
    elif char == "]":
        groupSymbol = "]"
        return Token("groupSymbol", groupSymbol.strip(), counter_for_lines)
        sys.exit()
        
    
    # delimiter state of automaton    
    elif char == ",":
        delimiter = ","
        
        return Token("delimiter", delimiter.strip(), counter_for_lines)
        sys.exit()
    
    elif char == ";":
        delimiter = ";"
        return Token("delimiter", delimiter.strip(), counter_for_lines)
        sys.exit()
    
    # assignment state of automaton
    elif char == ":":      
        char = infile.read(1)
        if char == "=":
            assignment = ":="
            return Token("assignment", assignment.strip(), counter_for_lines)
            sys.exit()
        else:  
            print ("Error : After ':' should come '=' so we can have ':=' which belongs in the language.\nThe charcter that read was", char, "in line:", counter_for_lines)   
            sys.exit()       
    
    # relOperator state of automaton  
    elif char == "<":
        char = infile.read(1)
        if(char == "="):
            relOperator = "<="
            return Token("relOperator", relOperator.strip(), counter_for_lines)
            sys.exit()
        elif char == ">":
            relOperator = "<>"
            return Token("relOperator", relOperator.strip(), counter_for_lines)
            sys.exit()      
        else:
            infile.seek(infile.tell() - 1)
            relOperator = "<"
            return Token("relOperator", relOperator.strip(), counter_for_lines)
            sys.exit()

    elif char == ">":
        char = infile.read(1)
        if char == "=":
            relOperator = ">="
            return Token("relOperator", relOperator.strip(), counter_for_lines)
            sys.exit()
        else:
            infile.seek(infile.tell() - 1)
            relOperator = ">"
            return Token("relOperator", relOperator.strip(), counter_for_lines)
            sys.exit()
            
    elif char == "=":
        relOperator = "="
        return Token("relOperator", relOperator.strip(), counter_for_lines)
        sys.exit()
    
    # finish state of automaton
    elif char == ".":
        end_of_program = "."
        return Token("finish", end_of_program.strip(), counter_for_lines)
        sys.exit()
    
    # Comments state of auromaton 
    elif char == "#":                         # Comments start with '#' character
        char = infile.read(1)                 # Read the next     
        while(char != "#"):                   # Read every character after '#' 
            char = infile.read(1)              
            if char == "":                    # If the final character is not '#' then error. Comments have systax '# anything #'
                print("Error: Found a comment which didn't close in line: ", counter_for_lines)
                sys.exit()
        return lexical_analyze()                
    # eof state of automaton
    elif char == "":
    	return Token("EOF", "END OF FILE", counter_for_lines)
    	sys.exit()
    
    else:
        print ("The language does not support this character in line :",counter_for_lines,"\nThe character was :", char)
       	sys.exit()


######################### SYNTAX ANALYSIS #########################

def syntax_analyze():    
	global token
	token = lexical_analyze()
	program()
	
def program():
    global token
    global main_program_name
    global nesting, scopeList
    
    l = token.lineNo	
    if(token.tokenString == "program"):
        token=lexical_analyze()
        if(token.tokenType == "keyword"):
            main_program_name = token.tokenString
            scope = Scope(nesting) ##
            token = lexical_analyze()
            ###
            ent = Entity(main_program_name,'main',8) ##
            scope.addentity(ent)
            scopeList[currentScope] = scope
            ###
            block(main_program_name)            
            if token.tokenString == ".":
                genquad("halt","_","_","_")
                genquad("end_block",main_program_name,"_","_")
                List_after_delete_scope.append(scopeList.pop(0))     ###
                token = lexical_analyze()
                if(token.tokenString != "END OF FILE"):
                    x = ""
                    while(1):  
                        if(token.tokenString != "END OF FILE"):
                            x = x +"\n" +token.tokenString
                            token = lexical_analyze()
                            continue
                        else:
                            break
                    print("WARNING : Found block of code after '.' , in line :",token.lineNo,"\nThe tokens of the block which follows after the end are: ",x )
                    sys.exit()
            else:
                print("ERROR: Didn't find '.' at the end of program in line ",token.lineNo,"\nIt found :'",token.tokenString,"'")
                sys.exit()	          
        else:
            print("ERROR: Didn't find a name of a variable in line",l,"\nFound ",token.tokenString)
            sys.exit()
    else:
        print("The forb_word 'program' does not exist at the start of the program","\nIn line ",l,"Found ",token.tokenString)
        sys.exit()
    				
			
def block(func_name):
    global token
    global scopeList,inFunction,main_program_name

    declarations()   
    subprograms()
   
    if func_name==main_program_name:
        inFunction=False   #den exw sunarthsh h diadikasia ka9ws to name pou phra apo program den alla3e meta apo subprograms
        genquad("begin_block",main_program_name,"_","_")
    else:
        scope=scopeList[0] ################
        entL=scope.returnListOfEntitys()
        ent=entL[0]
        ent.setstartQuad(nextquad())
        entL[0]=ent
        scope.setListOfEntitys(entL) ###########
        genquad("begin_block",func_name,"_","_")
    statements()
	
def subprograms():
    global token, have_sub_program
    while(token.tokenString=="function" or token.tokenString=="procedure"):
        have_sub_program=True
        subprogram()
 
def subprogram():
    global token,subProgramType,subprogram_name,foundreturn
	
    global functionsList,variableforSeeReturnCheck,functionL,nesting,currentScope,List_after_delete_scope,inFunction   #####
    global procedureList,procedureL
    
    if(token.tokenString=="function" or token.tokenString=="procedure"):
        if(token.tokenString=="function"):
            subProgramType="function"
            inFunction=True
        else:
            subProgramType="procedure"
            inFunction=False
            
        token=lexical_analyze()
        nesting=nesting+1          #####
        if(token.tokenType=="keyword"):
            
                if token.tokenString in functionL or token.tokenString in procedureL : ##
                   
                    print("Error: Βρεθηκε συνάρτηση ή διαδικασια με το ίδιο όνομα:","'",token.tokenString,"'")
                    sys.exit() ##
                
                if(subProgramType=="function"):
                    functionsList.append(token.tokenString)
                   
                    functionL.update({token.tokenString:0})
                else:
                    
                    procedureList.append(token.tokenString)
                    
                    procedureL.update({token.tokenString:0})
                    
               
                
                serSerTemp = Entity('', '', 0)
                serSerTemp = searchScope(token.tokenString)
                if token.tokenString== serSerTemp.name:
                   
                    print("Βρέθηκε συνάρτηση με όνομα ορισμένης μεταβλητής")
                    print("Το ονομα της συναρτησης που βρεθηκε ειναι",token.tokenString,"Στη γραμμη",token.lineNo)
                    sys.exit()
                
                subprogram_name=token.tokenString
                line=token.lineNo
                scope=Scope(nesting)
                
                ent=Entity(subprogram_name,subProgramType,8) 
                scope.addentity(ent)
                scopeList.insert(0,scope)                
                token=lexical_analyze()
               
                if(token.tokenString=="("):
                    token=lexical_analyze()
                    formalparlist()
                   
                    if (token.tokenString==")"):
                        token=lexical_analyze()
                        
                        block(subprogram_name)
                        
                        if (foundreturn!=True and subProgramType=="function"):
                            print("Βρέθηκε συναρτηση χωρις Return.Το ονομα της είναι:",subprogram_name,"Στη γραμμή",line)
                            sys.exit()
                            
                        foundreturn=False
                        
                        scopePrevious=scopeList[currentScope+1] #######
                        scope=scopeList[currentScope]
                        enL=scope.returnListOfEntitys()
                        ent=enL[0]
                        entemp=enL[-1]
                        ent.changeoffset(scopePrevious.getTotalOffset()) ### +4 gia A diaforetiko apo metavlhth
                        ent.setframelength(entemp.returnoffset())
                        scopePrevious.addentity(ent)
                        genquad("end_block",subprogram_name,"_","_")
                        nesting=nesting-1
                        List_after_delete_scope.append(scopeList.pop(0)) #######
                       
                    else:
                        
                        print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
                        sys.exit()
                
                else:
				
                    print("ERROR : Το πρόγραμμα περίμενε '(' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
                    sys.exit()
                
            
                
        else:
			
            print("ERROR : Το πρόγραμμα περίμενε 'όνομα μεταβλητής' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
            
    if(subProgramType=="function"):
        variableforSeeReturnCheck=functionsList.pop(0) 
           
    else:
                
        variableforSeeReturnCheck=procedureList.pop(0)
        


    
def formalparlist():
    global token
    if(token.tokenString=="in" or token.tokenString=="inout"):
        formalparitem()
        while(token.tokenString==","):
            token=lexical_analyze()
            formalparitem()
    else:	
        print("ERROR : Το πρόγραμμα περίμενε 'in' ή 'inout' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()		
			

def formalparitem():
    global token
    global listofFuncPars,scopeList #####
    
    scope=scopeList[currentScope]
    if(token.tokenString=="in" or token.tokenString=="inout"):
        if token.tokenString=="in":
            type_="in"
        else:
            type_="inout"
      
        token=lexical_analyze()
        if(token.tokenType=="keyword"):
            ent=Entity(token.tokenString,"var",(scope.getTotalOffset()+4))
            ent.setParMode(type_)
            scope.addentity(ent)
            arg=Argument(type_,"int")
            entL=scope.returnListOfEntitys() ##Παιρνουμε τη λιστα με entitys που ειναι στο scope
            ent=entL[0] #pairnei to teleutaio entity pou einai to entity tou subprogram        #####Dangerr !!
            ent.setArgument(arg)#vazoume to argument sto entity
            entL[0]=ent # antika8ista sthn teleutaia 8esh ths listas me ta entity to entity
            scope.setListOfEntitys(entL)
            scopeList[currentScope]=scope
            token=lexical_analyze()
        else:		
            print("ERROR : Το πρόγραμμα περίμενε 'keyword/ονομα μεταβλητής' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString) 
            sys.exit()    
    else:
        print("ERROR : Το πρόγραμμα περίμενε 'in' or 'inout' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()
		
								
def actualparlist(sub_prog_name):
    global token
    
    global listofFuncPars 
   
    x = Entity(sub_prog_name,"SubProgramForCheck",0) 
    listofFuncPars.insert(0,x) 
   
    parameters=[]
    parameter=actualparitem()
    parameters.append(parameter)
    
    while(token.tokenString==","):
        token=lexical_analyze()
        parameter=actualparitem()
        parameters.append(parameter)
       
    return parameters

def actualparitem():
    global token
    global listofFuncPars
    
    x=listofFuncPars[0]
    
    if(token.tokenString=="in"):
        token=lexical_analyze()
        arg=Argument("in","int")
        x.setArgument(arg)
        exp=expression()
        return (exp,"CV")
    elif(token.tokenString=="inout"):
        token=lexical_analyze()
        arg=Argument("inout","int")
        x.setArgument(arg)
        name=token.tokenString
        if(token.tokenType!="keyword"):   
            print("ERROR : Το πρόγραμμα περίμενε 'keyword/ονομα μεταβλητής' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
        token=lexical_analyze()
        return (name,"REF")
    else:
        print("ERROR : Το πρόγραμμα περίμενε 'in' or 'inout' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit() 
    
    listofFuncPars[0]=x

def idtail(sub_prog_name):
    global token
    
    if(token.tokenString=="("):
        token=lexical_analyze()
        parameters=actualparlist(sub_prog_name)    #
        if(token.tokenString==")"):
            token=lexical_analyze()
            return(True, parameters)       
        else:
            print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
    return(False, None)     

        										   
def declarations():
    global token
    l=token.lineNo
    if(token.tokenString=="declare"):

        token=lexical_analyze()
        varlist()	
        if(token.tokenString!=";" ):		
            print("ERROR : Το πρόγραμμα περίμενε ';' or ',' στη γραμμή:",l,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
        token=lexical_analyze()
        if(token.tokenString!=""):
            if(token.tokenString=="declare"):
                declarations()
	#############################			
   # global token
    #if (token.tokenString=="declare"):
     #   while 1:
                
      #      token=lexical_analyze()
       #     varlist()
        #    if(token.tokenString==";"):
           #     token=lexical_analyze()
          #  else:
            #    print("ERROR : Το πρόγραμμα περίμενε ';' or ',' στη γραμμή:",l,"\nΒρέθηκε ",token.tokenString)
             #   sys.exit()
           # if(token.tokenString=="declare"):
            #    continue;
            #else:
              #  break;
        
  #  else:
   #     print("ERROR : Το πρόγραμμα περίμενε 'declare'  στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
    #    sys.exit()
	########################		
def varlist():
    global token,list_of_variables 
    global currentScope,scopeList

    count=token.lineNo
    if(token.tokenString!=""):
        serSerTemp = Entity('', '', 0) #########
        serSerTemp = searchScope(token.tokenString) #######
        if(token.tokenType=="keyword" and "Fail"==serSerTemp.name):  ###
            list_of_variables.append(token.tokenString);     ###
            
            scope=scopeList[currentScope]
            totalscope=scope.getTotalOffset()
            ent=Entity(token.tokenString,"var",(totalscope+4))


            scope.addentity(ent)
            scopeList[currentScope] = scope

            
            token=lexical_analyze()
            if(token.tokenString==","):
                token=lexical_analyze()
                varlist()
        else:
            print("ERROR : Το πρόγραμμα περίμενε 'keyword/ονομα μεταβλητής' ή υπαρχει το όνομα μεταβλητής ήδη δηλωμένο στη γραμμή:",count,"\nΒρέθηκε ",token.tokenString) ######
            sys.exit()			
			

def statements():
    global token

    if(token.tokenString=="{"):
        token=lexical_analyze()
        l=token.lineNo
        statement()
		
        if(token.tokenString==";"):
            while(1):
                token=lexical_analyze()
                k=token.lineNo
                statement()
                if(token.tokenString==";"):
                    continue;
                else:
                    break;	
        else:
            print("ERROR : Το πρόγραμμα περίμενε ';' ή υπάρχει προβλημα με τα '{ }' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()	
        if (token.tokenString=="}"):
            token=lexical_analyze()		
        else:
            print("ERROR : Το πρόγραμμα περίμενε '}' or ';' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
    else:
        statement()
        if(token.tokenString==";"):
            token=lexical_analyze()
        else:
            print("ERROR : Το πρόγραμμα περίμενε ';' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
        #print("ERROR : Το πρόγραμμα περίμενε '{' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        #sys.exit()
					

def statement():
    global token,foundreturn
    if(token.tokenType=="keyword"):
    
        name_variable=token.tokenString
        token=lexical_analyze()
        assignStat(name_variable)
    elif (token.tokenString=="if"):
        token=lexical_analyze()
        ifStat()
    elif (token.tokenString=="while"):
        token=lexical_analyze()
		
        whileStat()
    elif (token.tokenString=="switchcase"):
        token=lexical_analyze()
        switchcaseStat()
    elif (token.tokenString=="forcase"):
        token=lexical_analyze()
        forcaseStat()
    elif (token.tokenString=="incase"):
        token=lexical_analyze()
        incaseStat()
    elif(token.tokenString=="call"):
        token=lexical_analyze()	
        callStat()
    elif(token.tokenString=="return"):
        token=lexical_analyze()
        foundreturn=True
        
        returnStat()
    elif (token.tokenString=="input"):
        token=lexical_analyze()
        inputStat()
    elif(token.tokenString=="print"):
        token=lexical_analyze()
        printStat()
    else:
        pass			

def assignStat(name_variable):
    global token
    
    
   
    
    tempVar = searchScope(name_variable)
    if tempVar.name=='Fail':
        
        print("Error: Βρέθηκε μεταβλητη",name_variable," που δεν εχει οριστεί στη γραμμή",token.lineNo)
        sys.exit()
    if(token.tokenString==":="):
        token=lexical_analyze()
        
        name=expression()
        
        genquad(":=",name,"_",name_variable)
    else:	
        print("ERROR : Το πρόγραμμα περίμενε ':=' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()
		
def whileStat():
    global token
    Bquad = nextquad()
    if(token.tokenString=="("):
        token=lexical_analyze()
        l=token.lineNo
        B_true, B_false = condition()
        if(token.tokenString==")"):
            backpatch(B_true,nextquad())
            token=lexical_analyze()
            statements()
            genquad("jump","_","_",str(Bquad))
            backpatch(B_false,nextquad())
        else:
            print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",l,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
    else:
        print("ERROR : Το πρόγραμμα περίμενε '(' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()	
        
def condition():
    global token
    Q1_true, Q1_false = boolterm()
    B_true = Q1_true
    B_false = Q1_false
    
    while(token.tokenString=="or"):
        backpatch(B_false,nextquad())
        token=lexical_analyze()
        Q2_true, Q2_false = boolterm()
        B_true = mergelist(B_true,Q2_true)
        B_false = Q2_false
    return B_true, B_false



def boolterm():
    global token
    R1_true, R1_false = boolfactor()
    Q_true = R1_true
    Q_false = R1_false
    
    while(token.tokenString=="and"):
        backpatch(Q_true,nextquad())
        token=lexical_analyze()
        R2_true, R2_false = boolfactor()
        Q_false = mergelist(Q_false,R2_false)
        Q_true = R2_true
    return Q_true, Q_false



def boolfactor():
    global token
    if(token.tokenString=="not"):
        token=lexical_analyze()
        if(token.tokenString=="["):
            token=lexical_analyze()
            B_true, B_false = condition()
            if(token.tokenString=="]"):
                R_true = B_false
                R_false = B_true
                token=lexical_analyze()
            else:
                print("ERROR : Το πρόγραμμα περίμενε ']' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
                sys.exit()
        else:
            print("ERROR : Το πρόγραμμα περίμενε '[' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
    
		
    elif(token.tokenString=="["):
        token=lexical_analyze()	
        B_true, B_false = condition()
        if(token.tokenString=="]"):
            R_true = B_true
            R_false = B_false
            token=lexical_analyze()
        else:
            print("ERROR : Το πρόγραμμα περίμενε ']' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()	
    else:
        exp1 = expression()
        relop = REL_OP()
        exp2 = expression()

        R_true = makelist(nextquad())
        genquad(relop,exp1,exp2,"_")
        R_false = makelist(nextquad())
        genquad("jump","_","_","_")
    return R_true, R_false
	
def expression():
    global token
    global scopeList,currentScope,numofTMP  ###############
    
    if(token.tokenType=="keyword"):
        serSerTemp = searchScope(token.tokenString) ##
        if token.tokenString    != serSerTemp.name:
           
            print("Error: Βρεθηκε μεταβλητη",token.tokenString , "που δεν έχει οριστεί στη γραμη:", token.lineNo)
            sys.exit()
  
    optionalSing()
    
    if(token.tokenType=="keyword"):
        serSerTemp = searchScope(token.tokenString) ##
        if token.tokenString    != serSerTemp.name:
           
            print("Error: Βρεθηκε μεταβλητη",token.tokenString , "που δεν έχει οριστεί στη γραμη:", token.lineNo)
            sys.exit()
    num1=term()
  
    scope=scopeList[currentScope] ##
    while(token.tokenString=="+" or token.tokenString=="-"):
        op_sing=token.tokenString
        ADD_OP()
        if(token.tokenType=="keyword"):
            serSerTemp = Entity('', '', 0)
            serSerTemp = searchScope(token.tokenString)
            if token.tokenString != serSerTemp.name:
                print("Variable", token.tokenString,"not declared in line ",token.lineNo)
                sys.exit()
        num2=term()
        if(token.tokenType=="keyword"):
            serSerTemp = searchScope(num2)
            if num2 != serSerTemp.name:
               
                print("Error: Βρεθηκε μεταβλητη",num2 , "που δεν έχει οριστεί στη γραμη:", token.lineNo)
                sys.exit()
        temp=newtemp()
        
        serSerTemp = searchScope(temp)
        if "Fail" == serSerTemp.name:

            scoOff=scope.getTotalOffset()
            ent=Entity(temp,"var",scoOff+4)
            scope.addentity(ent)
        genquad(op_sing,num1,num2,temp)
        num1=temp
        
    scopeList[currentScope]=scope
    serSerTemp = searchScope(num1)
    if num1 != serSerTemp.name:
        
        print("Error: Βρεθηκε μεταβλητη",num1 , "που δεν έχει οριστεί στη γραμη:", token.lineNo)
        sys.exit()


    numofTMP=0
    return num1    
		  

def optionalSing():
    global token
    if(token.tokenString=="+" or token.tokenString=="-"):
        token=lexical_analyze() 
        

def term():
    global token
    global numofTMP  ##
    
    num1=factor()
    
    scope=scopeList[currentScope]
    while(token.tokenString=="*" or token.tokenString=="/"): 
       
        op_sing=MUL_OP()
        ##
        
        ##        
        num2=factor()
        ##
        
        #####
        temp=newtemp()
        serSerTemp = searchScope(temp)
        if "Fail" == serSerTemp.name:
            scoOff=scope.getTotalOffset()
            ent=Entity(temp,"var",scoOff+4)
            scope.addentity(ent)
        genquad(op_sing,num1,num2,temp)
        num1=temp
        
    scopeList[currentScope]=scope    
    return num1    
	
def factor():

    global token
    global scopeList,list_of_variables
    scope=scopeList[currentScope]
    if(token.tokenType=="number"):
        num=INTEGER()
        return num
    elif(token.tokenString=="("):
        token=lexical_analyze()
        num=expression()
        if(token.tokenString!=")"):
			
            print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
        token=lexical_analyze()
        return num
    elif(token.tokenType=="keyword"):
        
        variable=token.tokenString
       
        token=lexical_analyze()
        
        have_func,parameters=idtail(variable)  ###
        if (have_func):
            func_name=variable
           
            idret=newtemp()
            ########
            s=scopeList[0]
            serSerTemp = Entity('', '', 0)
            serSerTemp = searchScope(idret)
            if 	"Fail" == serSerTemp.name:
                ent=Entity(idret,"var",s.getTotalOffset()+4)
                s.addentity(ent)
                scopeList[0]=s
             ##############   
            for param in parameters:
                genquad("par", param[0], param[1], "_")
            genquad("par", idret, "RET", "_")
            genquad("call", func_name, "_", "_")
            return idret
        else:
            return variable
    else:
		
        print("ERROR : Το πρόγραμμα περίμενε 'αριθμό' ή '(' ή 'ονομα μεταβλητης' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()

                   	
def printStat():
    global token
    if(token.tokenString=="("):
        token=lexical_analyze()
        exp = expression()
        genquad("out",exp, "_","_")
        if(token.tokenString==")"):
            token=lexical_analyze()
        else:
            print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
    else:			
        print("ERROR : Το πρόγραμμα περίμενε '(' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()
            
		
def returnStat():
    global token
    global variableforSeeReturnCheck,functionL,inFunction
    if(token.tokenString=="("):
        token=lexical_analyze()
        exp = expression()
        genquad("retv",exp,"_","_")
        
        
      
        if(inFunction==False):
            
            print("Error: Βρεθηκε Retutn εκτός {} συνάρτησης στη γραμμη:", token.lineNo)
            sys.exit()
        if(token.tokenString==")"):
            token=lexical_analyze()
        else:
            print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
    else:
        print("ERROR : Το πρόγραμμα περίμενε '(' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()     		    	

def inputStat():
    global token

    if(token.tokenString=="("):
        token=lexical_analyze()
        if(token.tokenType=="keyword"):
            idplace = token.tokenString
            id_place=searchScope(idplace)
            if id_place.name!=idplace:
               
                print("Error: Προσπάθεια αρχικοποιησης μεταβλητής","'",idplace,"'", "που δεν ειναι ορισμένη στη γραμμή:",token.lineNo)
                sys.exit()
            token=lexical_analyze()
            genquad("inp",idplace,"_","_")
            if(token.tokenString==")"):
                token=lexical_analyze()
            else:
                print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
                sys.exit()	
        else:
            print("ERROR : Το πρόγραμμα περίμενε 'όνομα μεταβλητής' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
    else:
        print("ERROR : Το πρόγραμμα περίμενε '(' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()

def REL_OP():
    global token
    l=token.lineNo
    if(token.tokenString=="=" or token.tokenString=="<=" or token.tokenString==">=" or token.tokenString==">" or token.tokenString=="<" or token.tokenString=="<>"):
        rel_op=token.tokenString
        token=lexical_analyze()
    else:	
        print("ERROR : Το πρόγραμμα περίμενε 'εναν λογικό τελεστή = ,<=, >=, >, <, <>' στη γραμμή:",token.lineNo,"/nΒρέθηκε ",token.tokenString)
        sys.exit()	    
    return rel_op
   
def MUL_OP():

    global token
	
    if(token.tokenString=="*" or token.tokenString=="/"):
        mul_op=token.tokenString
        token=lexical_analyze()
        
    else:	
        print("ERROR : Το πρόγραμμα περίμενε '*' ή '/' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()	
    return mul_op

def ADD_OP():
    global token
    if(token.tokenString=="+" or token.tokenString=="-"):
        add_op=token.tokenString
        token=lexical_analyze()
    else:	
        print("ERROR : Το πρόγραμμα περίμενε '+' ή '-' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()
    return add_op

def ifStat():
    global token
    if(token.tokenString=="("):
        token=lexical_analyze()
        
        b_true,b_false=condition()   ##
        
        if(token.tokenString==")"):
            token=lexical_analyze()
            backpatch(b_true,nextquad())  ##
            statements()
            if_list=makelist(nextquad())     ##
            genquad("jump","_","_","_")   ##
            backpatch(b_false,nextquad()) ##
            elsepart()
            backpatch(if_list,nextquad())  ##
        else:
            print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()	
    else:

        print("ERROR : Το πρόγραμμα περίμενε '(' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)

        sys.exit()


def elsepart():
    global token
    if(token.tokenString=="else"):
        token=lexical_analyze()
        statements() 	

def incaseStat():
    global token
    w=newtemp()
    p1Quad=nextquad()
    genquad(":=",1,"_",w)
    
    if(token.tokenString=="case"):
        while(1):       
            token=lexical_analyze()
            if(token.tokenString=="("):
                token=lexical_analyze()
                cond_true,cond_false=condition()
                if(token.tokenString==")"):
                    token=lexical_analyze()
                    backpatch(cond_true,nextquad())
                    genquad(":=",0,"_",w)
                    statements()
                    backpatch(cond_false,nextquad())
                    if(token.tokenString=="case"):
                        continue;
                    else:
                        genquad("=",w,0,p1Quad)   
                        break;
                else:	
                    print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
                    sys.exit()
            else:
                print("ERROR : Το πρόγραμμα περίμενε '(' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
                sys.exit()
    else:   
        print("ERROR : Το πρόγραμμα περίμενε 'case' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()    



def forcaseStat():
    global token
   
    p1Quad=nextquad()
    while(token.tokenString=="case"):
        token=lexical_analyze()
        if(token.tokenString=="("):
            token=lexical_analyze()
            cond_true,cond_false=condition()
            if(token.tokenString==")"):
                token=lexical_analyze()
                backpatch(cond_true,nextquad())
                statements()
                
                genquad("jump","_","_",p1Quad)
                backpatch(cond_false,nextquad())
            else:		
                print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
                sys.exit()	
        else:
            print("ERROR : Το πρόγραμμα περίμενε '(' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()					
    if(token.tokenString=="default"):
        token=lexical_analyze()
        statements()
    else:	
        print("ERROR : Το πρόγραμμα περίμενε 'case' ή 'default' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()
        #pass


def switchcaseStat():

    global token,l
    exitlist = emptylist()
    while(token.tokenString=="case"):
        token=lexical_analyze()
        if(token.tokenString=="("):
            token=lexical_analyze()
            cond_true,cond_false=condition()
            if(token.tokenString==")"):
                token=lexical_analyze()
                backpatch(cond_true,nextquad())
                statements()
                e=makelist(nextquad())
                genquad("jump","_","_","_")
                exitlist= mergelist(exitlist,e)  
                
                backpatch(cond_false,nextquad())
                
            else:			
                print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
                sys.exit()	
        else:
            print("ERROR : Το πρόγραμμα περίμενε '(' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
    
    if(token.tokenString=="default"):
        token=lexical_analyze()
        statements()
        backpatch(exitlist,nextquad())
    else:		
        print("ERROR : Το πρόγραμμα περίμενε 'case' ή 'default' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()
        pass
	
	
def callStat():

    global token,procedureL
    global variableforSeeReturnCheck ###
    if(token.tokenType=="keyword"):
        call_name=token.tokenString
       
        if(call_name not in procedureL):
            print("Error")
            sys.exit()
        token=lexical_analyze()
        if(token.tokenString=="("):
            token=lexical_analyze()
            parameters=actualparlist(call_name) 
            if(token.tokenString==")"):
                w = newtemp()
                s=scopeList[0]
                serSerTemp = Entity('', '', 0)
                serSerTemp = searchScope(w)
                if 	"Fail" == serSerTemp.name:##pi8anwn la8os apo ena tab
                    ent=Entity(w,"var",s.getTotalOffset()+4)
                    s.addentity(ent)
                    scopeList[0]=s
                token=lexical_analyze()
                for param in parameters:
                    genquad("par", param[0], param[1], "_")
                genquad("call",call_name,"_","_")
            else:
                print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
                sys.exit()
        else:
            print("ERROR : Το πρόγραμμα περίμενε '(' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()    
    else:
        print("ERROR : Το πρόγραμμα περίμενε 'όνομα μεταβλητής 'στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()
            				
def INTEGER():
    global token
    if(token.tokenType=="number"):
        num=token.tokenString
        token=lexical_analyze()
        return num
		
    else:
        print("ERROR : Το πρόγραμμα περίμενε 'εναν ακεραιο αριθμο' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()

##### INTERMEDIETE CODE ########### 


class Quad:
    def __init__(self, ID, op, x, y, z):
        self.ID = int(ID)
        self.op = str(op)
        self.x = str(x)
        self.y = str(y)
        self.z = str(z)

    def myfunc(self):
        print( self.ID,":"+self.op+","+self.x +","+self.y+","+self.z)
        
    def metatroph(self):
        
        return str(self.ID) +" : "+self.op+" , "+self.x +" , "+self.y+" , "+self.z


def nextquad():
    global counter_next_quad
    
    return counter_next_quad+1

def genquad(op, x, y, z):
    global quadList, counter_next_quad
   
    counter_next_quad = nextquad()
    
    quad=Quad(counter_next_quad,op,x,y,z)
    quadList.append(quad)
    
    
        
def newtemp():
    global T_i,list_of_variables
    # Temp variable    
    T_i += 1
    list_of_variables.append("T_" + str(T_i))      ##
    return "T_" + str(T_i)

def emptylist():
    mylist=[]
    return mylist
    
def makelist(x):
   lst=[]
   lst.append(x)
   return lst

def mergelist(list1, list2):

    mergedList = list1+ list2
    return mergedList

def backpatch(lst,z):
    global quadList
    
    for quad in quadList:
        if  quad.ID in lst:
            quad.z=str(z)
  


def find_variable():

    global list_of_variables
    for q in quadList:
        if (str(q.op) in ("+", "-", "*", "/", ":=", "<", ">", ">=", "<=", "<>", "=")):
            if ((not (q.z in list_of_variables )) and (str(q.z) != "_") and (not str(q.z).isdigit())):
                list_of_variables.append(str(q.z))

    


  
def intFileGen():
    global intFile, quadList
    
    intFile.write("//Name: Lampros Vlaxopoulos\t AM: 2948\t username: cse52948\n")
    intFile.write("//Name: Georgios Krommydas\t  AM: 3260\t username: cse63260\n\n")
    
    for i in range(len(quadList)):
        intFile.write(str(quadList[i].metatroph()))
        intFile.write('\n')

def cFileGen():
    global cFile,list_of_variables
    
    cFile.write("//Name: Lampros Vlaxopoulos\t AM: 2948\t username: cse52948\n")
    cFile.write("//Name: Georgios Krommydas\t  AM: 3260\t username: cse63260\n\n")
    cFile.write("#include <stdio.h>\n\n")
    cFile.write("int main(){\n")
    cFile.write("\tint ")
    find_variable()
    
    for i in range(len(list_of_variables)):
        cFile.write(str(list_of_variables[i]))
        if (len(list_of_variables) == i+1):
            cFile.write(";\n\n")
        else:
            cFile.write(", ")
    for q in quadList:
        if (q.op == "begin_block"):
            cFile.write("\tL_"+str(q.ID)+ ": ")
            cFile.write("\t//" + q.metatroph() + "\n")
        elif (q.op == ":="):
            cFile.write("\tL_"+str(q.ID) + ": " + str(q.z) + " = " + str(q.x) + "; ")
            cFile.write("\t//" + q.metatroph() + "\n")
        elif (q.op in('+','-','*','/')):
            cFile.write("\tL_"+str(q.ID) + ": " + str(q.z) + " = " + str(q.x) + q.op + str(q.y) + "; ")
            cFile.write("\t//" + q.metatroph() + "\n")
        elif (q.op == "jump"):
            cFile.write("\tL_"+str(q.ID) + ": " + "goto L_" + str(q.z) +"; ")
            cFile.write("\t//" + q.metatroph() + "\n")
        elif (q.op in ('=', '<>', '<', '<=', '>', '>=')):
            op=q.op
            if op == '=':
                op = '=='
            elif op == '<>':
                op = '!='
            cFile.write("\tL_"+str(q.ID) + ": " + "if (" + str(q.x) + op + str(q.y) + ") goto L_" + str(q.z) + "; ")
            cFile.write("\t//" + q.metatroph() + "\n")
        elif (q.op == "out"):
            cFile.write("\tL_"+str(q.ID) + ": " + "printf(\"" + str(q.x) + " = %d\\n\", " + str(q.x) + ");")
            cFile.write("\t//" + q.metatroph() + "\n")
        elif (q.op == "inp"):
            cFile.write("\tL_"+str(q.ID) + ": " + "scanf(\"%d" + "\", &" + q.x + ");")
            cFile.write("\t//" + q.metatroph() + "\n")
        elif (q.op == "halt"):
            cFile.write("\tL_"+str(q.ID) + ": " + "return 0; ")
            cFile.write("\t//" + q.metatroph() + "\n")
        elif (q.op == "end_block"):
            cFile.write("\tL_"+str(q.ID) + ": {}")
            cFile.write("\t//" + q.metatroph() + "\n")
            cFile.write("} ")

    
 ################### Symbol Table ############################

class Entity:

    def __init__(self,name,typeofEntity,offset):
        self.name=str(name)
        self.typeofEntity=str(typeofEntity)
        self.offset = offset
        self.startQuad = 0
        self.parMode = ""
        self.listOFArguments = []
        self.nextEntity= 0
        self.varType = "int"
        self.framelength = 0
    def setframelength(self,fl):
        self.framelength=fl
    '''def setVarType(self,vType):
        self.varType = vType'''

    '''def setEntity(self,nextE):
        self.nextEntity=nextE'''

    def setParMode(self,par):
        self.parMode=par

    def setArgument(self,nextA):
        self.listOFArguments.append(nextA)

    def setstartQuad(self,starQ):
        self.startQuad=starQ

    def changeoffset(self,newoffset):
        self.offset=newoffset

    def returnoffset(self):
        return self.offset

    def returnArgumentList(self):
        return self.listOFArguments

    def printer(self):
        print('Name:',self.name + ":" + "Offset " +str(self.offset) + " Type of entity "+self.typeofEntity+ " Par "+self.parMode)
        x=str("Name: ")+str(self.name) + str(" : ") + str(" Offset ") +str(self.offset) + str(" Type of entity ")+str(self.typeofEntity)+ " Par "+str(self.parMode)
        if self.typeofEntity == "function" or self.typeofEntity == "procedure":
            print("NextQuad",self.startQuad,"Framelength",self.framelength)
            x=str(x)+str("\nNextQuad ")+str(self.startQuad)+" Framelength "+str(self.framelength)
        return x    


class Scope:
    def __init__(self,nestingLevel):
        self.nestingLevel=nestingLevel
        self.listofEntitys = []
        self.enclosingScope = False

    '''def setScopeClosed(self):
        self.enclosingScope = True'''

    def addentity(self,entitytoadd):
        self.listofEntitys.append(entitytoadd)

    def printScope(self):
        print(self.nestingLevel)
        return(str(self.nestingLevel))

    def setListOfEntitys(self,entLi):
        self.listofEntitys=entLi

    def getTotalOffset(self):
        if len(self.listofEntitys)==0:
            return 0
        else:
            ent=self.listofEntitys[-1]
            entsoff=ent.returnoffset()
            return entsoff

    def returnListOfEntitys(self):
        return self.listofEntitys

    def varLocal(self,Varname):
        for x in self.listofEntitys:
            if x.name == Varname.strip():
                
                return 1
        return 0

class Argument:
    global argumentuniqeID
    argumentuniqeID=argumentuniqeID+1
    def __init__(self,parMode,typeOfArg):
        self.parMode=parMode
        self.typeofArgument = typeOfArg
        self.argumentID=argumentuniqeID
        self.nextArgument =0

    '''def compare(self,arg2):
        result=True
        if self.parMode!=arg2.parMode:
            result= False
        return result'''
    def printerArg(self):
        print(str(self.parMode)+"   ")
        return(str(self.parMode)+"   ")

    '''def tonextArgument(self,nextArg):
        self.nextArgument=nextArg'''


def searchScope(searchElement):
    vforreturn =Entity("Fail",'int',0)
    nameTostrip = ''
    for scope in scopeList:
        entititiesList=scope.returnListOfEntitys()
        for enti in entititiesList:
            if enti.name==searchElement:
                
                vforreturn=enti
                nameTostrip = vforreturn.name
                nameTostrip.strip()
                vforreturn.name = nameTostrip
            elif searchElement.isdigit():
                vforreturn.name= searchElement
    ###alages gia thn epistrofh san antikimeno enity kai alages ekei pou xrisimopiousame thn synarthsh


    return vforreturn
 
########### SEMATIC ANALYSIS ############

def Symasiologikh_analysh():
    global List_after_delete_scope, listofFuncPars,functionL 
    ##elexoi an otan kaloume mia synarthsh an einai idoi oi parametoi kai me thn idia seira
    #Ελεγχοι για το όταν καλούμε ένα subprogramm αν καλείτε με τους σωστους παραμετρους και με την ίδια σειρα
    for x in listofFuncPars:
        for y in List_after_delete_scope:
            search_froniter=y.returnListOfEntitys()
           
            for z in search_froniter:
                
                if x.name==z.name:
                    if len(z.returnArgumentList())==len(x.returnArgumentList()):
                        i=0
                        list_arg=z.returnArgumentList()
                        list_arg2=x.returnArgumentList()
                        while(i<len(z.returnArgumentList())):
                            arg=list_arg[i]
                            arg2=list_arg2[i]
                            if arg.parMode != arg2.parMode :
                                print("Detected a wrong parameter in funtion ",x.name)
                                print("Error: Found a wrong parameter in function or procedure with name:",x.name)
                                sys.exit()
                            i=i+1
                    else:
                        if(x.name in functionL):
                            continue;
                        else:    
                            print("Detected a wrong parameter in funtion ",x.name,"htht ")
                            print("Error: Found a wrong parameter in function or procedure with name:",x.name)
                            sys.exit()
    ##kanei update ola ta framelength
    for x in List_after_delete_scope:
        xlist=x.returnListOfEntitys()
        entiFunc = xlist[0]
        lastoffset= xlist[-1]
        entiFunc.setframelength(x.getTotalOffset())
        xlist[0]=entiFunc
        for y in List_after_delete_scope:
            ylistofentity=y.returnListOfEntitys()
            for yl in ylistofentity:
                if entiFunc.name==yl.name:
                    yl.setframelength(x.getTotalOffset())


########### SYMBOL TABLE #############
def printSymbolTable():## kanei print ta scopes
    
    global List_after_delete_scope,SymbolTableFile
    
    
    for xo in List_after_delete_scope:
        print("\n-------------------------------------------------------------------------")
        SymbolTableFile.write("\n---------------------------------------------------------\n")
        SymbolTableFile.write(xo.printScope()+"\n")
        print("\n=========================================================================\n")
        
        SymbolTableFile.write("\n=========================================================================\n")
        ls=xo.returnListOfEntitys()
        for l in ls:
            SymbolTableFile.write(str(l.printer())+"\n")
            a=l.returnArgumentList()
            for arg in a:
                SymbolTableFile.write(arg.printerArg()+"\n")
        print("---------------------------------------------\n")
        SymbolTableFile.write("---------------------------------------------------------\n")

######### FINAL CODE ################
def gnlvcode(v):
    global nesting
    for x in scopeList:
        scope=x
        listforentitys = scope.returnListOfEntitys()
        for ent in listforentitys:
            if ent.name == v :
                v = ent
                i = scope.nestingLevel

    x=nesting
    gnvlcodeReturn = 'lw $t0,-4($sp)\n'
    while 1:
        x = x+1
        if x >= i:
            break
        gnvlcodeReturn = gnvlcodeReturn + '\t\tlw $t0, -4($t0)\n'

    gnvlcodeReturn = gnvlcodeReturn + '\t\taddi $t0,$t0,-' + str(v.offset) + '\n'
    return gnvlcodeReturn

def loadvar(quadvar,tempregister):
    global nesting
    i =-1
   
    for scope in scopeList:
        listforentitys = scope.returnListOfEntitys()
        m=listforentitys[0]
        for ent in listforentitys:
            if ent.name == quadvar and i==-1:
                v = ent
                i = scope.nestingLevel
               
               

     
    if quadvar.isdigit():
        loadvarReturn = 'li $t'+str(tempregister)+','+str(quadvar)+'\n'
    elif i == 1 :
        loadvarReturn = 'lw $t'+str(tempregister)+',-' +str(v.offset)+'($s0)\n'
        
    elif (v.parMode == '' and i == nesting) or( v.parMode == 'in' and i == nesting) or (quadvar[0:2] == "T_"):
        loadvarReturn = 'lw $t'+str(tempregister)+',-' + str(v.offset)+'($sp)\n'
    elif  v.parMode == 'inout' and i==nesting :
        loadvarReturn = 'lw $t0,-'+str(v.offset)+'($sp)\n\t\t' + 'lw $t' + str(tempregister)+',($t0)\n'
    elif v.parMode == '' and i == nesting or v.parMode == 'in' or i < nesting:
        loadvarReturn = gnlvcode(v.name) + '\t\tlw $t'+ str(tempregister)+',($t0)\n'
    elif v.parMode == 'inout' and i < nesting:
        loadvarReturn = gnlvcode(quadvar) + '\t\tlw $t0,($t0)\n' + '\t\tlw $t'+ str(tempregister)+ ',($t0)\n'
    else:
        loadvarReturn = 'Error in loadvar\n'
        print(loadvarReturn)
    return '\t\t'+loadvarReturn
       

def storevar(r,v):
    global nesting
    i=-1
   
    for scope in scopeList:
        listforentitys = scope.returnListOfEntitys()
        for ent in listforentitys:
            if ent.name == v and i == -1:
                v = ent
                i = scope.nestingLevel
                
                
                break
    
   
    scope = scopeList[0]
    
    localVar = scope.varLocal(v.name)
    
 
    if i == 1:
        storevarReturn = 'sw $t' + str(r) + ',-' + str(v.offset) + '($s0)\n'
    elif (localVar == 1) and not(v.parMode == 'inout' and i == nesting) or (v.name[0:2] == "T_") or (v.parMode == 'in' and i == nesting):
        
        storevarReturn = 'sw $t' + str(r) + ',-' + str(v.offset) + '($sp)\n'
    elif v.parMode == 'inout' and i == nesting:
        
        storevarReturn = 'lw $t0, -' +str(v.offset) + '($sp)\n\t\t' + 'sw $t'+str(r)+',($t0)\n'
    elif v.parMode == '' and localVar == 1 or v.parMode == 'in' or i < nesting:
        
        storevarReturn = gnlvcode(v.name) + '\t\tsw $t' +str(r) +'($t0)'
    elif v.parMode == 'inout' and i < nesting:
        storevarReturn = gnlvcode(v.name) + '\t\tlw $t0,($t0)' + '\n\t\tsw $t' + str(r) + '($t0)\n'
    else:
        torevarReturn = 'Error in storevar'
            
    return '\t\t' + storevarReturn
    
    
   
   
def FinalCode_Transformer(quad):
    global currentScope,nesting,frameLengthValu,scopeList,main_program_name,List_after_delete_scope
    global counter_fake #counter_next_quad ## counter gia parametrous L_
    flag = True
    
    if quad.op == 'jump':
        ret = '\t\tj L_' + str(quad.z)
    elif quad.op == '+':
        
        ret = (loadvar(quad.x, 1) + loadvar(quad.y, 2) + '\t\tadd ' + '$t' + str(1) + ',$t' + str(1) + ',$t' + str(2) + '\n' +storevar(1,quad.z)) #flag_num
    elif quad.op == '-':
        ret = (loadvar(quad.x, 1) + loadvar(quad.y, 2) + '\t\tsub ' + '$t' + str(1) + ',$t' + str(1) + ',$t' + str(2) + '\n' +storevar(1,quad.z))
    elif quad.op == '*':
        ret = (loadvar(quad.x, 1) + loadvar(quad.y, 2) + '\t\tmul ' + '$t' + str(1) + ',$t' + str(1) + ',$t' + str(2) + '\n' +storevar(1,quad.z))
    elif quad.op == '/':
        ret = (loadvar(quad.x, 1) + loadvar(quad.y, 2) + '\t\tdiv ' + '$t' + str(1) + ',$t' + str(1) + ',$t' + str(2) + '\n' +storevar(1,quad.z))
    elif quad.op == '=':
        ret = loadvar(quad.x, 1) + loadvar(quad.y, 2) +'\t\tbeq $t' + str(1) + ',$t' + str(2) + ',L_' + str(quad.z)
    elif quad.op == '<':
        ret = loadvar(quad.x, 1) + loadvar(quad.y, 2) +'\t\tblt $t' + str(1) + ',$t' + str(2) + ',L_' + str(quad.z)
    elif quad.op == '>':
        ret = loadvar(quad.x, 1) + loadvar(quad.y, 2) +'\t\tbgt $t' + str(1) + ',$t' + str(2) + ',L_' + str(quad.z)
    elif quad.op == '<=':
        ret = loadvar(quad.x, 1) + loadvar(quad.y, 2) +'\t\tble $t' + str(1) + ',$t' + str(2) + ',L_' + str(quad.z)
    elif quad.op == '>=':
        ret = loadvar(quad.x, 1) + loadvar(quad.y, 2) +'\t\tbge $t' + str(1) + ',$t' + str(2) + ',L_' + str(quad.z)
    elif quad.op == '<>':
        ret = loadvar(quad.x, 1) + loadvar(quad.y, 2) +'\t\tbne $t' + str(1) + ',$t' + str(2) + ',L_' + str(quad.z)
    elif quad.op == ':=':
        
        ret = loadvar(quad.x,1) + storevar(1,quad.z)
    elif quad.op == 'begin_block':
        flag = False
        if quad.x == main_program_name:
            currentScope = -1
            nesting = 1
            for scope in List_after_delete_scope:
                if scope.nestingLevel == 1:
                    frameLengthValu = scope.getTotalOffset()
            ret = '#---------------------------------------------\n\n'
            
             
            ret = ret + '\tLmain:\n' + "\t\t" + 'addi $sp,$sp,' + str(frameLengthValu)+ '\n\t\t' + 'move $s0,$sp'
        else:
            currentScope = 0
            for scope in List_after_delete_scope:
                if scope.nestingLevel > 1:
                    listofentitys=scope.returnListOfEntitys()
                    entity=listofentitys[0]
                    if entity.name == quad.x:
                        frameLengthValu=entity.framelength
                        nesting=scope.nestingLevel
            ret = '#---------------------------------------------\n\n'
            ret = ret + '\t' + quad.x + ':' + '\n\t\t'+ 'sw $ra,($sp)' 
    elif quad.op == 'end_block':
    ##########
        #flag=False
        if quad.x in procedureL:
           
            temp=scopeList.pop(0)
            temp=temp.returnListOfEntitys()
            temp=temp[0]
            ret = '\t\tlw $ra,($sp)' + '\n\t\t'+ 'jr $ra'
            
            
     ##########       
        elif quad.x in functionL:    
            
            temp=scopeList.pop(0)
            temp=temp.returnListOfEntitys()
            temp=temp[0]
            ret = '\t\tlw $ra,($sp)' + '\n\t\t'+ 'jr $ra'
        else:
            ret=''
    elif quad.op == 'halt':
        ret = '\t\tli $v0,10\n\t\t' + 'syscall'
    elif quad.op == 'inp':
        v = searchScope(quad.x)
        ret = '\t\tli $v0,5\n\t\t' + 'syscall\n\t\t' + '\n\t\tmove $t0,$v0\n\t\t' + storevar(0,v)
    elif quad.op == 'out':
        v = searchScope(quad.x)
        ret = '\t\tli $v0,1\n' +loadvar(v.name,0)+ '\n\t\tmove $a0,$t0' + '\n\t\t' + 'syscall'   
    elif quad.op == 'retv':
        ret = loadvar(quad.x,1) + "\t\tlw $t0,-8($sp)"+"\n\t\tsw $t1,($t0)"#+ "\n\t\tlw $ra,($sp)" + "\n\t\tjr $ra"      #+ '\t\tmove $v0,$t1\n\t\tlw $ra,($sp)' + '\n\t\tjr $ra'
    elif quad.op == 'par' and quad.y == 'CV':
        flag_num=0
        if counter_fake ==0:
            for q in quadList:
                if q.ID == quad.ID:
                    flag_num = -1
                elif flag_num == -1 and q.op == 'call':
                    flag_num = searchScope(q.x)
                    frameLength=flag_num.framelength
                    break

            ret = '\t\taddi $fp,$sp,' + str(frameLength) + '\n'
        else:
            ret = ''

        temp = 12+4*counter_fake
        counter_fake = counter_fake+ 1
        ret = ret + loadvar(quad.x,1) + '\t\tsw $t1, -'+ str(temp) +'($fp)' ##όπου i ο αύξων αριθμός της παραμέτρου
    elif quad.op == 'par' and quad.y == 'RET':
        flag_num=0
        if counter_fake ==0:
            for q in quadList:
                if q.ID == quad.ID:
                    flag_num = -1
                elif flag_num == -1 and q.op == 'call':
                    flag_num = searchScope(q.x)
                    frameLength=flag_num.framelength
                    break

            ret = '\t\taddi $fp,$sp,' + str(frameLength) + '\n'
        else:
            ret = ''
        s=searchScope(quad.x)
        counter_fake = counter_fake+1
        ret = ret + '\t\taddi $t0,$sp,-'+ str(s.offset) + '\n\t\tsw $t0,-8($fp)'
    elif quad.op == 'par' and quad.y == 'REF':
        
        flag_num=0
        if counter_fake ==0:
            for q in quadList:
                if q.ID == quad.ID:
                    flag_num = -1
                elif flag_num == -1 and q.op == 'call':
                    flag_num = searchScope(q.x)
                    frameLength=flag_num.framelength
                    break
            ret = '\t\taddi $fp,$sp,' + str(frameLength) + '\n'
        else:
            ret = ''

        temp = 12 + 4 * counter_fake
        counter_fake = counter_fake + 1
        v = searchScope(quad.x.strip())
        scope=scopeList[0]
        localVar=scope.varLocal(v.name)
        ret ='Error!!!!'
        for scope in scopeList:
            if 1 == scope.varLocal(v.name):
                variableNesting=scope.nestingLevel

        if nesting == variableNesting or v.parMode == 'in' and localVar == 1:
            
            ret = '\t\taddi $t0,$sp,-'+ str(v.offset) + '\n\t\tsw $t0,-'+ str(temp) +'($fp)'
        elif nesting == variableNesting or v.parMode == 'inout':
            
            ret = '\t\tlw $t0,-'+str(v.offset)+'($sp)' +'\n\t\tsw $t0,-'+str(temp) +'($fp)'
        elif nesting != variableNesting or localVar ==1 or v.parMode == 'in':
            
            ret = gnlvcode(v.name) + '\t\tsw $t0,-' +str(temp) +'($fp)'
        elif nesting != variableNesting or v.parMode=='inout':
            
            ret = gnlvcode(v.name) + '\t\tlw $t0,($t0)' + '\n\t\tsw $t0,-' + str(temp) + '($fp)'
    elif quad.op == 'call':
        for scope in List_after_delete_scope:
            entityList= scope.returnListOfEntitys()
            for ent in entityList:
                if ent.name == quad.x and counter_fake >0:
                    i=scope.nestingLevel
                    counter_fake=0
                    
        frameLengthValu=searchScope(quad.x)
        if i == nesting:
            ret = '\t\tlw $t0,-4($sp)\n' + '\t\tsw $t0,-4($fp)\n'   
        else:
            ret = '\t\tsw $sp,-4($fp)\n'                            
       
        ret =ret + '\t\taddi $sp,$sp,'+str(frameLengthValu.framelength) + '\n\t\tjal '+ quad.x + '\n\t\taddi $sp,$sp,'+ str(-frameLengthValu.framelength)  
    else:
        ret = "Error: Cannot convert instructions to assembly!!!!"

    if flag == True:
        ret = '\tL_' + str(quad.ID) + ': \n' + ret
    return ret
    
def FinalCode_Generator_File(finalCodeFile):

    global counter_fake,quadList
    
    counter_fake=0
    finalCodeFile.write('#---------------------------------Global data as used in main \n')

    finalCodeFile.write('\t.text\n')
    finalCodeFile.write('\tj Lmain\n')
    for quad in quadList:
        q = FinalCode_Transformer(quad)
        
        finalCodeFile.write(q +'\t\t# '+ "%s" % int(quad.ID)+":"+str(quad.op)+"," +
                    str(quad.x)+","+str(quad.y)+","+str(quad.z)+ '\n')




def main(args):
    global infile,quadList,intFile,cFile,list_of_variables,have_sub_program,scopeList,SymbolTableFile
	
    if(len(args) !=2):
        print("Error in parsing: Not enough arguments. Files are missing!")
        sys.exit()
		
    in_file=args[1]
    if (not in_file.endswith('.ci')):
        print("Error: The file should end with '.ci' ")
        exit()	
	
    try:
        infile = open(in_file, "r")
        intFile = open("int_file.int","w")
        
    except OSError:
        print("Error: The system cannot open the file!")
        sys.exit()
      		
    syntax_analyze()
    intFileGen()
    Symasiologikh_analysh()
    scopeList=List_after_delete_scope.copy()
    try:
        SymbolTableFile = open("SymbolTableFile.txt","w")
     
    except OSError:
        print("Error: The system cannot open the file!")
        sys.exit()
    printSymbolTable()
    SymbolTableFile.close()
    if have_sub_program==False:
        try:
            cFile = open("C_file.c","w")
       
        
        except OSError:
            print("Error: The system cannot open the file!")
            sys.exit()
            
        
        cFileGen()
        cFile.close()
   
    finaclCodeFile = ".asm"
    fCode= open("final.asm",'w')
    FinalCode_Generator_File(fCode)
    scopeList=List_after_delete_scope.copy()
    
    infile.close()
    intFile.close()
    fCode.close()

if __name__ =="__main__":
	main(sys.argv)