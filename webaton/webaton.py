from selenium import webdriver ; 
from time import sleep 
import sys , argparse , os  


class Browser:

    def __init__(self , showWindow = False ):
        options = webdriver.ChromeOptions()
        if(showWindow):
            options.set_headless(headless=True) ; 

        driverfilename = "chrome_linux" if  os.name=='posix' else "chrome_windows.exe" if os.name=='nt' else "chrome_mac" ; 
        driverpath =  os.path.join(os.path.split(__file__)[0] , 'drivers{0}{1}'.format(os.path.sep , driverfilename))
        self.driver = webdriver.Chrome(executable_path=driverpath , chrome_options=options)
    

    def __find_element__(self , text , type , tag , classname , id , number ): 
        '''
        Preference :
        
        typetag:classname>id:text
        typetag:classname>id
        typetag:classname>id
        typetag:classname>anchor:text=text
        typetag:classname>button:text=text
        typetag:classname
        
        '''






    def go_back(self):
        self.driver.back() ;


    def go_to(self , url):
        self.driver.get(url) 


    def click(self , text , type = "button" , tag=None , id = None , classname =None , xpath = None , number = 1 ):
        element = self.__find_element__(text , type , tag , classname , id , number) 


    def write(self , into=None):
        pass;



class Chrome:
    pass
