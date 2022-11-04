# Blackboard Test Hacker
## *Okay, so maybe it isn't really hacking...* ##

This is a program I wrote initially to simply run some subnetting calculations because I was too lazy to do math.
I then got much lazier and decided to just write code to do my homework for me.

This works by reading the source of a blackboard test, then parsing it to json, stripping the questions from the json,
and running the questions by a filter to generate answers. The answers are output in javascript so they can be pasted
directly into the console log for the blackboard test page and ran.

To Use:
1. Download the program, the colleges modules may not need to all be downloaded, you can pick whichever ones apply to you individually
2. Set the `.env` variables to the respective values (command line arguments can also be passed to specify these values, but for repeated use it makes more sense to just set the `.env`)
3. Run `pip install -r requirements.txt`
4. Retreive the source code of the test. This can be done by pressing `Ctrl + S` and saving as **HTML File ONLY**. This method is slightly unreliable, as occasionally it will just set the source to a redirect page. For best results, view source first by pressing `Ctrl + U`, then select all and paste into the `source.html` file
5. Run `python3 import.py`
*When running the command, variables can be specified. The file can be specified as `file=example.html`, the college as `college=000000`, and the class as `class=AAAA100`*

Obviously in the current state of this program, it is only designed for my one college class. However, it has been designed with optimal public usage in mind. By copying the format of the module that is already existing, it can easily be set up for any class in any college, so long as blackboard is used. The number `002835` is not arbitrary, it uses the 2022-2023 FAFSA School Code Indexing. This was done so it can be universal

It is known that currently the only supported test type is short answer on one page. This is the only reference point I have currently, but I hope to update the entire thing soon to allow for more formats
 
