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
    


    def __find_element__(self , text , type , tag , classname , id , number ,css_selector , xpath): 
        '''
        Preference Order :
        css_selector
        xpath

        typetag:classname>id:text[number]
        typetag:id:text[number]
        typetag:classname:text[number]
        typetag:classname>anchor:text=text[number]
        typetag:classname>button:text=text[number]
        typetag:classname:text=text[number]
        typetag:*:text=text[number]
        anchor:text=text[number]
        button:text=text[number]
        input:placeholder=text[number]
        input:value=text[number]
        textarea:value=text[number]
        textarea:placeholder=text[number]
        '''

        # valid_element_types = ['button' , 'input' , 'textarea' , 'a' , 'img' , 'div']
        # css_selectors_order = [
        #     "{}.{}#{}".format( type if type in valid_element_types else "a" if (type=="link" or type=="href") else ""  , classname , id ) , 
        #     "{}#{}".format( type if type in valid_element_types else "a" if (type=="link" or type=="href") else ""  , id ) , 
        #     "{}.{}".format( type if type in valid_element_types else "a" if (type=="link" or type=="href") else ""  , classname ) , 
        #     "{}.{} a".format( type if type in valid_element_types else "a" if (type=="link" or type=="href") else ""  , classname ) , 
        #     "{}.{} button".format( type if type in valid_element_types else "a" if (type=="link" or type=="href") else ""  , classname ) , 
        #     "{}.{} button".format( type if type in valid_element_types else "a" if (type=="link" or type=="href") else ""  , classname ) , 
        #     "{}".format( type if type in valid_element_types else "a" if (type=="link" or type=="href") else ""  ),
        # ]
    
        self.element_to_score = {} ; 

        def add_to_init_text_matches_score(text_matches_elements : list , score :int )->None:
            '''Extends a dictionary and maps it with the text_matched_element with the score'''
            
            id_sets = set();

            if(self.element_to_score.keys()):
                for match_element_key in self.element_to_score.keys():
                    id_sets.add(match_element_key.id) 

            for element in text_matches_elements:
                if(element.id in id_sets):
                    ''' No need to call the max method if the method call is ordered from most specific to least specific which naturally has the max score if the element is already present '''
                    self.element_to_score[element] = max(self.element_to_score[element] , score ) ; 
                else:
                    self.element_to_score[element] = score ; 
                



        add_to_init_text_matches_score(self.driver.find_elements_by_xpath("//body/*[text()='{}']".format(text)) , score=15 ) ;
        add_to_init_text_matches_score(self.driver.find_elements_by_link_text("{}".format(text)) , score=13 ) ;

        add_to_init_text_matches_score(self.driver.find_elements_by_xpath("//body/*[contains(text() , {})]".format(text)) , score=10)

        add_to_init_text_matches_score(self.driver.find_elements_by_xpath("//body/*[contains(translate(text() , {} , {} ) , {})]".format(text.upper() , text.lower() , text.lower())) ,score=7) ; 


        for element in self.element_to_score.keys():
            score = self.element_to_score.get(element) ; 

            # Check ID > score+= 30
            if(id and id==element.get_attribute('id')):
                score += 30

            #Check Class > score+=20
            if(classname and classname==element.get_attribute('class')):
                score+=20 

            #Check element tag and check for button or anchor  or input or textarea
            
            




    def go_back(self):
        self.driver.back() ;


    def go_to(self , url):
        self.driver.get(url) 


    def click(self , text='' , type = "button" , tag='', id ='' , classname ='',  number = 1 , css_selector='' , xpath=''):
        element = self.__find_element__(text , type , tag , classname , id , number , css_selector , xpath) 


    def write(self , into=None):
        pass;



class Chrome:
    pass
