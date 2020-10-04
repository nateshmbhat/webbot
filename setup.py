from setuptools import setup



VERSION="0.34"


with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='webbot',


    packages = ['webbot','webbot.drivers'] ,
    version = VERSION , 
    long_description = long_description , 
    install_requires = ['selenium'] , 
    package_data = {'' : [r'drivers/*']},
    description = 'Web Browser automation and testing library for python with more features and simpler api than selenium' ,
    author = 'Natesh M Bhat' ,
    url = 'https://github.com/nateshmbhat/webbot',
    author_email = 'nateshmbhatofficial@gmail.com' ,
    keywords=['webbot', 'selenium' , 'autoweb','automate' , 'automation','pyttsx3','bs4' , 'beautiful soup' ,'web' , 'autoweb' , 'auto' , 'pyauto', 'pyautogui'],
    classifiers = [
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'License :: OSI Approved :: MIT License' , 
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7'
          ] 

)
