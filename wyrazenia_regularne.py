import re
text = ["to sa rozne ciekawe teksty", "to jest inny tekst", "a ten juz nie jest znalezione" ]

for linia in text:
	znalazlem = re.search(r'tekst', linia)
	if (znalazlem) :
		print(linia)