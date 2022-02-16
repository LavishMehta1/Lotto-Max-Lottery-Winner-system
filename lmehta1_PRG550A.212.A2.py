#!/home/pi/software/bin/python3

#Programmer: Lavish Mehta, 160716189
#Course: PRG550 A

# import modules for CGI handling
import cgi, cgitb
import datetime
import urllib.request
import re

cgitb.enable()  # enabled for CGI script troubleshooting
                # script langauge/runtime errors are displayed and sent back to
                # the browser

# create instance of FieldStorage to process CGI form values
form = cgi.FieldStorage()

color = form.getvalue('ttype')
number1 = form.getvalue('number1')
number2 = form.getvalue('number2')
number3 = form.getvalue('number3')
number4 = form.getvalue('number4')
number5 = form.getvalue('number5')
number6 = form.getvalue('number6')

userInput = []

userInput.append(number1)
userInput.append(number2)
userInput.append(number3)
userInput.append(number4)
userInput.append(number5)
userInput.append(number6)


print("Content-type: text/html\n\n")

def datein(line, num):
    for dat in range(len(lines)):
        all = re.findall(r"[ADFJMNOS]\w* [\d]{1,2}, [\d]{4}", lines[dat])
        if (len(all) != 0):
            if(num == "count"):
                return dat
            sm = str(all)
            km = sm.strip("[]''")
            num = dat
            return(km)

def numbers(lines, index):
    Webnum = []
    for i in range(6):
        Webnum.append(re.findall(r'[<b>](\d|\d\d)[</b>]', lines[index]))
        index = index + 1
        res = str(Webnum[i])
        Webnum[i] = res.strip("[]''")
    return Webnum



for i in range(len(userInput)):
    for j in range(i+1, len(userInput)):
        if userInput[i] == userInput[j]:
            print("<html>")
            print("<head>")
            print("<title>Error</title>")
            print("</head>")
            print("<body bgcolor='%s'>" % color)
            print("<h1>Sorry, numbers selected must be UNIQUE</h1>\n")
            print("</body>")
            print("</html>")
            quit()


webPage = urllib.request.urlopen("http://www.lottolore.com/lotto649.html")
webPageText = webPage.read( )
webPageText = webPageText.decode("UTF-8")
lines = webPageText.split("\n")

num = "count"
WebDate = datein(lines, 0)
count = datein(lines, num)

winNum = numbers(lines, count+8)
winNum.sort()

times = 0
matchnum = []

for i in range(len(userInput)):
    for j in range(len(winNum)):
        if userInput[i] == winNum[j]:
            matchnum.append(userInput[i])
            times += 1
            times += 1

userInput = sorted([int(x) for x in userInput])
matchnum =  sorted([int(x) for x in matchnum])
if times>=3:
    print("<html>")
    print("<head>")
    print("<title>Lotto Max Results</title>")
    print("</head>")
    print("<body bgcolor='%s'>" % color)
    print("<pre>")
    print("Winning Numbers for " +WebDate+ ":")  
    for x in winNum:
        print( x, end=" ")
    
    print("\n\nUser Selected Numbers:")
    for x in userInput:    
        print( x, end=" ")

    print("\n\nMatched Numbers:")
    for x in matchnum:    
        print( x, end=" ")
    print("\n</pre>")
    print("</body>")
    print("</html>")

else:
    print("<html>")
    print("<head>")
    print("<title>No Win</title>")
    print("</head>")
    print("<body bgcolor='%s'>" % color)
    print("<h1>Sorry, NOT a WINNING TICKET... Please Play Again</h1>")
    print("</body>")
    print("</html>")
    quit()






