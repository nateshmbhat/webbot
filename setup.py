import platform
from setuptools import setup

install_requires = ['selenium']

with open('README.rst' , 'r') as f:
    long_description = f.read() 

setup(
    name='webbot',
    packages = ['webbot','webbot.drivers'] ,
    version = '0.0.1',
    long_description = long_description , 
    description = 'Web Browser automation library for python with more features and simpler api than selenium' ,
    author = 'Natesh M Bhat' ,
    url = 'https://github.com/nateshmbhat/webbot',
    author_email = 'nateshmbhatofficial@gmail.com' ,
    keywords=['webbot', 'selenium' , 'autoweb','automate' , 'automation' ,'web' , 'autoweb' , 'auto' , 'pyauto', 'pyautogui'],
    classifiers = [] ,
)