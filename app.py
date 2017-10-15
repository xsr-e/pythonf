import requests
import bs4
url = 'https://www.microsoft.com/en-us/learning/course.aspx?cid=20483'
r =requests.get(url)
print ((r.status_code, r.encoding))

if(r.status_code == 200):
    s = bs4.BeautifulSoup(r.text,'html.parser')
    course_title = s.title.string
    print(course_title)
    c_info= s.find('dd',{'id':'course-info'})
    print c_info
    c_overwiev =s.find('dd',{'id':'overview'})
    print  c_overwiev.text
    c_syllabus =s.find('dd',{'id':'syllabus'})
    print  c_syllabus
    mods = s.find_all('span',{'class':'DetailPagesContentLeadIn'})
    for m in mods:
        print m
