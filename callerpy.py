
# callerpy.py - Truecaller Web Client 
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the <organization> nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Report any issues with this script to <mad_dev@linuxmail.org>


__author__ = ["Ammer Almadani::Mad_Dev"]
__email__  = ["mad_dev@linuxmail.org", "mail@sysbase.org"]


from flask import Flask, request, render_template, jsonify, abort, make_response, flash
import os
from selenium import webdriver
import re
import json
import time
import urllib
import urllib2
import string
import random
import sendgrid
from sendgrid import SendGridError, SendGridClientError, SendGridServerError
from form import searchform, emailForm


RECAPTCHA_OPTIONS = {'theme': 'red'}
RECAPTCHA_PUBLIC_KEY = "RECAPTCHA_PUBLIC_KEY"
RECAPTCHA_PRIVATE_KEY = "RECAPTCHA_PUBLIC_KEY"

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config.from_object(__name__)
path = app.root_path + '/templates/'
p = str(os.path.dirname(os.path.abspath(__file__)))

app.secret_key = 'the dog never left the house'


class CallerPy():

        def truecaller(self, country, number):
            webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (X11; Linux i686; rv:25.0) Gecko/20100101 Firefox/25.0'
            d = webdriver.PhantomJS('phantomjs/bin/phantomjs')
            L = 'http://www.facebook.com'
            d.get(L)
            time.sleep(0.5)
            user = d.find_element_by_id('email')
            user.send_keys('YOUR_EMAIL')
            password = d.find_element_by_id('pass')
            password.send_keys('YOUR_PASSWORD')
            signin = d.find_element_by_id('loginbutton')
            signin.send_keys("\n")
            final_url = 'https://tcfb.truecaller.com/request.php?search&q=%s&country=%s' %(number, country) 
            d.get('https://apps.facebook.com/truecaller/')
            d.get('https://tcfb.truecaller.com/')
            d.get(final_url)
            out = d.page_source
            p = re.compile(r'<.*?>')
            j = p.sub('', out)
            u = json.loads(j)
            name = u['SR']['NAME']
            national_number = u['SR']['NATIONAL_NUMBER']
            address = u['SR']['ADDRESS']
            street = u['SR']['STREET']
            zipcode = u['SR']['ZIPCODE']
            area = u['SR']['AREA']
            con = u['SR']['COUNTRY']
            company_name = u['SR']['COMPANY_NAME']
            twitter_name = u['SR']['TWITTER_NAME']
            twitter_screen_name = u['SR']['TWITTER_SCREEN_NAME']
            return name, national_number, address, street, zipcode, area, con, company_name, twitter_name, twitter_screen_name

	def country_by_code(self, code):
                a = open('scripts/countries', 'r')
                b = a.read()
                p = re.findall('[a-z]{1,}', b)
                o = re.findall('[0-9]{1,}', b)
                for i, e in zip(p, o):
                        if str(code) == str(e):
                                print 'Using Country By Code', code, i
                                return i

def run_once(f):
	def wrapper(*args, **kwargs):
		if not wrapper.has_run:
           		wrapper.has_run = True
            		return f(*args, **kwargs)
    	wrapper.has_run = False
	print str(f) + ' Running Once'
    	return wrapper

def sms(message, number):
    url = 'http://www.redoxygen.net/sms.dll?Action=SendSMS&'
    param = {}
    param['AccountId'] = '#'
    param['Password'] = '#'
    param['Email'] = '#'
    param['Recipient'] = number
    param['Message'] = str(message)
    url_ = urllib.urlencode(param)
    url_full = url + url_
    param = urllib2.urlopen(url_full)
    print number, 'code: ' + param.readline()


def shuff(passwd):
    shuffle = list(passwd)
    random.shuffle(shuffle)
    passwd = ''.join(shuffle)
    print passwd
    return passwd

def char_select(strg, inp):
    i = 0
    passwd = ''
    while i < inp:
        passwd += ''.join(random.choice(strg))
        i += 1
    return passwd

def digits(inp):
    return char_select(string.digits, inp)

def lower(inp):
    return char_select(string.ascii_lowercase, inp)

def upper(inp):
    return char_select(string.ascii_uppercase, inp)

##BEGIN PAGE RENDERING##

@app.route('/')
def index():
        return render_template("index.html", stat='CallerPy')

x = CallerPy()


#@app.route('/search/world/api/v1/REST', methods = ['GET', 'POST'])
#def paramWorld():
#        number = request.args.get('number', None)
#        code = request.args.get('cc', None)
#        if number is None:
#                try:
#                        abort(400)
#                except:
#                        return make_response(jsonify({'error':'wrong param'}))
#                #return render_template("view.html", contents='Error...Must Enter Number')
#        elif number is not None:
#                if code == '54':
#                        try:
#                            country = 'argentina-buenosaires'
#                            a = x.truecaller(country, number)
#                            print a
#                        except:
#                            return make_response(jsonify({'Server-OverLoad': 'CallerPy error::163*::Try Again In A few minutes::Argentina::API'}))
#                elif code == '245':
#                        try:
#                            country = 'guinea-bissau'
#                            a = x.truecaller(country, number)
#                            print a
#                        except:
#                            return make_response(jsonify({'Server-OverLoad': 'CallerPy error::228*::Try Again In A few minutes::Guinea::API'}))
#                elif code == '91':
#                        try:
#                            country = 'india-other'
#                            a = x.truecaller(country, number)
#                            print a
#                        except:
#                            return make_response(jsonify({'Server-OverLoad': 'CallerPy error::228*::Try Again In A few minutes::India::API'}))
#                else:
#                        try:
#                            a =  x.truecaller(x.country_by_code(code), number)
#                            print a
#                        except:
#                            return make_response(jsonify({'Server-OverLoad': 'CallerPy error::228*::Try Again In A few minutes::WORLD::API'}))
#                try:
#                    rest = [{
#                            'NAME': a[0],
#                            'NUMBER': a[1],
#                            'ADDRESS': a[2],
#                            'STREET': a[3],
#                            'ZIPCODE': a[4],
#                            'AREA': a[5],
#                            'COUNTRY': a[6],
#                            'COMPANY_NAME':a[7],
#                            'TWITTER_NAME': a[8],
#                            'TWITTER_SCREEN_NAME': a[9]}]
#                    
#                    return jsonify({'getWorld': rest})
#                except:
#                    rest = [{
#                            'Field': a
#                            }]
#                    return jsonify({'Error_Or_Something_Went_Wrong': rest})               
#        else:
#                return make_response(jsonify({'error': 'CallerPy error::901*'}))


#cc_form_name = shuff(upper(5)+lower(12)+digits(21))
#@app.route('/search', methods = ['GET', 'POST'])
#def param():

 #       number = request.args.get('local_number', None)
  #      code = request.args.get('cc', None)
   #     if number is None:
    #            return render_template("view.html", contents='Error...Must Enter Number')
     #   elif number is not None:
      #          if code == '54':
       #                 try:
        #                    country = 'argentina-buenosaires'
         #                   a = x.truecaller(country, number)
          #                  print a
           #             except:
            #                sms('CALLERPY::SYSTEM-DOWN::ARGENTINA', '0503297977')
             #               return make_response(jsonify({'Server-OverLoad': 'CallerPy error::158*::Try Again In A few minutes::Argentina::Form'}))
              #  elif code == '245':
               #         try:
                #            country = 'guinea-bissau'
                 #           a = x.truecaller(country, number)
                  #          print a
                   #     except:
                    #        sms('CALLERPY::SYSTEM-DOWN::GUINEA-BISSAU', '0503297977')
                  #          return make_response(jsonify({'Server-OverLoad': 'CallerPy error::228*::Try Again In A few minutes::Guinea::Form'}))
              #  elif code == '91':
               #         try:
                #            country = 'india-other'
                 #           a = x.truecaller(country, number)
                  #          print a
                   #     except:
                    #        sms('CALLERPY::SYSTEM-DOWN::INDIA', '0503297977')
                     #       return make_response(jsonify({'Server-OverLoad': 'CallerPy error::228*::Try Again In A few minutes::India::Form'}))
             #   else:
              #          try:
               #             a =  x.truecaller(x.country_by_code(code), number)
                #            print a
                 #       except:
                  #          sms('CALLERPY::SYSTEM-DOWN::WORLD', '0503297977')
                   #         return make_response(jsonify({'Server-OverLoad': 'CallerPy error::228*::Try Again In A few minutes::WORLD::Form'}))
                
               # return render_template("view.html", contents=a[0], number=number)
       # else:
        #        return render_template("view.html", contents='CallerPy error::900*')
           
    
@app.route('/form', methods = ['GET', 'POST'])
def formCatch():
        form = searchform()
        send = emailForm()
        if request.method == 'POST':
            
            number = request.form.get('local_number', None)
            code = request.form.get('cc', None)
            if number is None:
                    return render_template("index.html", stat='Error...Must Enter Number')
            elif number is not None:
                    if code == '54':
                            try:
                                country = 'argentina-buenosaires'
                                a = x.truecaller(country, number)
                                print a
                            except:
                                sms('CALLERPY::SYSTEM-DOWN::ARGENTINA', '0503297977')
                                return make_response(jsonify({'Server-OverLoad': 'CallerPy error::158*::Try Again In A few minutes::Argentina::Form'}))
                    elif code == '245':
                            try:
                                country = 'guinea-bissau'
                                a = x.truecaller(country, number)
                                print a
                            except:
                                sms('CALLERPY::SYSTEM-DOWN::GUINEA-BISSAU', '0503297977')
                                return make_response(jsonify({'Server-OverLoad': 'CallerPy error::228*::Try Again In A few minutes::Guinea::Form'}))
                    elif code == '91':
                            try:
                                country = 'india-other'
                                a = x.truecaller(country, number)
                                print a
                            except:
                                sms('CALLERPY::SYSTEM-DOWN::INDIA', '0503297977')
                                return make_response(jsonify({'Server-OverLoad': 'CallerPy error::228*::Try Again In A few minutes::India::Form'}))
                    else:
                            try:
                                a =  x.truecaller(x.country_by_code(code), number)
                                print a
                            except:
                                sms('CALLERPY::SYSTEM-DOWN::WORLD', '0503297977')
                                return make_response(jsonify({'Server-OverLoad': 'CallerPy error::228*::Try Again In A few minutes::WORLD::Form'}))
                        
                    return render_template("view.html", contents=a[0], number=number, form=send, add='')
            else:
                return render_template("view.html", contents='CallerPy error::900*')
            
        elif request.method == 'GET':

            return render_template("form.html", form=form)

@app.route('/send', methods = ['GET', 'POST'])
def sendEmail():
    send = emailForm()
    number_form_name = shuff(upper(12)+lower(21)+digits(5))
            #email = request.args.get('email', None)
    email = request.form.get('email', None) 
    name = request.form.get('name', None)
    number = request.form.get('number', None)
    if send.validate_on_submit():

            #final_email = str(email)+'@sysbase.org'

        messages = '''

        <html>
        <head>
        <title></title>
        <meta content='text/html; charset=3DUTF-8' http-equiv='Content-Type'>
        <style media='screen' type='text/css'>

        body {
          width: 50%;
          text-align: center

        }


        object, embed {
            float: none;
            clear: both;
            border: 0;
            display: block;
        }

        a img {
            text-decoration: none;
            border: 0;
        }

        a, a:visited {
            border: 0;
            color: #33ccff;
            text-decoration: none;
        }

        p {
            clear: both;

        }

        .bord {
         -webkit-box-shadow: 0px 2px 10px 0px rgba(50, 50, 50, 0.58);
        -moz-box-shadow: 0px 2px 10px 0px rgba(50, 50, 50, 0.58);
        box-shadow:  0px 2px 10px 0px rgba(50, 50, 50, 0.58);
        border: 0px;
        }

        @media only screen and (max-width: 480px) {
          .button-action{font-size:23px !important}
          .float-cell{display:block;}
        }
        @media only screen and (max-width: 320px) {
          .button-action{font-size:20px !important}
          .float-cell{display:block;}
        }
        @media only screen and (max-width: 280px) {
          .button-action{font-size:16px !important;padding-left:20px !important;padding-right:20px !important}
          .float-cell{display:block;}
        }
        </style>
        </head>

        <body>
        <div class='bord'>
        </p>
        <p style="font-size: 24px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333333;line-height: 1.2;padding:5px 0 0;">
        Name: '''+name+'''
        </br>
        Number: '''+number+'''
        </p>


        </div>
        <img src="http://www.sysbase.org/callerpy/img/callerPy.png" alt="CallerPy"  width="70px"/></br></br>
        Email ID: '''+number_form_name+'''</br>
        If you didn't send this email, please send the Email ID to <a href="mailto:mail@sysbase.org">mail@sysbase.org</a>
        </body>
        </html>
            '''
            #mesg = 'Name: %s Number: %s \n CallerPy \n Email ID: %s' %(name, number, number_form_name)
        sg = sendgrid.SendGridClient('#', '#', raise_errors=True)
        message = sendgrid.Mail()
        message.add_to(email)
        message.set_subject('Number Request')
        message.set_html(messages)
            #message.set_text(mesg)
        message.set_from('CallerPy <mail@sysbase.org>')

        try:
            print 'Sending Email...'
            status, msg = sg.send(message)
            return render_template("view.html", contents=name, number=number, form=send, add='Email Sent to %s' %email)
        except SendGridClientError:
            return render_template("view.html", contents=name, number=number, form=send, add='Client Error')
        except SendGridServerError:
            return render_template("view.html", contents=name, number=number, form=send, add='Server Error')

    return render_template("view.html", contents=name, number=number, form=send, add='Please enter a correct RECAPTCHA')    

@app.errorhandler(400)
def not_found(error):
        return make_response(jsonify({'error': '400'}), 400)

@app.errorhandler(500)
def not_found500(error):
        return make_response(jsonify({'error': '500'}), 500)

