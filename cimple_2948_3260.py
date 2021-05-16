## Ονοματεπώνυμο : Λάμπρος Βλαχόπουλος , ΑΜ : 2948 , username : cse52948 
## Ονοματεπώνυμο : Γιώργος Κρομμύδας   , ΑΜ : 3260 , username : cse63260  



import sys 

global list

list=['program',
    'declare',
    'if',
    'else',
    'while',
    'switchcase',
    'forcase',
    'incase',
    'case',
    'default',
    'not',
    'and',
    'or',
    'function',
    'procedure',
    'call',
    'return',
    'in',
    'inout',
    'input',
    'print'
    ]

T_i=0 
counter_next_quad=0
quadList=[]
main_program_name=""
have_sub_program=False
list_of_variables=[]
subProgramType=""
subprogram_name=""
scopesList=[]
Lmain_Flag = True

class Token:
 
    def __init__(self, tokenType, tokenString, lineNo):
    
        self.tokenType=tokenType
        self.tokenString=tokenString
        self.lineNo=lineNo
    
##Λεκτική Ανάλυση
counter_for_lines=1
def lexical_analyze():

    global  counter_for_lines
    
    tokenString= []        ##λεκτική μονάδα
    counter_for_letters = 0      #μετρητης γραμμάτων
    
    char=infile.read(1)      #Διαβάζω 1 χαρακτήρα
    
    # start                                      #Το while υλοποιεί την κατάσταση με τους λευκούς χαρακτηρες space kai newline.
    while True:
    	 if char==" " or char=="\t"  :
             
            char=infile.read(1)
    	 elif char.isspace():
    	 	if char =="\n" :
    	 		counter_for_lines+=1
    	 		return lexical_analyze()
            
    	 else:       
       
            break
    
    
    #number
    if (char.isdigit()):
        tokenString.append(char)
        
        char=infile.read(1)
        
        while(char.isdigit()):
        
            tokenString.append(char)
            char=infile.read(1)
            
        infile.seek(infile.tell()-1) ########ΑΦου κροιφοκοιτάξω μεσα στο while και βρω κάτι αλλο απο κάθε κατάσταση γυρνάω μια θέση πίσω τον μετρητη του αρχειου που μου δειχνει τη θεση # infile.tell() μετρητης τρεχουσας θεσης  # infile.seek() βαζω εγω το μετρητη στη θεση που θελω 
        
        if char.isalpha():
        	
        	t=''.join(tokenString)
        	print("Error : Δημιουργετε String που ξεκινά με αριθμούς(",t,") στη γραμμή: ",counter_for_lines)
        	sys.exit()
                
        number=''.join(tokenString)
        if (int(number) < -(pow(2,32)-1) or int(number) >(pow(2,32) -1) ):     #ελεγχος για το αν ο αριθμος ειναι αποδεκτος απο τη γλωσσα
            print("Ο αριθμός ",number, "είναι έξω από τα όρια 2^32 -1")
            sys.exit()
          
       
        return Token("number",number.strip(),counter_for_lines)
        sys.exit()
        
        
     #identifier/keywordString
    elif (char.isalpha()):
        counter_for_letters+=1
        tokenString.append(char)
        char=infile.read(1)
        
        while (char.isalpha() or char.isdigit() ):
            tokenString.append(char)
            counter_for_letters+=1
            char=infile.read(1)
           
          
        infile.seek(infile.tell()-1)   
        tokenString=''.join(tokenString)
       
        if counter_for_letters<=30:
        
           
             if(tokenString.strip() in list): 
                type="identifier"
             else:
                type="keyword"
             return Token(type,tokenString.strip(),counter_for_lines)
             sys.exit()
        else:
            print("Το string",tokenString.strip()," ειναι εκτός ορίων καθώς η γλώσσα υποστηρίζει keywords μέχρι και 30 χαρακτηρες\n")
          
            sys.exit()
     #addOperator  
    elif char=="+":
        addOperator="+"
      
        return Token("addOperator",addOperator.strip(),counter_for_lines)
        sys.exit()
        
    elif char =="-":
        addOperator="-"
       
        return Token("addOperator",addOperator.strip(),counter_for_lines)
        sys.exit()
     #mulOperator  
    elif char =="*":
        mulOperator="*"
      
        return Token("mulOperator",mulOperator.strip(),counter_for_lines)
        sys.exit()
     
    elif char =="/":
        mulOperator="/"
     
        return Token("mulOperator",mulOperator.strip(),counter_for_lines)
        sys.exit()
     #groupSymbol
    elif char=="{":
        groupSymbol="{"
       
        return Token("groupSymbol",groupSymbol.strip(),counter_for_lines)
        sys.exit()
        
    elif char =="}":
        groupSymbol="}"
       
        return Token("groupSymbol",groupSymbol.strip(),counter_for_lines)
        sys.exit()
        
    elif char =="(":
        groupSymbol="("
        
        return Token("groupSymbol",groupSymbol.strip(),counter_for_lines)
        sys.exit()
        
    elif char ==")":
        groupSymbol=")"
      
        return Token("groupSymbol",groupSymbol.strip(),counter_for_lines)
        sys.exit()
        
    elif char =="[":
        groupSymbol="["
       
        return Token("groupSymbol",groupSymbol.strip(),counter_for_lines)
        sys.exit()
     
    elif char =="]":
        groupSymbol="]"
        
        return Token("groupSymbol",groupSymbol.strip(),counter_for_lines)
        sys.exit()
        
     #delimiter
        
    elif char==",":
        delimiter=","
        
        return Token("delimiter",delimiter.strip(),counter_for_lines)
        sys.exit()
        
    elif char==";":
        delimiter=";"
      
        return Token("delimiter",delimiter.strip(),counter_for_lines)
        sys.exit()
     #assignment   
        
    elif char ==":":      
        char=infile.read(1)
        if char=="=":
            assignment=":="
           
            return Token("assignment",assignment.strip(),counter_for_lines)
            sys.exit()
    
    
        else:
                
                print ("Error : Mετά απο ':' έπρεπε να έρθει '=' ώστε να έχουμε ':=' που υποστηρίζει η γλώσσα.\nΟ χαρακτήρας που έλαβε ήταν",char,"στη γραμμή:",counter_for_lines)
                
                sys.exit()
                
      #relOperator
      
    elif char=="<":
        char=infile.read(1)
        if(char=="="):
            relOperator="<="
            
            return Token("relOperator",relOperator.strip(),counter_for_lines)
            sys.exit()
        elif char ==">":
            relOperator="<>"
            
            return Token("relOperator",relOperator.strip(),counter_for_lines)
            sys.exit()
        
        else:
            infile.seek(infile.tell() - 1)
            relOperator="<"
           
            return Token("relOperator",relOperator.strip(),counter_for_lines)
            sys.exit()
            
            
    elif char==">":
       
        char =infile.read(1)
        if char=="=":
            relOperator=">="
         
            return Token("relOperator",relOperator.strip(),counter_for_lines)
            sys.exit()
        else:
            infile.seek(infile.tell() - 1)
            relOperator=">"
           
            return Token("relOperator",relOperator.strip(),counter_for_lines)
            sys.exit()
            
    elif char=="=":
        relOperator="="
       
        return Token("relOperator",relOperator.strip(),counter_for_lines)
        sys.exit()
    #τέλος προγραμματος
    elif char==".":
        telos_programmatos="."
        
        return Token("finish",telos_programmatos.strip(),counter_for_lines)
        sys.exit()
    #κανω skip τα σχολια 
    elif char=="#":                       # αν ο χαρακτηρας ειναι #
        char=infile.read(1)                 # διαβασε τον επομενο       
        while(char!="#"):                   # οσο ο χαρακτηρας δεν ειναι # 
            char=infile.read(1)                 #διαβασε τον επομενο
            if char=="":                        #αν ο χαρακτήρας ειναι το eof =""
                
                print("Error: Βρέθηκε σχόλιο που δεν έκλεισε στη γραμμή :",counter_for_lines)
                sys.exit()
            
        return lexical_analyze()                
        
            ##eof
    elif  char=="":
    	
    	return Token("EOF","END OF FILE",counter_for_lines)
    	sys.exit()
    
    else:
        print ("H γλώσσα δεν υποστηρίζει χαρακτήρα που Βρεθηκε στην γραμμη:",counter_for_lines,"\nΟ χαρακτήρας ήταν :", char)
      
       	sys.exit()


##Συντακτική ανάλυση

def syntax_analyze():    
	global token
    
	token=lexical_analyze()
	program()
		
				
def program():

    
    global token
    global main_program_name
   
    l=token.lineNo	
    if(token.tokenString=="program"):
        token=lexical_analyze()
        if(token.tokenType=="keyword"):
        
            main_program_name=token.tokenString
            
            token=lexical_analyze()           
            block(main_program_name)            
            if token.tokenString==".":
                genquad("halt","_","_","_")
                genquad("end_block",main_program_name,"_","_")
                
                token=lexical_analyze()
                if(token.tokenString!="END OF FILE"):
                    x=""
                    while(1):
                        
                        if(token.tokenString!="END OF FILE"):
                            
                            x=x+"\n"+token.tokenString
                            token=lexical_analyze()
                            continue;
                        else:
                            break;
                    print("WARNING : Βρέθηκε κώδικας μετά από το τέλος προγράμματος '.' , στην γραμμή :",token.lineNo,"\nΟ κώδικας που ακολουθεί τον τερματισμό σε λεκτικές μονάδες είναι: ",x )
                    sys.exit()
            else:
                print("ERROR: Δεν βρέθηκε '.' στο τελος του προγράμματος στη γραμμή",token.lineNo,"\nΒρεθηκε :'",token.tokenString,"'")
                sys.exit()	
                  
        else:
            print("ERROR: Δεν βρέθηκε όνομα μεταβλητής στη γραμμή",l,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
    else:
        print("Δεν υπάρχει η δεσμευμένη λέξη 'program' στην αρχή του προγράμματος","\nΣτην γραμμή ",l,"Βρέθηκε ",token.tokenString)
        sys.exit()
    				
			
def block(func_name):

    global token
   
    
    declarations()   
    subprograms()
   
    if func_name==main_program_name:
                                 #den exw sunarthsh h diadikasia ka9ws to name pou phra apo program den alla3e meta apo subprograms
        genquad("begin_block",main_program_name,"_","_")
    else:
        
        genquad("begin_block",func_name,"_","_")
       
    statements()
	
def subprograms():
    global token, have_sub_program
    while(token.tokenString=="function" or token.tokenString=="procedure"):
        have_sub_program=True
        subprogram()
 
def subprogram():
    global token,subProgramType,subprogram_name
	
    if(token.tokenString=="function" or token.tokenString=="procedure"):
        if(token.tokenString=="function"):
            subProgramType="function"
        else:
            subProgramType="procedure"
            
        token=lexical_analyze()
        if(token.tokenType=="keyword"):
            subprogram_name=token.tokenString   
            token=lexical_analyze()
            if(token.tokenString=="("):
                token=lexical_analyze()
                formalparlist()
               
                if (token.tokenString==")"):
                    token=lexical_analyze()
                    
                    block(subprogram_name)
                    tk = lexical_analyze()
                    print(tk.tokenString)
                    '''
                    if(subProgramType == "procedure" and token.tokenString == "return"):
                        print("ERROR: Μία διαδικασία δεν επιτρέπεται να έχει 'return' στην γραμμή: ",token.lineNo)
                        sys.exit()
                    else if(subProgramType == "function"):
                        if(token.tokenString!= "return"):
                            print("ERROR: Μία συνάρτηση θα πρέπει να έχει τουλάχιστον ένα return!")
                            sys.exit()
                        else if(token.tokenString == "}"):
                    '''
                    genquad("end_block",subprogram_name,"_","_")
                else:
					
                    print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
                    sys.exit()
               
            else:
				
                print("ERROR : Το πρόγραμμα περίμενε '(' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
                sys.exit()
                
        else:
			
            print("ERROR : Το πρόγραμμα περίμενε 'όνομα μεταβλητής' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
        
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
 
    if(token.tokenString=="in" or token.tokenString=="inout"):
        token=lexical_analyze()
        if(token.tokenType=="keyword"):
            token=lexical_analyze()
        else:		
            print("ERROR : Το πρόγραμμα περίμενε 'keyword/ονομα μεταβλητής' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString) 
            sys.exit()    
    else:
        print("ERROR : Το πρόγραμμα περίμενε 'in' or 'inout' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit()
		
								
def actualparlist():
    global token
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
    
    if(token.tokenString=="in"):
        token=lexical_analyze()
        exp=expression()
        return (exp,"CV")
    elif(token.tokenString=="inout"):
        token=lexical_analyze()
        name=token.tokenString
        if(token.tokenType!="keyword"):   
            print("ERROR : Το πρόγραμμα περίμενε 'keyword/ονομα μεταβλητής' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
        token=lexical_analyze()
        return (name,"REF")
    else:
        print("ERROR : Το πρόγραμμα περίμενε 'in' or 'inout' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        sys.exit() 


def idtail(sub_prog_name):
    global token
   
    if(token.tokenString=="("):
        token=lexical_analyze()
        parameters=actualparlist()    ####
        if(token.tokenString==")"):
            token=lexical_analyze()
            return(True, parameters)       ######
        else:
            print("ERROR : Το πρόγραμμα περίμενε ')' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
            sys.exit()
    return(False, None)     ####

        										   
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

    count=token.lineNo
    if(token.tokenString!=""):
        if(token.tokenType=="keyword"):
            list_of_variables.append(token.tokenString);     ###
            token=lexical_analyze()
            if(token.tokenString==","):
                token=lexical_analyze()
                varlist()
        else:
            print("ERROR : Το πρόγραμμα περίμενε 'keyword/ονομα μεταβλητής' στη γραμμή:",count,"\nΒρέθηκε ",token.tokenString)
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
    global token
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
    optionalSing()
    num1=term()
    
    while(token.tokenString=="+" or token.tokenString=="-"):
        op_sing=token.tokenString
        ADD_OP()
        num2=term()
        temp=newtemp()
        genquad(op_sing,num1,num2,temp)
        num1=temp

    return num1    
		  

def optionalSing():
    global token
    if(token.tokenString=="+" or token.tokenString=="-"):
        token=lexical_analyze() 
        

def term():
    global token			
    num1=factor()
	
    while(token.tokenString=="*" or token.tokenString=="/"): 
        op_sing=MUL_OP()
       
        num2=factor()
        temp=newtemp()
        genquad(op_sing,num1,num2,temp)
        num1=temp
        
    return num1    
	
def factor():

    global token
    
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
    if(token.tokenString=="("):
        token=lexical_analyze()
        exp = expression()
        genquad("retv",exp,"_","_")
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
        #print("ERROR : Το πρόγραμμα περίμενε 'case' ή 'default' στη γραμμή:",token.lineNo,"\nΒρέθηκε ",token.tokenString)
        #sys.exit()
        pass


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

    global token
    if(token.tokenType=="keyword"):
        call_name=token.tokenString
        token=lexical_analyze()
        if(token.tokenString=="("):
            token=lexical_analyze()
            parameters=actualparlist()
            if(token.tokenString==")"):
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

##### ενδιαμεσος κωδικας 


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

    def __init__(self,name,entity_type):
        self.name = name
        self.entity_type = entity_type
    
    def toString(self):
        return self.name + ":" + self.entity_type

class Variable(Entity):

    def __init__(self,name,offset = 0):
        Entity.__init__(self,name,"VAR")
        self.offset = offset
    
    def toString(self):
        return Entity.toString(self) + "\toffset" + str(self.offset)

class Function(Entity):

    def __init__(self,name,retFuncVal,startQuad,argument,framelength):
        Entity.__init__(self,name,"FUNC")
        self.startQuad = startQuad
        self.retFuncVal = retFuncVal
        self.argument = list()
        self.framelength = 0
    
    def setFramelength(self,framelen):
        self.framelength = framelen
    
    def setQuad(self,quad_num):
        self.startQuad = quad_num
    
    def setVal(self,value):
        self.retFuncVal = value
    
    def toString(self):
        return Entity.toString(self) + ", Starting Quad: " + self.startQuad.toString()\
                + ", Framelength: " + str(self.framelength) + ", Function Arguments: " + self.argument.toString()

class ConstantValue(Entity):

    def __init__(self,name,conVal):
        Entity.__init__(self,name,"CONSVAL")
        self.conVal = conVal
    
    def toString(self):
        return Entity.toString(self) + ", Constant value" + conVal

class Parameter(Entity):   
  
    def __init__(self, name, parMode, offset = 0):
        Entity.__init__(self, name, "PAR")
        if parMode == "in":	
            self.parMode = "CV"
        elif parMode == "inout":
            self.parMode = "REF"
        else:
            self.parMode = "RET"
        self.offset = offset

    def toString(self):
        return Entity.toString(self) + ",\tParameter_Mode: " + self.parMode + ",\toffset: " + self.offset

class TemporaryVariable(Entity):

    def __init__(self, name, offset = 0):
        Entity.__init__(self, name, "TMPVAR")
        self.offset = offset

    def toString(self):
        return Entity.toString(self) + ",\toffset: " + str(self.offset)

class Scope:

    def __init__(self, nestingLevel = 0):
        self.entities = list()
        self.nestingLevel = nestingLevel
        self.sp = 12

    def getSP(self):
        res = self.sp
        self.sp += 4
        return res
    
    def addEntityToScope(self, ent):   
        self.entities.append(ent)  
    
    def toString(self):
        return self.__repr__() + "\n Nesting Level: " + self.nestingLevel.__repr__()
    
class Argument:

    def __init__(self, parMode):
        self.parMode = parMode
        self.type = "Int"
        
    def addArgsToFunc(parMode, func_name):
        funcEnt = searchEntity(func_name, "FUNC")[0]
        if funcEnt is None:
            print("Δεν βρέθηκε κάποια συνάρτηση ή διαδικασία στο συγκεκριμένο βάθος φωλιάσματος!")
            sys.exit()
        funcEnt.argument.append(parMode)


def checkSymbolTable(name):
    global scopesList
    
    currentScope = scopesList[-1]
    
    while(currentScope is not None):
        for entity in currentScope.entities:
            if entity.name == name:
                return entity, currentScope.nestingLevel
    return None
    
################################ Final Code ######################################
  
def gnvlcode(v):
    global quadList, asmFile, scopesList
    
    ent, entLevel = checkSymbolTable(v)
    
    if ent is None:
        print("Βρέθηκε μία κενή οντότητα στον πίνακα συμβολών η οποία δεν είναι μεταβλητή!")
        sys.exit()

    if ent.entity_type == "Func":
        print("Βρέθηκε υποπρόγραμμα στον πίνακα συμβόλων με όνομα", v, "ενώ περίμενε μεταβλητή!")
        sys.exit()
    
    currentLevel = scopesList[-1].nestingLevel
    varLevel = currentLevel - entLevel
    asmFile.write("\tlw $t0, -4($sp)\n")
    
    while varLevel > 1:
        asmFile.write("\tlw $t0, -4($t0)")
        varLevel -= 1
        
    asmFile.write("\taddi $t0, $t0, - %d\n" % ent.offset)
   
def loadvr(v, r):
    global quadList, asmFile, scopesList
    
    if str(v).isdigit():
        asmFile("\tli $t%s, %s\n"%(r,v))
    else:
        ent, entLevel = checkSymbolTable(v)
        
        if ent is None:
            print("Βρέθηκε μία κενή οντότητα στον πίνακα συμβολών η οποία δεν είναι μεταβλητή!")
            sys.exit()
        
        currentLevel = scopesList[-1].nestingLevel
        
        if(ent.entity_type == "VAR" and entLevel == 0):
            asmFile.write("\tlw $t%s, -$d($s0)\n"%(r, ent.offset))
        elif((ent.entity_type == "VAR" and entLevel == currentLevel) or (ent.entity_type == "PAR" and entLevel == currentLevel and ent.parMode == "CV") or (ent.entity_type == "TMPVAR")):
            asmFile.write("\tlw $t%s, -%d($sp)\n"%(r,ent.offset))
        elif((ent.entity_type == "PAR" and entLevel == currentLevel and ent.parMode == "REF")):
            asmFile.write("\tlw $t0, -%d(%sp)\n"%ent.offset)
            asmFile.write("\tlw $t%s, ($t0)\n"%r)
        elif((ent.entity_type == "VAR" and entLevel < currentLevel) or (ent.entity_type == "PAR" and entLevel < currentLevel and ent.parMode == "CV")):
            gnvlcode()
            asmFile.write("\tlw $t%s, ($t0)\n")
        elif((ent.entity_type == "PAR" and entLevel < currentLevel and ent.parMode == "REF")):
            gnvlcode()
            asmFile.write("\tlw $t0, ($t0)\n")
            asmFile.write("\tlw $t%s, ($t0)\n"% r)
        else:
            print("Υπάρχει σφάλμα κατά την μεταφορά των δεδομένων ", v,"από τον καταχωρητή ",r)
            sys.exit()

def store(r, v):
    global quadList, asmFile, scopesList
  
    ent, entLevel = checkSymbolTable(v)
        
    if ent is None:
        print("Βρέθηκε μία κενή οντότητα στον πίνακα συμβολών η οποία δεν είναι μεταβλητή!")
        sys.exit()
       
    currentLevel = scopesList[-1].nestingLevel
        
    if(ent.entity_type == "VAR" and entLevel == 0):
        asmFile.write("\tsw $t%s, -$d($s0)\n"%(r, ent.offset))
    elif((ent.entity_type == "VAR" and entLevel == currentLevel) or (ent.entity_type == "PAR" and entLevel == currentLevel and ent.parMode == "CV") or (ent.entity_type == "TMPVAR")):
        asmFile.write("\tsw $t%s, -%d($sp)\n"%(r,ent.offset))
    elif((ent.entity_type == "PAR" and entLevel == currentLevel and ent.parMode == "REF")):
        asmFile.write("\tlw $t0, -%d(%sp)\n"%ent.offset)
        asmFile.write("\tsw $t%s, ($t0)\n"%r)
    elif((ent.entity_type == "VAR" and entLevel < currentLevel) or (ent.entity_type == "PAR" and entLevel < currentLevel and ent.parMode == "CV")):
        gnvlcode(v)
        asmFile.write("\tsw $t%s, ($t0)\n")
    elif((ent.entity_type == "PAR" and entLevel < currentLevel and ent.parMode == "REF")):
        gnvlcode(v)
        asmFile.write("\tlw $t0, ($t0)\n")
        asmFile.write("\tsw $t%s, ($t0)\n"% r)
    else:
        print("Υπάρχει σφάλμα κατά την μεταφορά των δεδομένων ", v," στον καταχωρητή ",r)
        sys.exit()

def asmFileGen(currentQuad,name,labelNum):
    global quadList, asmFile, scopesList, Lmain_Flag, main_program_name

def main(args):
    global infile,quadList,intFile,cFile,list_of_variables,have_sub_program,asmFile
	
    if(len(args) !=2):
        print("Δώσε αρχείο με τον κωδικα")
        sys.exit()
		
    in_file=args[1]
    if (not in_file.endswith('.ci')):
        print("Το αρχείο πρέπει να έχει επεκταση '.ci' ")
        exit()	
	
    try:
        infile = open(in_file, "r")
        intFile = open("int_file.int","w")
        
    except OSError:
        print("Το συστημα δε μπορει να ανοιξει το αρχειο")
        sys.exit()
				
    syntax_analyze()
    intFileGen()
    if have_sub_program==False:
        cFile = open("C_file.c","w")
        cFileGen()
        cFile.close()
    for i in range(len(quadList)):
        quadList[i].myfunc()
    
   
    infile.close()
    intFile.close()
    
if __name__ =="__main__":
	main(sys.argv)	
    			

