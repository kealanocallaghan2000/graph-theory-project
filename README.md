# ReadMe

## Contents:
##### 1. Programme description
##### 2. Programme instructions
##### 3. Algorithm explanation
##### 4. Log of progress
##### 5. Definitions

## Programme description
The following programme is written in Python3 with no external libraries or imports to search a text file using a regular expression and to output any (or none) matches that it finds within a text file.
The programme will take the path of a text file and the regular expression. It will then convert the regular expression to postfix, convert the postfix to a nfa, and then match the nfa to each word in each line of the text.

## Programme Instructions 

* To run the project, clone the code and depending on your version of python type "python3 project.py".
* At first you will be asked to enter the location of your txt file which you're looking to process.
* Type your txt file path in the format 'C/Users/Name/file.txt' and the programme will interpret that for
the WSL format.
* If the programme finds your file, it will then ask you to then enter the regular expression you would
like to apply on the text file (explained below). 
* Once you've entered your regular expression and hit enter, the programme will apply it and output
each word, in each line of your textfile and whether or not it matches the regular expression you chose.

## Algorithm Explained

##### Shunting yard algorithm
In order for the regular expression to be converted into an nfa to be applied on the text, it must first be converted into postfix using the shunting yard algorithm. The 'shunt' method reads in the users regular expression and pops the operators or letters onto a stack according to its precedence in the code. '*' has the highest precedence, followed by '.' followed by '|'. Once the precedence has been applied to the regex it will return the variable 'postfix' which will be a string that can be used later in the programme. Eg. (a|b) -> ab|

##### Thompsons construction
Once the programme has created it's postfix notation of the regex, it is time for it to be converted into an NFA using 'Thompson's Construction'.
This section of the programme is split into two classes (State and NFA) and one large method (re_to_nfa):
* In the 'State' class, it is used to create a coded version of an nfa's states. Meaning it can have the state of the nfa and the arrows coming from it.
* In the 'NFA' class, the constructor will take in three params, self,the String 's' and 'end'. The method 'match' takes in self and 's' which matches the string s to the NFA. The method returns True or False depending on whether the string matches the NFA or not.

**Finally** the method re_to_nfa, takes in the posdtfix of the users regular expression, loops through each character in the posdtfix and applies different methodoligies depending on which operator (or letter) is next in the regular expression. It creates start and end points for the nfa depending on the character and appends the NFA accordingly, once the string has been looped through, it will return ther stack which should only contain one NFA at the end.

##### Bringing everything together
The final piece of the code connects all of the methods and the users input together to match the regular expression to the users text file as follows:
* Postfix = shunting yard algorithm applied on the users regex -> shunt(regex)
* Nfa = the re_to_nfa method applied on the postfix from the previous point.
* For every line in the users file
* For every word in the line from above
* match = the nfa on the word in the line
* If the match = True, print the line and the word where the regular expression matched the word.
* Counters++ and repeat this process until every word has been applied.


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

Before we answer this question, we should define a few things first.
What is a formal language? A formal language is a set of finite strings. A string is simply a sequence of characters. All of the following are formal languages:

* The set of all strings
* The empty set
* The set of all strings that have an even number of characters
* The set of all strings that begin with the letter ‘q’

It is said that a regular expression can decide a formal language if both their statments are equivalent for each string. Eg. **X** is in the language **Y**, **X** is accepted by **Z**, or in other words, **X** is equivalent to **Z** - they both describe the same set of strings.

By applying the basic operators of a regular expression (| * .), you can already match all regular languages (a language which can be expressed with finite automota). After this, you need to use a few more tools of regular expression to fully match all formal languages, such as :
* Backreferences.
* Recursion.

###### Backreferences
Backreferences extend a regular expressions syntax by allowing you to refer a segment of the string that was captured by the regex in another location. This gives you alot more expressive power than regular languages.

###### Recursion
Recursion in regular expressions can be even more powerful. This is when you repeat the regular expression, in the middle of the matching string. The simplest example of this would be, if we wanted to match all the strings of 'b's, we can already do this with the regex b*. This works as we accept the empty string, as the whole thing we're matching is optional. If we didnt have an empty string, then it must be 'b'. Following the b we either have nothing or we have a recurring application of the whole regular expression.

This shows that with a few extra tools of the regular expression such as **backreference's** and **recursion**, it's possibilities are limitless and can match any formal language, demonstrating how truly powerful they are.