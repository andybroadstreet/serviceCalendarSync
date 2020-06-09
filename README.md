program to read lightspeed workbenchschedule.csv and update to google calendar

#! /bin/bash
python csvReadAndFormat.py
python writeNextEventsToCSV.py
python compareCSvfiles.py


flow--->

	* obtain current work order schedule file frop lightspeed cloud
	* read file
	* update database of enteries not in database to workBenchSchedule.csv
	* info updated --> <ID>-<CUSTOMERNAME>
		       --> <DESCRIPTON><HOOKIN/HOOKOUT>
		       --> CURRENTDAY + <DAYSOVER> = DATE TO SCHEDULE
	* google calendar is checked for exisiting event
