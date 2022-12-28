#  First we would import all the libraries:
import requests
from bs4 import BeautifulSoup

# This is the website that I am going to scrape:
url = "https://www.codewithharry.com/"

# Now we will get the contents of the website:
r=requests.get(url)
htmlContent=r.content
# print(htmlContent)
# Now we would parse the HTML:
soup= BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)
#Html tree traversal:
# title=soup.title 
# print(title) title of html page
# Commonly used types of objects:
# 1.Tag print(type(title))
# 2.Navigable string print(type(title.string))
# 3.Beautiful soap print(type(soup))
# 4.comment
# markup="<p><!-- This is acomment --></p>"
# soup2=BeautifulSoup(markup)
# print(soup2.p.string)


#title of html page:
title=soup.title 

#get all paragraphs from the page:
paras=soup.find_all('p')
# print(paras)

# #get first paragraph:
# print(soup.find('p'))
#get class used in first paragraph:
# print(soup.find('p',['class']))
#to print all elements which contain class=lead
# print(soup.find_all('p',class_='lead'))

# to get text from the tags/soup:
# print(soup.find('p').get_text()) #would print the text inside the first para tags.
# print(soup.get_text())

#get all anchor tags from the page:
anchors=soup.find_all('a')

#to get all the links on the page:
# for link in anchors:
#     print(link.get('href'))
# all_links=set()
# for link in anchors:
#     if(link.get('href')!='#'):
#         linkText="https://www.codewithharry.com"+ link.get('href')
#         all_links.add(link)
#         print(linkText)

#printing a div tag with a particular id:
navbarSupportedContent=soup.find(id="nav-content")
# .contents -> a tags children are available as a list
# .children -> a tags children are available as a generator
# print(navbarSupportedContent.contents)
# for elem in navbarSupportedContent.contents: // to print the children of the tag
#     print(elem)
# for elem in navbarSupportedContent.strings: # this would all the strings in the tag such as login, signup etc
#     print(elem)

# for elem in navbarSupportedContent.strings: # this would all the strings in the tag such as login, signup etc
#     print(elem)

# #Printing the parent tag:
# print(navbarSupportedContent.parent)
#Printing parent's name:
# print(navbarSupportedContent.parent.name) #ans was just div
# print(navbarSupportedContent.parents) #print all the parents and their content
# now printing all the names of parents:
# for elem in navbarSupportedContent.parents:
#     print(elem.name)
#print next sibling:
# print(navbarSupportedContent.next_sibling)
#print previous's previous or two  before sibling:
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# # printing tag with a specific id(#imgpreview2) or css class(.imgpreview):
# elem=soup.select('#imgpreview2')
# print(elem)


