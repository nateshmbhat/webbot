from selenium import webdriver ;
from selenium.common import exceptions
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
    


    def __find_element__(self , text , tag , classname , id , number ,css_selector , xpath , match_level): 
   
        self.element_to_score = {} ; 
        self.element_to_score_id_set = set();

        def add_to_init_text_matches_score(text_matches_elements : list , score :int )->None:
            '''Extends a dictionary and maps it with the text_matched_element with the score'''
            

            for element in text_matches_elements:
                if(element.id in self.element_to_score_id_set):
                    ''' No need to call the max method if the method call is ordered from most specific to least specific which naturally has the max score if the element is already present '''
                    self.element_to_score[element] = max(self.element_to_score[element] , score ) ; 
                else:
                    self.element_to_score[element] = score ; 
                    self.element_to_score_id_set.add(element.id)

        
        def add_to_init_text_matches_score_from_xpath(xpath , score ):
            add_to_init_text_matches_score( self.driver.find_elements_by_xpath(xpath) , score ) ;




        def find_input_element_for_label(elementlist , score):
            '''This method finds the input tag elements by taking in the label elements and assigns the score argument to the new found input elements and puts them in the  elemenet to score mapping '''

            for element in elementlist:
                possible_input_id = element.get_attribute('for') ; 
                try : 
                    add_to_init_text_matches_score_from_xpath(("//body//input[@id='{}']".format(possible_input_id)) , score )

                    add_to_init_text_matches_score( element.find_elements_by_xpath("../input[contains(translate(@id , '{}' ,'{}' ) , '{}')]".format(text.upper() , text.lower() ,  text.lower())) , score - 5)                    

                    add_to_init_text_matches_score( element.find_elements_by_xpath("/./preceding::input") ,  score - 7)                    

                    add_to_init_text_matches_score_from_xpath(("//body//input[@name='{}']".format(possible_input_id)) , score-6 )

                    add_to_init_text_matches_score( element.find_elements_by_xpath("../input") , score - 10)                    
                    

                except exceptions.NoSuchElementException as E:
                    print("Exception : {}".format(E)) ;


        if tag:
            add_to_init_text_matches_score_from_xpath(("//body//{}[@value='{}']".format(tag , text)) , score=50 )
            add_to_init_text_matches_score_from_xpath(("//body//{}[text()='{}']".format(tag , text)) , score=50 )
            add_to_init_text_matches_score_from_xpath(("//body//{}[contains(text() , '{}') ]".format(tag , text)) , score=49 )
            add_to_init_text_matches_score_from_xpath(("//body//{0}[contains(translate(text()  ,'{1}', '{2}') , '{2}') ]".format(tag , text.upper() , text.lower())) , score=48 )


        if(text.lower() in 'your password'):
            add_to_init_text_matches_score_from_xpath("//body//input[contains(@name , '{}') ]".format('password') , score=47)

        if(text.lower() in ['username' , 'email' , 'login'] and tag=='input'):
            add_to_init_text_matches_score_from_xpath("//body//input[contains(translate(@name , 'USERNAME' , 'username' )  , 'username') or contains(translate(@name ,'EMAIL' , 'email' ) , 'email') or contains(translate(@name , 'LOGIN' , 'login'  ) , 'login' ) ]" , 53 )


        add_to_init_text_matches_score_from_xpath(("//body//input[@value='{}']".format(text)) , score=45 )
        add_to_init_text_matches_score_from_xpath(("//body//input[@placeholder='{}']".format(text)) , score=45 )

        find_input_element_for_label(self.driver.find_elements_by_xpath("//body//label[text()='{}']".format(text)) , score =45)


        add_to_init_text_matches_score_from_xpath(("//body//button[text()='{}']".format(text)) , score=45)


        add_to_init_text_matches_score(self.driver.find_elements_by_link_text("{}".format(text)) , score=43 ) ;

        add_to_init_text_matches_score_from_xpath(("//body//input[contains( @value , '{}')]".format(text)) , score=37 )
        add_to_init_text_matches_score_from_xpath(("//body//input[contains( @placeholder , '{}')]".format(text)) , score=37 )
        find_input_element_for_label(self.driver.find_elements_by_xpath("//body//label[contains( text() , '{}')]".format(text)) , score=37 )


        add_to_init_text_matches_score_from_xpath(("//body//button[contains(text() , '{}')]".format(text)) , score=37 )


        add_to_init_text_matches_score_from_xpath(("//body//input[contains(translate( @value , '{}' , '{}' ) , {})]".format(text.upper() , text.lower() , text.lower())) ,score=33) ; 
        add_to_init_text_matches_score_from_xpath(("//body//input[contains(translate( @placeholder , '{}' , '{}' ) , {})]".format(text.upper() , text.lower() , text.lower())) ,score=33) ; 


        find_input_element_for_label(self.driver.find_elements_by_xpath("//body//label[contains(translate( text() , '{}' , '{}' ) , '{}')]".format(text.upper() , text.lower() , text.lower())) ,score=33) ; 


        add_to_init_text_matches_score_from_xpath(("//body//button[contains(translate(text() , '{}' , '{}' ) , '{}')]".format(text.upper() , text.lower() , text.lower())) ,score=33) ; 


        if(match_level=='loose'):
            add_to_init_text_matches_score_from_xpath("//body//*[@value='{}']".format(text) , score=30 ) ;
            add_to_init_text_matches_score_from_xpath("//body//*[text()='{}']".format(text) , score=30 ) ;


            add_to_init_text_matches_score_from_xpath(("//body//*[contains(text() , '{}')]".format(text)) , score=27 )

            add_to_init_text_matches_score_from_xpath(("//body//*[contains(translate(text() , '{}' , '{}' ) , '{}' )]".format(text.upper() , text.lower() , text.lower())) ,score=25) ; 
                            


        for element in self.element_to_score.keys():
            score = self.element_to_score.get(element) ; 

            # Check ID > score+= 30
            if(id and id==element.get_attribute('id')):
                score += 30

            #Check Class > score+=25
            if(classname and classname in element.get_attribute('class').split()):
                score+=25 

            #Check element tag and check for button or anchor  or input or textarea
            if(tag.lower() in ["button",'link'] and element.tag_name in ['button' , 'a'] or (tag.lower()=='input' and 'input' == element.tag_name) ):
                score+=20
            
            # If user doesn't enter any tag
            if(tag is None and element.tag_name in ['button' , 'a' , 'input'] ):
                score+=17
        

        max_score = max(self.element_to_score.values())
        max_scored_elements = [element for element in self.element_to_score.keys() if (self.element_to_score[element]==max_score)]

        print("\n\nMax SCORES " , max_scored_elements) ; 

        if(len(max_scored_elements)):
            return max_scored_elements[0] if (len(max_scored_elements)<=number) else max_scored_elements[number]


        print("No element found !") ; 
        raise exceptions.NoSuchElementException('Element not found ! ') ; 


    def go_back(self):
        self.driver.back() ;


    def go_to(self , url):
        self.driver.get(url) 



    def click(self , text='' , tag='button', id ='' , classname ='',  number = 1 , css_selector='' , xpath='' , match_level = 'loose' ):
        element = self.__find_element__(text , tag , classname , id , number , css_selector , xpath , match_level) 
        element.click() ; 
        

    def type(self , text , into , clear = True , tag='input', id ='' , classname ='',  number = 1 , css_selector='' , xpath='' , match_level = 'loose' ):
        element = self.__find_element__(into , tag , classname , id , number , css_selector , xpath , match_level)
        if(clear):
            element.clear() 
        element.send_keys(text)
        
        pass;



class Chrome:
    pass


if(__name__=='__main__'):
    aton = Browser() ; 
    aton.go_to('http://daedalcrafters.pythonanywhere.com') 
    # aton.type("hello" , 'Username')
    # aton.type("itsme" , 'Password')
    aton.click('login' , tag='button')