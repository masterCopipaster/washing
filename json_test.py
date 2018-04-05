import string, datetime
import json
#json_raw_str = "[{'uid': '12345', 'date_start': datetime.date(2017, 9, 3), 'time_start': datetime.time(16, 24, 15), 'time_end': datetime.time(23, 59, 00)}]"

json_raw_str = '[{"uid": "12345", "date_start": "2017-09-04", "time_start": "11:26", "time_end": "23:59"}]' 
#json_raw_str = '[{"uid": "12345", "date_start": "2017-09-04"}]'

json_str = string.replace(json_raw_str, "'", '"')

print json_str

def date_hook(json_dict):
	for (key, value) in json_dict.items():
		try:
			print key, value
			json_dict[key] = datetime.datetime.strptime(value, "%Y- %m- %d)")
		except:
			pass
		try:
			print key, value
			json_dict[key] = datetime.datetime.strptime(value, "%H:%M")
		except:
			pass
	return json_dict


data = json.loads(json_str, object_hook=date_hook)
print data
