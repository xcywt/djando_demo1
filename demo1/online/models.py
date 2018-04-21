from django.db import models
import json
import time

MESSAGE_FILE = 'messages.json'

# Create your models here.
def get_data():
	f = open(MESSAGE_FILE, 'rt')
	ctx = f.read()
	f.close()
	return json.loads(ctx)

def save_data(username, title, content):
	mesold = get_data()
	strtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
	mesnew = {'publish_date':strtime,'username':username,'title':title,'content':content}
	mesold.append(mesnew)
	f = open(MESSAGE_FILE, 'w')
	f.write(json.dumps(mesold))
	f.close()
	return True
