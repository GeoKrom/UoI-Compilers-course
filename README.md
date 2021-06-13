# Compilers

This is a compiler for a custom programming language named Cimple.

It is a semester project for the course CSE/MYY802 - Compilers, Department of Computer Science and Engineering, UoI.

# Front - End

The front end part analyzes the source code with lectical, syntax and sematic analyzer, in order to generate an internal
represantation of the program, called the intermediate code. In these stages, we implemennt the symbol table and the error handler.
The symbol table is a data structure which stores every variable(Global, Local, Temporary) of the source code. The error handler projects an error message on the terminal when an unauthorized action is performed, such as keywords that do not belong in the language.

# Back - End

The back end is responsible for generating machine level code (assembly code) so the CPU can execute it. 
In particular the generated code is for the MIPS processor. With the use of symbol table and intermediete code, the objective code can be generated.

# Cimple Syntax 

To view the syntax of the programming language [click here](https://github.com/GeoKrom/Compilers/tree/main/Syntax).

# Authors
[Lambros Vlaxopoulos](https://github.com/lamprosvlax13)

[George Krommydas](https://github.com/GeoKrom)
