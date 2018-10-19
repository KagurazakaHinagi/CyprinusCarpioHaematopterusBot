file = 'user.config'
# KOI_PHOTO = 
# SALTED_PHOTO = 

class Analysis():

	def __init__(self, msg, content_type, chat_type, chat_id, admin, bot):

		if (chat_type == 'private' and chat_id == admin):
			if msg['text'] == '/starthack':
				hack.Control(1)
				bot.sendMessage(admin, "Hack started.")
				with open(file) as Vfile:
					for user in Vfile.readlines():
						bot.sendMessage(user, "Ready for hack. ")
			elif msg['text'] == '/stophack':
				hack.Control(0)
				bot.sendMessage(admin, "Hack Stopped.")

		if (chat_type == 'private' and content_type == 'text'):
			if msg['text'] == '/start':
				if(msg['from'].has_key('username') == 0):
					bot.sendMessage("Please set your Telegram Username first and then send /start again to continue. ")
				else:
					username = msg['from']['username']
					bot.sendMessage(chat_id, "Welcome! ")
					bot.sendMessage(chat_id, "Verified as @" + msg['from']['username'])
					bot.sendMessage(admin, msg['from']['username'] + " has joined. ")
					with open(file, 'a') as Vfile:
						Vfile.write(chat_id + '\n' )
			elif(msg['text'] == '/hack'):
				status = hack.Hack()
				if status == 1:
					hack.Control(0)
					# bot.sendPhoto(chat_id, KOI_PHOTO)
					bot.sendMessage(chat_id, "Congratulations! ")
					bot.sendMessage(admin, "The Koi is @" + username)
				elif status == 0:
					# bot.sendPhoto(chat_id, SALTED_PHOTO)
					bot.sendMessage(chat_id, "Better luck next time! ")
				elif status == -1:
					bot.sendMessage(chat_id, "Koi running hot. Wait for 5 secs. ")
				elif status == -2:
					bot.sendMessage(chat_id, "Koi burned out. It may take some time to reset. ")
