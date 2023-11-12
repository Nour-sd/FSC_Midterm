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
import json 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time



Tabs = []
driver = webdriver.Chrome() 



def open_tab():
  Tab = {}
  Tab["URL"] = input("enter a valid URL:")
  Tab["Title"] = input("enter title: ")
  Tab["number"] = len(Tabs) + 1
  link = "https://" + Tab["URL"]
  print(link)
  driver.get(link)
  Tabs.append(Tab)
def close_tab():
  
  if Tabs:
   for i, tab in enumerate(Tabs):
    choice = int(input("Enter tab number: ")) - 1
    if 0 <= choice < len(Tabs):
     driver.switch_to.window(driver.window_handles[choice])
     driver.close()
     del Tabs[choice]
    else:
     print("Invalid tab number, try again...")
  else:
    driver.close()
def switch_tab():
 p = driver.current_window_handle

 chwd = driver.window_handles

 for w in chwd:
  if(w!=p):
    driver.switch_to.window(w)
  break
#def display_all_tabs():
 
#def open_nested_tab():
  
def clear_all_tabs():
    driver.close()
    Tabs.clear()
    print("Tabs closed.")
  
#def save_tabs():
  
#def import_tabs():

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
    elif choice == 3:
      switch_tab()
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
    elif choice == 9:
      break
    else:
     print("Invalid choice. try again...")

if __name__ == "__main__":
    menu()

 



