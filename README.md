callerpy
========
[![Build Status](https://travis-ci.org/Logic-gate/callerpy.png?branch=master)](https://travis-ci.org/Logic-gate/callerpy)  

Truecaller Name Retriever.  
Since my request for the API was rejected, I commenced using python parsing libraries.  
Callerpy emulates the process one would encounter if using a web-browser.

***
**NEW FEATURE**  
Strangely enough, it is not possible to physically enter the country code in www.truecaller.com although defined in www.truecaller.com/javascripts/app.min.1385646302.js  
However, it is possible to do so using callerpy.  

***
TODO
--------
***
LAST EDIT 28/11/2013
```  
CallerPy v0.2 - TODO
  
Defintion: 

* [IMP]	    Important Changes 
* [ASTH]	Aesthetic Implementations  
* [FIX]	    Fixes to Currant Version  
* [IMPV]	Improvments
-----------------------
1. [IMPV]	More Login Methods--Facebook, G+, Linkedin  
2. [IMP]	Automated Name|Number Crawler  
3. [ASTH]	View in Map * Will handle encoding  
4. [IMP]	Show all possible names  
5. [IMP]	Define function to handle arguments
6. [IMP]    Add xml parsing
```
***
How To
-----
***
**CMD**
```
python callerpy.py -h
usage: callerpy_v2.py [-h] -n number [-c country] [-cc country code] -l login

TrueCaller Name Retriever

optional arguments:
  -h, --help            show this help message and exit
  -n number, --number number
                        Phone Number Without Country Code (default: None)
  -c country, --country country
                        Country | String (default: None)
  -cc country code, --countrycode country code
                        Country | Int (default: None)
  -l login, --login login
                        Login Method | twitter, g+, fb (default: twitter)

Do not forget to hardcode your credentials
```
***
**RUN**
```
python callerpy.py -n 7349303030 -c us -l twitter  
```
***
*OR*
```
python callerpy.py -n 7349303030 -cc 1 -l twitter
```
***
**OUTPUT**
```
            <entry>
    			<name>Dominos Pizzay Quejas</name>
				<number>7349303030</number>
				<country>us</country>
			</entry>
		
			<entry>
				<name>Pizza Hut Delivery</name>
				<number>08447700669</number>
				<country>uk</country>
			</entry>

```
*Note*: you should enclose the xml by adding a tag
```
<something>
            <entry>
        		<name>Dominos Pizzay Quejas</name>
				<number>7349303030</number>
				<country>us</country>
			</entry>
		
			<entry>
				<name>Pizza Hut Delivery</name>
				<number>08447700669</number>
				<country>uk</country>
			</entry>
</something>
```


