import tweepy, time, sys, random, csv, calendar

players = []
returns2 = []
verbs = []
contracts = []
prospects = []

from keys import keys

CONSUMER_KEY = keys['CONSUMER_KEY']
CONSUMER_SECRET = keys['CONSUMER_SECRET']
ACCESS_KEY = keys['ACCESS_KEY']
ACCESS_SECRET = keys['ACCESS_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

running = True

with open('players.csv', 'r') as f:
	player = csv.reader(f, delimiter=',', quotechar='|')
	for row in player:
		players += [row]

with open('returns.csv', 'r') as x:
	returns = csv.reader(x, delimiter='|', quotechar='|')
	for row in returns:
		returns2 += row

with open('verbs.csv', 'r') as y:
	y2 = csv.reader(y, delimiter='|', quotechar='|')
	for row in y2:
		verbs += row

with open('contracts.csv', 'r') as z:
	z2 = csv.reader(z, delimiter='|', quotechar='|')
	for row in z2:
		contracts += row

with open('prospects.csv', 'r') as q:
	q2 = csv.reader(q, delimiter='|', quotechar='|')
	for row in q2:
		prospects += row

def randomplayer():
	return players[random.randint(0, len(players)-1)][0]

def randomreturn():
	return returns2[random.randint(0, len(returns2)-1)]

def randomteam():
	return players[random.randint(0, len(players)-1)][1]

def randomverb():
	return verbs[random.randint(0, len(verbs)-1)]

def randomcontract():
	return contracts[random.randint(0, len(contracts)-1)]

def randomprospect():
	return prospects[random.randint(0, len(prospects)-1)]

def template0():
	return "BREAKING: " + randomteam() + " traded " + pickathing() + " to " + randomteam() + " for " + pickathing2() + ". Details to follow."

def template1():
	return "BREAKING: " + randomplayer() + " won't " + randomverb() + " for " + pickathing3() + ". Details to follow."

def template2():
	return "BREAKING: " + pickathing4() + " has a strong interest in " + pickathing() + ". Details to follow."

def template3():
	return "BREAKING: " + randomplayer() + " has signed with " + randomteam() + " for " + pickasigning() + ". Details to follow."

def template4():
	return "BREAKING: Scouts say" + randomprospect + " has "

def template5():
	return

def template6():
	return

while running:

	player_return = [randomplayer, randomreturn]
	team_return = [randomreturn, randomteam]
	team_player = [randomplayer, randomteam]
	return_contracts = [randomreturn, randomcontract]
	tweet_templates = [template0, template1, template2, template3]

	pickathing = random.choice(player_return)
	pickathing2 = random.choice(player_return)
	pickathing3 = random.choice(team_return)
	pickathing4 = random.choice(team_player)
	pickasigning = random.choice(return_contracts)
	pickatemplate = random.choice(tweet_templates)

	tweet = pickatemplate() + " #TradeCentre"
	tweettime = random.randint(300, 600)

	if len(tweet) <= 139:
		api.update_status(tweet)
		print(str(tweettime/60) + " minutes until next exciting tweet")
		print(tweet)
		print(len(tweet))
		time.sleep(tweettime)