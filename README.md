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
LAST EDIT 2/12/2013
```  
CallerPy v0.2 - TODO
  
Defintion: 

* [IMP]     Important Changes 
* [ASTH]	Aesthetic Implementations  
* [FIX]	    Fixes to Currant Version  
* [IMPV]	Improvments
-----------------------
1. [IMPV]	More Login Methods--Facebook, G+, Linkedin  
2. [IMP]	Automated Name|Number Crawler  
3. [ASTH]	View in Map * Will handle encoding  
4. [IMP]	Show all possible names  
5. [IMP]	Define function to handle arguments
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
            {
name::Dominos Pizzay Quejas
number::7349303030
country::us
}
{
name::Pizza Hut Delivery
number::08447700669
country::uk
}

```
*Note*: this is an update to the former, or rather the latter method which used the XML format  
  
To view the log: *note the lack of arguments*
```
python callerpy.py
Dominos Pizzay Quejas -- 7349303030 -- us
Pizza Hut Delivery -- 08447700669 -- uk
```


