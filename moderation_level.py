import numpy as np
import os
import file_manager

def set_to_low(chat_id, chat_name):
	mod_lvl = file_manager.open("mod_lvl", 0, 1, chat_name)

	if not chat_id in mod_lvl:
		done = True
		mod_lvl = np.append(mod_lvl, [[chat_id]], axis = 0)

	else:
		done = False

	file_manager.save("mod_lvl", 0, mod_lvl, chat_name)
	return done

def is_in(chat_id, chat_name):
	mod_lvl = file_manager.open("mod_lvl", 0, 1, chat_name)

	return chat_id in mod_lvl

def set_to_hight(chat_id, chat_name):
	mod_lvl = file_manager.open("mod_lvl", 0, 1, chat_name)

	if chat_id in mod_lvl:
		done = True
		for sc_c in range(len(mod_lvl)):
			if mod_lvl[sc_c][0] == chat_id:
				mod_lvl[sc_c][0] = 0
				break

	else:
		done = False

	file_manager.save("mod_lvl", 0, mod_lvl, chat_name)
	return done