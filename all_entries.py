import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
WORKSPACE_ID = os.getenv('WORKSPACE_ID')
USER_ID = os.getenv('USER_ID')

headers = {'x-api-key': API_KEY}

url = f'https://api.clockify.me/api/v1/workspaces/{WORKSPACE_ID}/user/{USER_ID}/time-entries'
all_entries = requests.get(url, headers=headers).json()
all_entries_json = json.dumps(all_entries, indent=2, ensure_ascii=False)  # for pretty printing
print(all_entries_json)
