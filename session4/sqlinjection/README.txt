Welcome to EECS Decal Session 4: Computer Security!

In this demo, you will be exploring a few examples of common web attacks.
First, we will observe the effects of Cross-site scripting in two forms:
	1. Stored XSS 
	2. Reflected XSS
Then, we will show an example of SQL Injection which may result in some interesting effects to your server. ;)

1. Stored XSS:
	This attack is generally caused by an attacker storing malicious javascript on a server in place of text-input data.

Setup:

Step 1: Locate the directory where you cloned the git repository to and navigate to the sqlinjection folder inside the session4 directory.

Step 2: Make sure you have the most up-to-date version of the repo by entering the command in the terminal window below in the same directory:
	
	git pull origin master

Step 3: Make sure you are locally hosting the website by entering the command below:
	
	python server.py

	If done successfully, you should see a message being displayed with the link to use to access your website. Copy/paste this link from the terminal window into the URL on a new tab in your browser and reload. The website should now be displayed.

Step 4 (optional): Open up server.py in SublimeText to examine code and see where vulnerability is. Discuss with your neighbor possible fixes to this problem.
	

Demo 1: Cross-Site-Scripting Vulnerabilities
	In the text field, copy/paste the following line and add item:

	<script>alert("Alert! This is an XSS vulnerability")</script>

	Now, reload page and see what happens.



Demo 2: SQL Injection
	In the text field, copy/paste the following line:
	
	itemName'%3BDROP TABLE todos%3B--

	Add the item to the page. Refresh and examine behavior. Now try to delete the same text field, and then refresh and examine behavior. Do you notice something wrong? Talk with your neighbor about what happened and possible fixes to problem.

Demo 3: Clickjacking
	Click the link at the bottom of the page and see what happens. ;)

