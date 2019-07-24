Installation
------------

Introduction
~~~~~~~~~~~~

webbot is a web browser automation library which is built upon the Selenium framework and works at a much higher level and eliminates much of the code you would need in Selenium.

Almost all the time, the workflow of any web automation is to find an element and perform some action like click or type into an input field etc on that element. webbot takes care of all these thing internally and gives direct methods to **click, type, special key press, scroll, switch_tabs** and a whole lot more functionalities without you having to worry about implementing everything from scratch yourself.


Installation:
~~~~~~~~~~~~~

`pip install webbot`


Usage :
~~~~~~~

.. code-block:: python
   
   from webbot import Browser
   driver = Browser()


