# chemist
A python program for chemistry.


This is very simple program to do basic chemical calculations with the CLI.

**Commands:**

**mass:**

Calculates the mass of an element or a molecule. It looks for uppercase characters and divides them into an array, then it looks for any number in the
element to multiply with the molar mass.


**Example:** chemist mass H20


Here, the program translates H2O into "1.008 * 2" + "15.999" giving us 18.015 g/mol.



**convert:**

Converts an amount of matter from either moles or grams, depending on the input.


**Example:** chemist convert 10 mol H2O


Here, the program takes the molecular mass of H2O "18.015 g/mol" and multiplies it with the amount "10 moles" giving us a result of 180.15 g H2O
if we use the command "chemist convert 10 g H2O", then it would divide 10 by 18.015, giving us 0.555 moles of H2O.


**preassure:**


Converts the unit of a specific preassure.


**Example:** chemist preassure 10 atm torr


Here, the program converts 10 atmospheric preassure to torr, giving us the result of 7600.02torr
**Available units: torr, mmHG, PSI, Pa, Bar**


**energy:**


This command works much like the preassure command, but with energy unit conversion. It takes three arguments.


**Example:** chemist energy 10 joules kcal


**Available units: Cal, Kcal, Joule, KJoule**


**temp:**


This command converts temperature. to either Celcius, Fahrenheit, and Kelvin.


**Example:** chemist temp 10 C K


**Available units: C, K, F.**


**atomicnumber:**


Takes one argument, an element and returns it's atomic number.


**Example:** chemist atomicnumber H


This returns 1.


**ect:**


Prints the electron configuration table, takes no arguments.
1s2
2s2 2p6
3s2 3p6 3d10
4s2 4p6 4d10 4f16
5s2 5p6 5d10 5f16
6s2 6p6 6d10 
7s2 7p6
8s2


**econf:**


Takes one argument, an element and prints the electronic configuration of that element.


**Example:** chemist econf Li


Since Lithium has an atomic number of three, the electron configuration would be: "1s2 2s1"


**showtable:**

Prints the periodic table on the terminal. It takes one optional argument of an element to show basic information about said element and highlights it.


**Example:** chemist showtable H


Highlights Hydrogen on the periodic table.


**name:**


Prints the name of an element, "chemist name H" prints out "Hydrogen".


**whatis:**


Takes the common name of a molecule, and prints it in it's original compund. "chemist whatis salt" prints out "NaCl".


**molecule:**


Prints all molecules in the molecules.py module, They can be used in mass/convert commands (even their common names can be used).


**calc:**


Performs basic arithmatic, 1 + 1 = 2.


**help:**
Lists all usable commands.


**-s:**


The "-s" is not a command, but a flag. It is used to show precise results. Since chemist uses floating point arithmatic, we may need to round the result.
Insert the "-s" flag anywhere in the command to get more precise results. It will increase the rounding digits number.
