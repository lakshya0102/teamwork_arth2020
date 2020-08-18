import pyttsx3
import os


pyttsx3.speak("namaste welcome to our app!!")
print("*********")

pyttsx3.speak("now i will show the list of services u will get in our app")
x=[ "browers","notepad","player","compiler","virtualbox","movies counter","About some famous personalities of India"]
print(x)

while True:
            print("Tell me what we do for you : "  , end=' ')
            p= input()
            
            print("-----------------")
            
            
           
            if (((("run" in p ) or ("execute" in p) or ("open" in p) or ("launch" in p)))) and (("notepad" in p) or ("editor" in p)) :
             pyttsx3.speak("enjoy services")
             os.system("notepad")
             
            elif (((("tell" in p ) or ("execute" in p) or ("open" in p) or ("launch" in p)))) and (("famous person" in p) or ("personalities" in p)) :
             x=["Amitabh bacchan" , "Narendera modiji" , "Mother terisa"] 
             print(x)
             while True:
                             print("choose your favourite personalities : " , end=' ')
                             p=input()
                             if ("tell "in p) and (("narendre modiji") or ("modiji")):
                               pyttsx3.speak(" India runs of the bicameral legislature as it is a democratic country. It has the president as well as the prime minister who are solely responsible for the country’s welfare. Narendra Modi who is 14th PM of India belongs to BJP. In the present, he owns the status of MP from Varanasi. He also owned the status of Gujarat’s chief Minister for continuous four years. He has been known as the master strategist of his party.")   
                             elif ("about" in p) and (("amitabh bachhan") or ("amitabh ji")):
                               pyttsx3.speak("Amitabh Bachchan pronounced born Inquilaab Srivastava 11 October 1942 is an Indian film actor, film producer, television host, occasional playback singer and former politician. He first gained popularity in the early 1970s for films such as Zanjeer, Deewaar and Sholay, and was dubbed India's  angry young man for his on-screen roles in Bollywood. Referred to as the Shahenshah of Bollywood in reference to his 1988 film Shahenshah, Sadi ka Mahanayak Hindi for, Greatest actor of the century, Star of the Millennium, he has since appeared in over 200 Indian films in a career spanning more than five decades Bachchan is regarded as one of the greatest actors in the history of Indian cinema.")
                             elif ("enlight "in p) and (("mother terisa") or ("terisa")):
                               pyttsx3.speak("Short Biography of Mother Teresa Mother Teresa was born in 1910 in Skopje, the capital of the Republic of Macedonia. Little is known about her early life, but at a young age, she felt a calling to be a nun and serve through helping the poor. At the age of 18, she was given permission to join a group of nuns in Ireland.")
                             elif(( "exit" in p or "close" in p)):
                              pyttsx3.speak("welcome again to main menu")
                              break
            elif(((("run" in p ) or ("execute" in p) or ("open" in p) or ("launch" in p)))) and (("player" in p) or ("media" in p)) :  
             pyttsx3.speak("enjoy services")   
             os.system("wmplayer")
           
            elif(((("run" in p ) or ("execute" in p) or ("open" in p) or ("launch" in p)))) and (("browsers" in p) or ("serach engines" in p)) :  
             pyttsx3.speak("choose which browser u want to go through")
             x=["chrome", "firefox" , "microsoft edge"]
             print(x)
             while True:
                             print("choose your favourite browser: "  , end=' ')
                             p= input()  
                             if (((("run" in p ) or ("execute" in p) or ("open" in p) or ("launch" in p)))) and (("internet explorer" in p) or ("microsoft edge" in p)) :
                              pyttsx3.speak("enjoy services")
                              os.system("msedge")    
                               
                             elif (((("run" in p ) or ("execute" in p) or ("open" in p) or ("launch" in p)))) and (("chrome" in p) or ("google chrome" in p)) :
                              pyttsx3.speak("enjoy services")
                              os.system("chrome")  
                            
                             elif (((("run" in p ) or ("execute" in p) or ("open" in p) or ("launch" in p)))) and (("fox" in p) or ("firefox" in p)) :
                              pyttsx3.speak("enjoy services")
                              os.system("firefox")  
                             
                             elif(( "exit" in p or "close" in p)):
                              pyttsx3.speak("welcome again to main menu")
                              break
            elif(((("run" in p ) or ("execute" in p) or ("open" in p) or ("launch" in p)))) and (("DEVC++" in p) or ("compiler" in p)) :  
             pyttsx3.speak("enjoy services")   
             os.system("devcpp")
            
            elif(((("run" in p ) or ("execute" in p) or ("open" in p) or ("launch" in p)))) and (("virtualbox" in p) or ("virtualmachine" in p)) :  
             pyttsx3.speak("enjoy services")   
             os.system("VirtualBox")
         
            elif(( "exit" in p or "close" in p)):
             pyttsx3.speak("shukriya")
             break

            else :
             print("dont support") 