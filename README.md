This is a tool for receiving reports from clockify.me

### Instructions:

1. Open your terminal and navigate to the directory you wish to store the project and run the following command:

```commandline
git clone https://github.com/margo-dubovik/clockify_daily_reporter.git
```

2. Open project in yout code editor.
3. create and activate a venv.
4. In terminal:

```commandline
pip install -r requirements.txt
```

5. I the root of the project create a file ``.env`` and define the variables: API_KEY, USER_ID, WORKSPACE_ID
6. To get the list of all time entries in Clockify, run the file ``all_entries.py``.
7. To get a summary report with time, spent on each task, grouped by date, run the file ``summary_report.py``

<i>If you want to save the report to file, uncomment the last 4 lines in ``summary_report.py``</i>