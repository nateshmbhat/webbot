webbot
======


Web automation library for python for web browser automation and end to
end UI testing.

webbot provides a much feature rich automation than selenium for all
kinds of automation of webpage. Since the major portion of web
automation is to perform actions like click and type into webpage
elements , webbot automatically handles finding the right elements to
perform the actions.

Features :
----------

-  Use any combination of selectors like id, name, text, css etc to
   perform actions on elements with one line of code.
-  Automate and test pages loaded dynamically by javascript.
-  Click any button or link without having to worry about finding the
   element first or knowing css_selectors , xpath etc
-  Smart scoring algorithm which finds the best matching elements on
   which you want to perform the action .
-  Automation designed to work even in case of webpages with dynamically
   changing id and classname
-  Immensely minimizes the code required for performing input actions
   like clicks and keyboard actions.
-  Get webpage source , cookies , total tabs , webpage title etc..
-  Simulate key presses and special key combinations
-  Bidirectional scrolling
-  Perform an action on webpage elements by applying various filters to
   select the elements .
-  Perfrom action on multiple elements at once.
-  If certain elements don’t have text or visible property , then use
   either their id , class , css_selector , xpath , tag etc.
-  The entire automation process can be made without having to open the
   browser window i.e in the background as a console process (see docs
   for more details )

--------------

Installation :
--------------

``pip install webbot``

If “No distribution found error occurs” just update setuptools using
``pip install --upgrade setuptools``

Quickstart :
------------

Demo code 0 :
'''''''''''''

.. code:: python

   from webbot import Browser 
   web = Browser()
   web.go_to('google.com') 
   web.type('hello its me')  # or web.press(web.Key.SHIFT + 'hello its me')
   web.press(web.Key.ENTER)
   web.go_back()
   web.click('Sign in')
   web.type('mymail@gmail.com' , into='Email')
   web.click('NEXT' , tag='span')
   web.type('mypassword' , into='Password' , id='passwordFieldId')
   web.click('NEXT' , tag='span') # you are logged in . woohoooo

Demo code 1 :
'''''''''''''

**If multiple buttons with similar properties are to be clicked at
once**

.. code:: python

   web = Browser()
   web.go_to('siteurl.com')
   web.click('buttontext' , multiple = True)

Demo code 2 :
'''''''''''''

**If there are multiple elements and you want to perform action on one
of them**

.. code:: python

   web = Browser()
   web.go_to('siteurl.com')

   # types the text into the 3rd input element when there are multiple input elements with form-input class
   web.type('im robo typing' , number = 3 , classname="form-input" ) 

   web.click('Post')

--------------

Links :
-------

-  Full Documentation : https://webbot.readthedocs.io
-  Project home : https://github.com/nateshmbhat/webbot

.. |Downloads| image:: https://pepy.tech/badge/webbot/week

