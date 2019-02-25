# Writeup 2 - OSINT

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (45 pts)

1. v0idcache's real name is Elizabeth Moffet
2. She works in the cybersecurity and finance fields in a company called 1337bank.money. The URL to their website is 1337bank.money. 
3. Moffet has a twitter account with the username v0idcache and a secret online lover whos twitter handle is Dev0id_cache. There is also a reddit account with a flag by the name of v0idcache, but this is probably a fake account. Moffet is also from the netherlands. All social media information was found through www.social-searcher.com. 
4. 142.93.126.81 is the only associated ip address with 1337bank.money. This can be found using nmap on the URL for the website. The server is hosted in the Amsterdam, Netherlands under the company, Digital Ocean, using the website dnstrails.com. There was no additional history within the DNS search. 
5. Using robots.txt, the directory /secret_directory was found which gave a flag. The second flag was found in the html/css of the page. 
        Flag 1: CMSC389R-{h1ding_fil3s_in_r0bots_L0L}
        Flag 2: CMSC389R-{h1dd3n_1n_plain_5ight}
6. There are 3 ports that are open: 22, 80, and 1337. 22 and 1337 are ssh, and 80 is http. nmap revealed the services behind each port. 
7. The server is running on the operating system of Ubuntu Linux. I found this using nmap -sV 1337bank.money.
8. CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}
    


### Part 2 (75 pts)

Using pre-existing code, I filled in the host with the IP address found in part1 as well as the port. Using kali-linux to using the rockyou.txt file I ran the method brute_force(). In bruteforce, I assigned a username: v0idcache and ended it with a newline. Then I opened the file, wordlist, and began to loop through it. I opened a socket for each line, then connected to the host and port. I received any data (which was username) and then send the data it asked for. So in order of requests, I sent the username then password. I then ran one final receive for this specific request to get whether or not it failed. If it did not fail, I ended the loop and return the password that was accepted.

