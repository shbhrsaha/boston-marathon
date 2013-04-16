
import urllib, sys, codecs
from bs4 import BeautifulSoup

START = 1
END = 27

for n in range(START,END):

    output = ""
    
    sys.stderr.write("Getting URL #" + str(n) + "\n")
    
    url = "http://boston-iframe.r.mikatiming.de/2013/?page="+str(n)+"&event=R&num_results=1000&pid=search&search[club]=%25&search[age_class]=%25&search[sex]=%25&search[nation]=%25&search[state]=%25&search_sort=name"
    
    f = urllib.urlopen(url)
    html = f.read()
    html = html.decode('utf8')

    soup = BeautifulSoup(html)

    tr_list = soup.find_all("tr")

    length = len(tr_list)

    for n in range(1, length):
        
        tr = tr_list[n]
        line = list()
        
        for td in tr.find_all('td'):
            line.append(td.get_text().strip())

        output += "\t".join(line) + "\t" + tr.find_all("a")[0].get('href') + "\n"

    f = codecs.open("runners.txt", "a", "utf-8")
    f.write(output)