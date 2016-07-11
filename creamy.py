
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
this is a reflex agent program to pretend nuison to talk to a poison user 
"""

import time
import random
import datetime

def main():
	# grab input
	print("You are now talking to nuison")
	start_talk_to_luison = time.time()
	# logic
	nuison_replies = ["haha", "wow", "okay", "oh reli?", "aiiii", "!!!"]
	while True:
		timenow = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		ask = raw_input("@"+timenow+ " You: ")

		if ask == '-1':
			print("You decided to give up being a 9gong. Good job!")
			break

		if ask:
			time_with_luison = int(time.time() - start_talk_to_luison)
			
			time_wait_for_nuison = random.randint(5,10)
			
			if time_with_luison > 120:
				time_wait_for_nuison = random.randint(1,time_with_luison)
				
			time.sleep(time_wait_for_nuison)

			choice = random.randint(0,len(nuison_replies))
			
			if choice == len(nuison_replies):
				if len(ask) > 10:
					reply = "what do you mean???"
				else:
					reply = str(ask) + "???"
			else:
				reply = nuison_replies[choice]
			timenow = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
			print("@"+timenow+ " Nuison: "+reply)

	# output

if __name__ == '__main__':
	start = time.time()
	main()
	elapsed = time.time() - start
	print("You have conversed with nuison for %s seconds") % (elapsed)

