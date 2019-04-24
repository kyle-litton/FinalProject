from bs4 import BeautifulSoup
import urllib2


url = 'http://sis.rutgers.edu/soc/#subjects?semester=92019&campus=NB&level=U'

page = urllib2.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

print(soup)

