## Log of progress

Feb 7th:
* Created a repository and a txt file as my first commit for the graph theory project, brushed up on ideas and oncepts to date to help with understanding how to go about the project. No grasp on how the python will be implemented to use automata.

March 31st:
* Began the project, up until this point I have just been studying the different concepts like the shunting
yard algorithm and thompsons construction and trying to make sense of how they will eventually work in the 
form on nfa's to work through a txt file like a regular expression.
* I spent the time on my project to figure out the best way to read a file path in python, the reading
was simple but figuring out that I needed to use /mnt to find a path took longer than I care to admit.
* Only hard coded file path works.

Apr 5th:
* User can finally input their custom file path and the programme will output each line of the code.

Apr 9th:
* I spent today implementing the shunting yard algorithm from the lecture into my programme so that instead
of a hard coded regular expression the user can now input any re that they want.
* Finally starting to understand how the concepts we've learned to date will be applied to the project.
* File reading and writing code commented out for now.

Apr 15:
* Applied thompsons construction to the project so now when the user inputs their regular expression,
the project will make a postfix version of it and then turn it into an nfa.
* Watching videos on the match function to be applied soon.

Apr 17:
* Applied the matching function to everything i've done to date. 
* Brought back my file input code and regular expression input code.
* Watched videos on matching function again to figure out how it works.
* User can now choose their own regular expression and text file path.


## Programme Instructions 

* To run the project, clone the code and depending on your version of python type "python3 project.py".
* At first you will be asked to enter the location of your txt file which you're looking to process.
* Type your txt file path in the format 'C/Users/Name/file.txt' and the programme will interpret that for
the WSL format.
* If the programme finds your file, it will then ask you to then enter the regular expression you would
like to apply on the text file (explained below). 
* Once you've entered your regular expression and hit enter, the programme will apply it and output
each word, in each line of your textfile and whether or not it matches the regular expression you chose.


# Definitions

### What is a regular expression?

Regular expressions are very powerful, yet simple sequence of characters which can be looked at almost as a mini programme or piece of code. Regular expressions are generally used for searching string of text or for searching and replacing words/text in a paragraph or a file - it describes a set of strings that match the pattern in the regular expression.

Conceptually, the simplest regular expressions are literal characters. The pattern N matches the character 'N'. Regular expressions next to each other match sequences. For example, the pattern 'Ian', matches the sequence 'I' followed by 'a' followed by 'n'. When we add just a little more complexity, you can match either 'ian' or 'Ian' with the patter [Ii]an. 

There are many operators in regular expressions, each with their own set of rules/applications. For example, the '.' operator matches any single character. A '*' will match the preceeding letter 0 or more times. The '?' will match the preceeding item at most, once. I'll include a small table of all the possible operators below.

Operator | Effect
-------- | ------
'.' | Matches any single character.
'?' | The preceding item is optional and will be matched, at most, once.
'*' | The preceding item will be matched zero or more times.
'+' | The preceding item will be matched one or more times.
'{N}' | The preceding item is matched exactly N times.
'{N,}' | The preceding item is matched N or more times.
'{N,M}' | The preceding item is matched at least N times, but not more than M times.
'-' | represents the range if it's not first or last in a list or the ending point of a range in a list.
'^' | Matches the empty string at the beginning of a line; also represents the characters not in the range of a list.
'$' | Matches the empty string at the end of a line.
'\b' | Matches the empty string at the edge of a word.
'\B' | Matches the empty string provided it's not at the edge of a word.
'\<' | Match the empty string at the beginning of word.
'\>' | 	Match the empty string at the end of word.

The most important part about regular expressions is the concepts. It's important to not get bogged down in learning all the different operators as when you figure out what they all do, the differences in syntax amount to little more than small dialects. 

Regular expressions (regexes) are a core component of modern programming languages. Regexes are commonly used for text processing and input sanitization, appearing, for example, in an estimated 30-40% of open-source Python and JavaScript projects.

Some real world applications of regular expressions are:
###### Email validation

'^[^@ ]+@[^@ ]+\.[^@ \.]{2,}$' -> This regular expression can check if an email address is the valid syntax.

###### Password validation

'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s)(?=.*[!@#$*])' -> This regular expression can check if an password is the valid syntax. eg. includes uppercase and special characters

###### Credit card number Validation:

**Visa Credit Card**: ^4[0–9]{12}(?:[0–9]{3})?$
**American Express Credit Card**: ^3[47][0–9]{13}$
**Mastercard**: ^(?:5[1–5][0–9]{2}|222[1–9]|22[3–9][0–9]|2[3–6][0–9]{2}|27[01][0–9]|2720)[0–9]{12}$
**Discover Card**: ^6(?:011|5[0–9]{2})[0–9]{12}$


As you can see, Regular expressions are extremely useful in computer science, especially in any information based systems where searching and replacing text is commonplace.




### How do regular expressions differ across implementations?

As regular expressions are so powerful and useful across many different applications, it's no surprise that they can differ between different implementations. Many applications and programming languages have their own implementation of regular expressions, often with slight and sometimes with significant differences from other implementations.

This can cause some serious portability issues if you're expecting to just copy and paste regular expressions between different programming languages. A paper written in Virginia Tech, USA states that 'this lack of standardization comes as no surprise to developers familiar with regexes as a library feature rather than a language primitive'.

Different programming languages have distinct regex engines which may show different performance characteristics. A re-used regex might have worse worst-case performance in its new language than the one that it has been reused from. For example: a regular expression which is being transported from php to Node.js will have catastrophically worse vulnerabilities because regexes are knows for having worse worst-case performance in Node.js.

##### Examples of differences in regular expressions across languages:

* Visual studio 2010 uses {} instead of () to group expressions for back references.
* In python '[...]' means Character class, whereas in grep it represents a Bracket expression.
* In SED, (){}[] are escaped when used in regex's, which can be extremely problematic for other implementations.

Regular expressions will compile in different implementations most of the time, but the small differences in each different type make them very hard to be standardized. Their apparent portability masks problems of correctness and performance, but not enough that they can be called a standardized language.



### Can all formal languages be encoded as regular expressions?