Documentation for **webbot**  ^_^
=============================================

webbot is a web browser automation library which is built upon selenium and has a feature rich library with hassle-less automation of the web browsers for developers and end users alike.

The library is used to automate the actions of a user interacting with the browser.

Almost all the time , the workflow of any web automation is to find an element and perform some action like click or type into an input field etc on that element. webbot takes care of all these thing internally and gives direct methods to **click , type , special key press  , scroll , switch_tabs** and a whole lot more functionalities without having to worry about implementing everything from scracth yourself.

HomePage : https://github.com/nateshmbhat/webbot


Quick demo code ^_^
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

        from webbot import Browser
        web = Browser() 
        web.go_to('google.com')
        web.click('Sign In')
        web.type('mymail@gmail.com' , into = 'Email')
        web.click('Next') 
        web.type('password' , into = 'password') 
        web.click('Next')
        web.scrolly(100) 
        web.click('inbox')
        

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
