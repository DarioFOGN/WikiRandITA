from asyncio.windows_events import NULL
from os import link
import re
import requests

#script to get all the links! be carefull once started it will rewrite in the file so if stopped the file will miss a lot of links!

def converting():
    FirstLink = 'https://it.wikipedia.org/w/index.php?title=Speciale:TutteLePagine&from=%21'
    x = requests.get(FirstLink)
    contents = (str) (x.content)
    links = []
    for phrase in contents.split():
        if(re.match("href", phrase)):
            res = phrase.replace("href=\"", "").replace("\"", "")
            links.append(res)
    
    f = open("links.txt", "w")
    i = 0
    
    link = NULL
    for x in range(100000):
        for element in links:
            if  i>13 and i<359:
                f.write(element)
                f.write('\n')
            if  i == 358:
                element = element.replace("/wiki/", "")
                nextlink = element
            i += 1
        i = 0
        links.clear()
        oldlink = link 
        link = "https://it.wikipedia.org/w/index.php?title=Speciale:TutteLePagine&from=" + nextlink
        print(link)
        x = requests.get(link)
        contents = (str) (x.content)
        for phrase in contents.split():
            if(re.match("href", phrase)):
                res = phrase.replace("href=\"", "").replace("\"", "")
                links.append(res)
        if(i>1 and oldlink == link):
            break;
        
        print(x)
    f.close()


def main():
    print("hey there")
    converting();   
  
if __name__=="__main__":
    main()


