import praw
from init import REDDIT


def main():
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



if __name__ == '__main__':
	main()

