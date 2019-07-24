Documentation for **webbot**  ^_^
=============================================

webbot is a web browser automation library which is built upon `Selenium <https://www.seleniumhq.org/>`_ and has a feature-rich library with hassle-free automation of the web browsers for developers and end users alike.

The library is used to automate the actions of a user interacting with the browser.

Almost all the time, the workflow of any web automation is to find an element and perform some action like click or type into an input field etc on that element. webbot takes care of all these thing internally and gives direct methods to **click, type, special key press, scroll, switch_tabs** and a whole lot more functionalities without you having to worry about implementing everything from scratch yourself.

HomePage : https://github.com/nateshmbhat/webbot


Quick demo code ^_^
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

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
        web.click('NEXT' , tag='span') # you are logged in . oohoooo

        #--------------------------------------------------------------------------

        # If multiple buttons with similar properties are to be clicked at once
        web = Browser()
        web.go_to('siteurl.com')
        web.click('buttontext' , multiple = True)

        #--------------------------------------------------------------------------

        # If there are multiple elements and you want to perform action on one of them : 
        web = Browser()
        web.go_to('siteurl.com')

        # types the text into the 3rd input element when there are multiple input elements with form-input class
        web.type('im robo typing' , number = 3 , classname="form-input" ) 
        


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :numbered:


   installation
   license
   features
   webbot


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
