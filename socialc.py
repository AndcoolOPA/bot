import numpy as np
import os
import file_manager

def SocialScore(id1, am, chat_id, chat_name):
	sc = file_manager.open("SocialScore", chat_id, 3, chat_name)

	finded = False
	for sc_c in range(len(sc)):
		if sc[sc_c][0] == id1:
			sc[sc_c][1] += am
			finded = True

	if finded == False: sc = np.append(sc, [[id1, 500 + am, 0]], axis = 0)
	
	file_manager.save("SocialScore", chat_id, sc, chat_name)

def SocialScore_set(id1, am, chat_id, chat_name):
	sc = file_manager.open("SocialScore", chat_id, 3, chat_name)

	finded = False
	for sc_c in range(len(sc)):
		if sc[sc_c][0] == id1:
			sc[sc_c][1] = am
			finded = True

	if finded == False: sc = np.append(sc, [[id1, am, 0]], axis = 0)
	
	file_manager.save("SocialScore", chat_id, sc, chat_name)




def show(id1, chat_id, chat_name):
	sc = file_manager.open("SocialScore", chat_id, 3, chat_name)

	sc_am = 0
	finded = False

	for sc_c in range(len(sc)):
		if sc[sc_c][0] == id1:
			finded = True
			sc_am = sc[sc_c][1]

	if finded == False: sc_am = 500

	return sc_am
