import requests
url = 'https://www.microsoft.com/en-us/learning/course.aspx?cid=20483'
r =requests.get(url)
print ((r.status_code, r.encoding))

if(r.status_code == 200):
    print(r.text)