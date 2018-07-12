'''
app.py

The script that runs this bot
'''

import praw
from reddit.config import REDDIT
from reddit import wikipedia

def wiki_testing():
	'''Practicing finding wikipedia links 
	in a string'''

	comment = 'steins gate is pretty cool https://en.wikipedia.org/wiki/Steins;Gate_(TV_series)'
	# prints a list containing any wikipedia links
	print(wikipedia.get_urls(comment))

def comment_testing():
	''' Practicing looking through reddit 
	comments. Currently need to be able to look through
	replies recursively. Look in agenda.txt for more details
	'''
	submissions = REDDIT.subreddit('all').hot(limit=1) # first 100 submissions in r/all
	comment_count = 0
	for submission in submissions:
		print('\n' + submission.title + '\n')
		for comment in submission.comments:
			print()
			if comment_count < 15:
				print(comment.body)
				comment_count += 1
			else:
				break

def main():
	comment_testing()
	print()
	wiki_testing()

if __name__ == '__main__':
	main()

