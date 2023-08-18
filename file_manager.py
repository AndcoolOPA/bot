import numpy as np
import os
def init():
	if not os.path.exists("data"): os.mkdir("data")

def open(name, chat_id, am, chat_name):
	if not os.path.exists(f"data/{chat_id}"): os.mkdir(f"data/{chat_id}")
	return np.zeros(am).reshape(1, am) if not os.path.exists(f"data/{chat_id}/{name}{chat_id}.npy") else np.load(f"data/{chat_id}/{name}{chat_id}.npy", allow_pickle=True)


def save(name, chat_id, list, chat_name):
	if not os.path.exists(f"data/{chat_id}"): os.mkdir(f"data/{chat_id}")
	np.save(f"data/{chat_id}/{name}{chat_id}.npy", list)