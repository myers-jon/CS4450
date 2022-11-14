Ryan could not get antlr to work on his computer, he is still trying to get it set up
we worked over discord on these problems and the approach, so I have done all the pushes this time

We used an Ubunutu environment with antlr 4.9.3 and python3 for this program.
Our approach requires the Java RTE and the correct antlr version jar file.

Install and run up Ubuntu on your machine. There are several ways to do this 
including a hosted hypervisor, booting from an image on a flash drive,
or installing Ubuntu as your native OS.
Install python and Java.
Download the antlr 4.9.3 jar file.
Navigate with 'cd ~/Downloads' and run this command:

$export CLASSPATH=".:usr/local/lib/antlr-4.9.3-complete.jar:$CLASSPATH";
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9.3-complete.jar:$CLASSPATH" org.antlr.v4.Tool'

Make sure your pip is up to date and run:

$pip install antlr4-python3-runtime==4.9.3

Navigate to where you saved the project repo and run this command to generate the
parser with python3 as the selected language and the .g4 grammar file as the target grammar.

$antlr4 -Dlanguage=Python3 new_grammar.g4

If everything is set up correctly this will generate the necessary lexar, parser, token, etc. files to run the Main.py file with the grammar contained in new_grammar.g4.

Alternatively, you can save the jar file in the same repository as the grammar and main file and run this command on the jar file directly.

$java -jar antlr-4.9.3-complete.jar -Dlanguage=Python3 new_grammar.g4

To run the program cd into the project directory and run this command:

$python3 Main.py

Now, we can define some variables!
Valid syntax for the parser starts with a variable name that cannot begin with an integer.
Press the enter key between definitions. Use ^D to parse the input and exit the program.

For example:
W = True  <br />
X = 2  <br />
Y = 2 + 2  <br />
Z = foo  <br />
Z1 = bar  <br />
^D  <br />

This will produce an output conisting of a parse tree and input type.
Incorrect syntax will produce an error.







