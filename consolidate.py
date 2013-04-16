
import urllib, sys, codecs
from bs4 import BeautifulSoup
import os, sys

matchFile = open("matches.txt","r")

count = 0
for line in matchFile.readlines():
    
    print count
    count += 1
    
    lineSplit = line.replace("\n","").split("\t")
    url = "http://boston-iframe.r.mikatiming.de/2013/"+lineSplit[-1]
    
    f = urllib.urlopen(url)
    html = f.read()
    html = html.decode('utf8')

    soup = BeautifulSoup(html)
    
    gender = soup.find_all("td", class_="f-age_class")[0].get_text().split(" ")[0].decode('utf8')
    age = soup.find_all("td", class_="f-age")[0].get_text().decode('utf8')
    state = soup.find_all("td", class_="f-state")[0].get_text().decode('utf8')

    output = "\t".join(lineSplit[:-1]).decode('utf8') + gender + "\t" + age + "\t" + state + "\n"
    f = codecs.open("consolidated.txt", "a", "utf-8")
    f.write(output)