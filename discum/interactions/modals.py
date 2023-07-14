# New Additions to discum/interactions.py

import random, string
from ..RESTapiwrap import Wrapper

class Modals(object):
	__slots__ = ['discord', 's', 'log']
	def __init__(self, discord, s, log):
		self.discord = discord
		self.s = s
		self.log = log

	#click on a button or select menu option(s)
	def click(self, applicationID, channelID, guildID, nonce, data, sessionID):
		url = self.discord+"interactions"
		#nonce
		if nonce == "calculate":
			from ..utils.nonce import calculateNonce
			nonce = calculateNonce()
		else:
			nonce = str(nonce)
		#session id
		if sessionID == "random":
			sessionID = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
		body = {
			"type": 5,
			"nonce": nonce,
			"guild_id": guildID,
			"channel_id": channelID,
			"application_id": applicationID,
			"data": data,
			"session_id": sessionID
		}
		if guildID == None:
			body.pop("guild_id")
		print("modal body callout: " + str(body))
		return print(Wrapper.sendRequest(self.s, 'post', url, body, log=self.log))
