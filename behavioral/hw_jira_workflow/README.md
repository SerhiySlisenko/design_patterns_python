# HomeWork task 'JIRA Workflow': State pattern using Python

This task roughly implements the workflow of the JIRA in the issue-tracking system.

* From the 'Opened' state it can be transferred to 'In Progress' or 'Resolved'
* From the 'In Progress'  state it can be transferred to 'Opened' or 'Resolved'
* From the 'Resolved'  state it can be transferred to 'Opened' or 'Verified' 
* From the 'Verified'  state it can be transferred to 'Opened' or 'Closed'
* From the 'Closed'  state it can be transferred to 'Opened'

Other state transitions are prohibited.
