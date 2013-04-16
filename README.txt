These scripts enable users to rapidly search for names in the 2013 Boston Marathon list. Read more at http://www.princeton.edu/~saha/

USAGE
=====
everyone.csv should be a spreadsheet of individuals in your community. names.py might would probably need to be tweaked to accomodate your spreadsheet format. consolidated.txt will contain the marathon results line with the last three columns containing gender, age, and state, respectively.

    python scraper.py
    python names.py everyone.csv > names.txt
    python grep.py > matches.txt
    python consolidate.py