callerpy
======== 

**UPDATE MAY_18_2014**  
A new RESTful online version is available @ http://callerpy.sysbase.org  
I will port it to CLI within a few days.

CURL Example:
```
$ curl -v 'http://callerpy.sysbase.org/search/world/api/v1/REST?number=920012345&cc=966'

* About to connect() to callerpy.sysbase.org port 80 (#0)
*   Trying 54.243.121.176...
* connected
* Connected to callerpy.sysbase.org (54.243.121.176) port 80 (#0)
> GET /search/world/api/v1/REST?number=920012345&cc=966 HTTP/1.1
> User-Agent: curl/7.26.0
> Host: callerpy.sysbase.org
> Accept: */*
> 
* additional stuff not fine transfer.c:1037: 0 0
* additional stuff not fine transfer.c:1037: 0 0
* additional stuff not fine transfer.c:1037: 0 0
* additional stuff not fine transfer.c:1037: 0 0
* additional stuff not fine transfer.c:1037: 0 0
* additional stuff not fine transfer.c:1037: 0 0
* additional stuff not fine transfer.c:1037: 0 0
* additional stuff not fine transfer.c:1037: 0 0
* additional stuff not fine transfer.c:1037: 0 0
* HTTP 1.1 or later with persistent connection, pipelining supported
< HTTP/1.1 200 OK
< Content-Type: application/json
< Date: Sun, 18 May 2014 00:19:12 GMT
< Server: gunicorn/18.0
< Content-Length: 302
< Connection: Keep-Alive
< 
{
  "getWorld": [
    {
      "ADDRESS": "", 
      "AREA": "", 
      "COMPANY_NAME": "", 
      "COUNTRY": "Saudi Arabia", 
      "NAME": "Dominos Pizza", 
      "NUMBER": "9200 12345", 
      "STREET": "", 
      "TWITTER_NAME": "", 
      "TWITTER_SCREEN_NAME": "", 
      "ZIPCODE": ""
    }
  ]
* Connection #0 to host callerpy.sysbase.org left intact
}* Closing connection #0

```
*** 

Truecaller Name Retriever.  
Since my request for the API was rejected, I commenced using python parsing libraries.  
Callerpy emulates the process one would encounter if using a web-browser.

***
**NEW FEATURE**  
Strangely enough, it is not possible to physically enter the country code in www.truecaller.com although defined in www.truecaller.com/javascripts/app.min.1385646302.js  
However, it is possible to do so using callerpy.  

**...EVEN NEWER FEATURE::THANKS TO NIRAV DESAI FOR HIS INSISTENCE :)**  
Automated Crawler
*Truecaller has rate limit*
```
python callerpy.py -crawl 2 -l twitter
```  
The integer represents the time to wait between each request.  

Write the numbers in ```num.list``` according to the following format(```CC;number```):  
```
1;7349303030
1;7349303022
```
*Note the escape between them*

***
TODO
--------
***
LAST EDIT 2/12/2013
```  
CallerPy v0.2 - TODO
  
Defintion: 

* [IMP]     Important Changes 
* [ASTH]    Aesthetic Implementations  
* [FIX]     Fixes to Currant Version  
* [IMPV]  Improvments
-----------------------
1. [IMPV] More Login Methods--Facebook, G+, Linkedin  
2. [IMP]  Automated Name|Number Crawler  
3. [ASTH] View in Map * Will handle encoding  
4. [IMP]  Show all possible names  
5. [IMP]  Define function to handle arguments
```
***
How To
-----
***
**CMD**
```
usage: callerpy.py [-h] [-n number] [-c country] [-cc country code] -l login
                   [-crawl]

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
                        Login Method | twitter, g+, fb (default: None)
  -crawl                Automated Crawler | time int (default: None)

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


