import requests
import re


r = requests.get('https://www.cyanidevf.fr/image-aleatoire/')
page = str(r.content)
#print(page)
#src="https://www.cyanidevf.fr/wp-content/uploads/2020/08/pote.png"
#mot="<a href=\"/comics/matt-all-the-more-reason-to-continue-drinking#comic"
#print(re.findall('<a href=\"(/comics/[a-z\-]+[a-z]+#comic)',page))

print(re.findall('src=\"https://www.cyanidevf.fr/wp-content/uploads/[a-z/]*[.]png',page))
