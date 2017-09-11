           	                             
			                       MAPLE: 

1)Install MAPLE and open the maple program Assignments-new.mw. From the top down View menu select Collapse all Sections.  


2) Expand Section titled: "Defines the word and the Bott-Samelson"

a) Enter word corresponding to the Bott-Samelson in the array STRING. 

b) Enter the Lie-type in the variable Lietype.

c) Set Morse to 1 if you want to do Morse theory. Otherwise let it be set to 0.
 

3) Compile the entire program. 

------ Morse theory------------
4) If you are doing Morse theory there will be 2^d text files created in the same folder titled "test1", "test2" and so on corresponding to the fixed points. 

5)There will be another text file created titled "A" corresponding to the assignment basis. So total of 2^d+1 text files will be created. 
 
		               PYTHON (Only required for Morse theory)

1) Open the python program "singular-format-new.py" in a text editor.

2) From terminal call python.

3) Type in the terminal: execfile("singular-format-new.py") and press enter.

4) At the prompt: <Enter the number of fixed points> 
enter the number of fixed points which is 2^d.

5) There will be 2^d+1 total output files (2^d fixed points + one assignment basis) created and an extra file
called Singularlists, consisting of two Singular lists "vertex" and "sing".


          			SINGULAR (Only required for Morse theory)
1) Open the program "Singular-Ideal" in a text editor. 

2) Open Singular prompt (by default opens in home folder in Mac):

7) In the Singular prompt type: execute(read(“Singular-Ideal”));

8) A file called output.txt is generated.

9) The output.txt file lists the morse generators(assignments supported at a vertex and above) and also the ideal generators. 

10) The output.txt file also generates the matrix of morse generators, and the relations between them.


















