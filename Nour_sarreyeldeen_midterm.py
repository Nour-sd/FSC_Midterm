
import webbrowser, selenium
import json 

from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlopen

class Browser_tab():
 def __init__(self, Title, URL, TabNumber):
  self.title = Title
  self.URL = URL
  self.TabNumber = TabNumber
  self.driver = webdriver.Chrome()


class Browser_tabs():
 
 def __init__(self):
  self.tabs = []

 def openTab(self):
   url = input("enter a valid URL:")
   title = input("enter title: ")
   TabNumber = len(self.tabs) + 1
   link = "https://" + url
   tab = Browser_tab(title, link, TabNumber)
   self.tabs.append(tab)
   print(link)
   tab.driver.get(link)
    
 def close_Tab(self):
   if len(self.tabs) == 0:
    print("no open tabs.")
   else:
     choice= int(input("enter Tab Number: "))-1
     if (0<= choice <= len(self.tabs)):
      tab = self.tabs[choice]
      tab.driver.close()
      del self.tabs[choice]
     else:
      print ("Invalid Choice!")

 def switch_Tab(self):
   if len(self.tabs)==0:
    print("no open tabs.")
   else:
    choice = int(input("Enter tab number:")) - 1
    if (0<= choice <= len(self.tabs)):
      tab = self.tabs[choice]
      page = urlopen(tab.URL)
      html_bytes = page.read()
      html = html_bytes.decode("utf-8") 
      print(html)
    else:
      print ("Invalid Choice!")
      
  
 def display_all_Tabs(self):
   if len(self.tabs)==0:
    print("no open tabs.")
   else:
    for i in range(len(self.tabs)):
      print(f'{self.tabs[i].TabNumber}. {self.tabs[i].title}')

 def clear_all_Tabs(self):
   if len(self.tabs)==0:
    print("no open tabs.")
   else:
     for i in range(len(self.tabs)):
       self.tabs[i].driver.close()
     self.tabs.clear()
  
 def save_Tabs(self):
   if len(self.tabs)==0:
    print("no open tabs.")
   else:
     file_path = input("enter file path:")

#def open_nested_tab():
  
  
#def save_tabs():
  
#def import_tabs():

browser = Browser_tabs()

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
      browser.openTab()
      #open_tab()
    elif choice == 2:
      browser.close_Tab()
    elif choice == 3:
      browser.switch_Tab()
    elif choice == 4:
      browser.display_all_Tabs()
    #elif choice == 5:
      #open_nested_tab()
    elif choice == 6:
     browser.clear_all_Tabs()
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

 



