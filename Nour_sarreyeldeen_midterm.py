# menu :
# openinig tabs : open a url
# close tab : close it
# switch tab : switch between tabs
#display all tabs: tabs html url read
# open nested tab :tab tab b2alb tab
# clear all tabs :
# save tabs :
# import tabs :
# exit :
import webbrowser, selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


Tabs = []
driver = webdriver.Chrome() 

def open_tab():
  Tab = {}
  Tab["URL"] = input("enter a valid URL:https:// ")
  Tab["Title"] = input("enter title")
  #driver = webdriver.Chrome() 
  #Tab["content"] = webbrowser.open(Tab["URL"])
  #driver.get(Tab["URL"]) 
  Tabs.append(Tab)
  driver.get("https://www.google.com/")
  time.sleep(99999999)
  
 
 
def close_tab():
  
  
  url = "https://www.google.com/"
    
  # Fetching the Url 
  #driver.get(url) 
  driver.close()




#def switch_tabs():

#def close_tab():
#def close_tab():
  
#def switch_tab():
#def display_all_tabs():
  #print(f"{Tab['title']} {Tab['URL']}")
#def open_nested_tab():
  
#def clear_all_tabs():
  
#def save_tabs():
  
#def import_tabs():
  
def exit_():
  aa = 3
  
def menu():
 print("Menu :")
 print("1. Openinig tabs")
 print("2. Close tab")
 print("3. Switch tab")
 print("4. Display all tabs")
 print("5. Open nested tab")
 print("6. Clear all tabs")
 print("7. Save tabs")
 print("8. Import tabs")
 print("9. Exit")

 while True:
    choice = int(input("Enter your choice : "))

    if choice == 1:
      open_tab()
    elif choice == 2:
      close_tab()
    #elif choice == 3:
      #switch_tab()
    #elif choice == 4:
      #display_all_tabs()
    #elif choice == 5:
      #open_nested_tab()
    #elif choice == 6:
     # clear_all_tabs()
    #elif choice == 7:
      #save_tabs()
    #elif choice == 8:
    #  import_tab()
    #elif choice == 9:
     # exit_()
     # break
    else:
      print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    menu()

 



