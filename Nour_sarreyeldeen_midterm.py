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
  Tab["URL"] = input("enter a valid URL:")
  Tab["Title"] = input("enter title: ")
  Tabs.append(Tab)
  link = "https://" + Tab["URL"]
  print(link)
  driver.get(link)
def close_tab(i):
  if 0 <= i < len(Tabs):
    Tabs[i](driver.close)
    del Tabs[i]
  else:
    print("Invalid tab index")
    
def switch_tabs(Tab):
  link = "https://" + Tab["URL"]
  driver.switch_to.window(driver.window_handles[1])
  driver.get(link)
  driver.switch_to.window(driver.window_handles[0])

#def close_tab():
#def close_tab():
  
#def switch_tab():
#def display_all_tabs():
  #print(f"{Tab['title']} {Tab['URL']}")
#def open_nested_tab():
  
#def clear_all_tabs():
  
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

 



