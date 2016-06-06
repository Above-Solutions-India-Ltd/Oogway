

from pymongo import MongoClient
from datetime import datetime
import requests,json
import re



client_list = requests.get('http://52.9.185.212:4567/results/')
ptolist =[]

for i in client_list.json():
    ptolist.append(i['client'])

pi = list(set(ptolist))

for i in range(0,len(pi)) :
	print pi[i]
	r = requests.get('http://52.9.185.212:4567/results/'+pi[i]+'/check_mem')
	output_tok = json.loads(r.text)
	client_name = output_tok['client']
	checks_details = output_tok['check']
	checks_name = checks_details['name']
	checks_output = checks_details['output']
	checks_status = checks_details['status']
	#checks_metric = re.findall(r'([0-9.]+)',checks_output)
	client = MongoClient()
	db = client.mcollection

	#"metrics_output": {
	#   "Total":checks_metric[0],
	#   "User":checks_metric[1],
	#   "nice":checks_metric[2],
	#   "system":checks_metric[3],
	#   "idle":checks_metric[4],
	#   "iowait":checks_metric[5],
	 #  "irq":checks_metric[6],
	 #  "softirq":checks_metric[7],
	 #  "steal":checks_metric[8],
	 #  "guest":checks_metric[9]
	#},

	result = db.mcollection.insert_one(

	{
		"project": client_name,
		"mtype": checks_name,
		"matrix": checks_output,
	    "status":checks_status,
	    "mdatetime":datetime.isoformat(datetime.now())
    

	}

	)

	print(db)
	print(result.inserted_id)