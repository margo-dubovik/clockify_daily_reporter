import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
WORKSPACE_ID = os.getenv('WORKSPACE_ID')
USER_ID = os.getenv('USER_ID')

headers = {'x-api-key': API_KEY}

data = {
    "dateRangeStart": "2022-12-29T00:00:00.000",
    "dateRangeEnd": "2022-12-30T23:59:59.000",
    "summaryFilter": {
        "groups": [
            'DATE',
            'TIMEENTRY',
        ],
        'sortColumn': 'GROUP',
        "options": {
            "totals": "CALCULATE"
        },
    },
    "sortOrder": "ASCENDING",
    'amountShown': 'HIDE_AMOUNT',
    "exportType": "JSON",
}

url = f'https://reports.api.clockify.me/v1/workspaces/{WORKSPACE_ID}/reports/summary'
summary_report = requests.post(url, headers=headers, json=data).json()
summary_report_json = json.dumps(summary_report, indent=2, ensure_ascii=False)  # for pretty printing
print(summary_report_json)
