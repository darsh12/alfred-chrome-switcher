#!/usr/bin/python

import json
import os.path

chrome_path = "~/Library/Application Support/Google/Chrome/Local State"
local_state_full_path = os.path.expanduser(chrome_path)

local_state_file = open(local_state_full_path, 'r')

local_state_json = json.load(local_state_file)['profile']['info_cache']

profiles = []
for profile_id in local_state_json:
    profile_name = local_state_json.get(profile_id)['name']
    # print(f"{profile_id}, {local_state_json.get(profile_id)['name']}")
    config_dict = {"uid": profile_id, "type": "default", "title": profile_name,
                   "subtitle": profile_name + " : " + profile_id,
                   "autocomplete": profile_id, "arg": profile_id}
    # Append each config_dict the the profiles list
    profiles.append(config_dict)

# Convert the profiles list to a json object
json_convert = json.dumps(profiles, sort_keys=True, indent=2)
# Append the items to the json object then print it
print('{{"items" :  {profile} }}'.format(profile=json_convert))
