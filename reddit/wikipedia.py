'''
wikipedia.py

All functions related to wikipedia:

Looking through comments and getting wikipedia URLs,
using the URL to access wikipedia and get the summary
of the article (first paragraph of the introduction)

'''

def get_urls(comment: str) -> [str]:
	'''Looks through a reddit comment and returns a
	list of wikipedia urls
	'''
	return [word for word in comment.split() if ('wikipedia.org' in word and word.startswith('http'))]









