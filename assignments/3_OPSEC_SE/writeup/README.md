# Writeup 3 - Operational Security and Social Engineering

Name: Adhithya Kannan
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Adhithya Kannan

## Assignment Writeup

### Part 1 (40 pts)

Under the assumption that Moffet is technologically inept without access to Google, we can pose as a trusted company to get information from her. Using Moffet's phone number, we can directly call Moffet to ask her about her information. We can use the pretext that we are Moffet's insurance company asking about a database error that occurred with her information. We can then ask her to fill out a form on the company website, which we have recreated but will not work. As she tries to log in, an error will be thrown with a special error code which will come with a special message to call and ask about the number. Since Moffet is already in the call, we can assume she will directly ask us about it. We can tell her that it is a browser error, and ask her what browser she is using, which answers one of the five questions we need to know. After, we can redirect her to a working website which will allow us to phish the other four questions. On the website, we simply ask her to recreate her login information with specific questions to fix the database error. If she says that she cannot answer any of the questions, ask her what a good followup question would be so it can be altered in the database. If she asks why we require her ATM pin number, we can say it was a previous question that she had answered and needed to be renewed to update and fix the database. The same follows for the first pet question. If she never had a pet, then we say it was the first pet she wished she had. If at any point, she decides to ask why again, we can say that we require a personal update on all confidential information so there are no external leaks with said information. 

### Part 2 (60 pts)

- The first method to securing Moffat's enterprise is setting up a firewall and securing the IP port 1337 since it is left unprotected. Leaving an unprotected port allows an adversary to send information to the server, which allows them to test the server by sending data packets. Closing her firewall off from unprotected ports, such as 1337, would prevent the adversary from sending data packets which would not allow them to receive information regarding the website without directly accessing it through a web browser. 
	-Source regarding solution: https://www.techradar.com/news/networking/how-to-secure-your-tcp-ip-ports-633089/3

- The second method to securing the Moffat bank corporation is creating a significantly stronger password. Her current password is linkinpark, which is purely lowercase letters, which can be hacked with enough time. In order to secure the password, adding uppercase letters, numbers, and other symbols make it much more difficult to crack the password. 
	--- A side note: In addition, maintaining numerous passwords and tracking them with a password manager is another way to keep multiple accounts safe.
	-Source regarding why and what to do: https://www.cnet.com/how-to/the-guide-to-password-security-and-why-you-should-care/
	-Source has 3 links to making better passwords which are useful in securing her activities

- The third method to securing the Moffat financial interests is differentiating the usernames from personal and professional life. Through a inteltechniques search, we found v0idcache in a few websites which we could trace back to 1337bank.money; however, if she had a different username for her social media and her corporate interests, we would never have been able to access the website's file system.   