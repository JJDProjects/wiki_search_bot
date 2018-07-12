'''
init.py
Setting up our Reddit API
'''
import praw

CLIENT = 'L8x-6g1eTzKv-g'
SECRET = 'J0inUb7XHpxfbc3Cd1eauU8j2GY'
BOT_NAME = 'TheQuestionAnswerBot'
BOT_PASSWORD = 'TheQuestionAnswerBot'
AGENT = 'created by Justin, Josh, David'

REDDIT = praw.Reddit(
					client_id = CLIENT, 
					client_secret = SECRET, 
					username = BOT_NAME, 
					password = BOT_PASSWORD, 
					user_agent = AGENT)




