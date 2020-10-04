Welcome to EECS Decal Session 4: Computer Security!

In this demo, you will be exploring a few examples of common web attacks
through a sample to-do list application.

First, we will observe the effects of Cross-site scripting in two forms:

	1. Stored XSS
	2. Reflected XSS

Then, we will show an example of SQL Injection which may result in some
interesting effects to your to-do list website. ;)


---- Setup: -----

Step 1:

  Locate the directory where you cloned the git repository to and navigate to
  the session 4 directory.


Step 2:

  Make sure you have the most up-to-date version of the repo by entering the
  command in the terminal window below in the same directory:

	git pull origin master


Step 3:

  Make sure you are locally hosting the website by entering the command below:

	python server.py

  If done successfully, should see output message in terminal. Copy this link
  to go to the website you're now hosting:

	http://localhost:1050


Step 4 (optional):

  Open up server.py and index.html in your favorite text editor to examine the
  code to try to see where the vulnerabilities are. Discuss with your neighbor
  possible fixes to these problems.

Note: If you want to reset the database at any point, run

    git reset --hard HEAD

-------- Setup Complete ---------

----- Demos: -----

Demo 1: Cross-Site-Scripting Vulnerabilities

  In the text field, copy/paste the following line and add item:

	<script>alert("Alert! This is an XSS vulnerability")</script>

  Now, reload the page and see what happens.


Demo 1.1: Relfected XSS Vulnerability:

  Copy/paste the URL below in and refresh to see effects:

	http://localhost:1050/?person=%3Cimg%20%20src=%22broken%20link%22%20onerror=%22alert(%27Triggered%27)%22/%3E


Demo 2: SQL Injection

  In the text field, copy/paste the following line:

	itemName'%3BDELETE FROM todos%3B--

  Add the item to the page. Refresh and examine behavior. Now try to delete the
  same text field. Do you notice something wrong? Talk with your neighbor about
  what happened and possible fixes to the problem.


Demo 3: Clickjacking (optional)

  Click the link close to the bottom of the page and see what happens. ;)
  You may need to try clicking a few times.

