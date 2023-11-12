
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
      new_tabs = []
      for i in range(len(self.tabs)):
        new_tab = {}
        new_tab["title"] = self.tabs[i].title
        new_tab["URL"] = self.tabs[i].URL
        new_tab["TabNumber"]=self.tabs[i].TabNumber
        new_tabs.append(new_tab)
      file = json.dumps(new_tabs)
      print(file)
      file_path = input("enter file path:")
      document = open(file_path, "w")
      document.write(file)
      document.close()
    
 def import_Tabs(self):
  file_path = input("enter file path:")
  file = open(file_path, 'r')
  data = file.read()
  file.close()
  result = json.loads(data)
  if len(self.tabs)>0:
     for i in range(len(self.tabs)):
       self.tabs[i].driver.close()
     self.tabs.clear()
  for tab in result:
    title = tab['title']
    URL = tab['URL']
    TabNumber = tab['TabNumber']
    tab = Browser_tab(title, URL, TabNumber)
    self.tabs.append(tab)
   
#def open_nested_tab():

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
    elif choice == 7:
      browser.save_Tabs()
    elif choice == 8:
      browser.import_Tabs()
    elif choice == 9:
      break
    else:
     print("Invalid choice. try again...")

if __name__ == "__main__":
    menu()

 

#  >>>>    Conclusion:The program enters an infinite loop,
#         allowing the user to interact with the browser tabs until they choose the option to exit.
#         The code provides a simple command-line interface for managing multiple browser tabs using
#         Selenium for automation and JSON for saving and loading tab information.
#         The user can open, close, switch between tabs, and perform other actions through the provided menu.
#         Used: necessary libraries
#         Define a class for individual browser tabs
#         Define a class for managing multiple browser tabs
#         Method to open a new tab
#         Method to close a tab
#         Method to switch to a tab and display its HTML content
#         Method to display information about all open tabs
#         Method to close all open tabs
#         Method to save information about open tabs to a JSON file
#         Method to import information about tabs from a JSON file
#         Create an instance of Browser_tabs
#         Define a menu function for user interaction
#         Selenium: The Selenium library is used for web automation. 
#         In this code,
#         It is used to control and interact with the Chrome browser.
#         JSON: The JSON library is used for working with JSON data.
#         In this code, it is used to save and load information about browser tabs to and from a JSON file.
 


#>>>>         resources links:#https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
              #https://realpython.com/python-web-scraping-practical-introduction/#build-your-first-web-scraper
              #https://www.w3schools.com/python/python_json.asp#:~:text=If%20you%20have%20a%20Python,the%20json.dumps()%20method
              #https://www.geeksforgeeks.org/convert-class-object-to-json-in-python/
              #https://pythonexamples.org/python-json-to-list/
              #https://www.w3schools.com/python/python_classes.asp
              #https://sparkbyexamples.com/python/convert-python-list-to-json/#:~:text=dumps()%20method%20to%20convert,boolean%2C%20and%20None%20into%20JSON.
