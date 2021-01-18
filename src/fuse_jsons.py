from pathlib import Path
import os
import json

#Fuse all the json into one
def fuse_json(repertory_path):
	
	data_path = Path(repertory_path)
	reps = os.listdir(data_path)
	
	all_datas = {}
	json_list = []	
	
	for json_file in reps:
		datas = {}
		json_path = data_path / json_file
		
		if str(json_path).endswith(".json"):
			
			with open(json_path) as json_file:
				data = json.load(json_file)
				
			json_name = os.path.splitext(json_path)[0]
			print("Working on ", json_name, "...")
			datas["pdf"] = json_name
			datas["content"] = data
			json_list.append(datas)
			
			all_datas["data"] = json_list
	
	with open(r"data/out/all_data.json", "w", encoding="utf-8") as outfile:
		json.dump(all_datas, outfile)
						
fuse_json("data/out/")
