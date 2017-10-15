import requests
import bs4
course_number=20486
url = "https://www.microsoft.com/en-us/learning/course.aspx?cid={}".format(course_number)
print url
r =requests.get(url)
print ((r.status_code, r.encoding))

if(r.status_code == 200):
    s = bs4.BeautifulSoup(r.text,'html.parser')
    course_title = s.title.string
    print(course_title)
    c_info= s.find('dd',{'id':'course-info'})
    #print c_info
    c_overwiev =s.find('dd',{'id':'overview'})
    #print  c_overwiev.text
    c_syllabus =s.find('dd',{'id':'syllabus'})
    #print  c_syllabus
    mods = s.find_all('span',{'class':'DetailPagesContentLeadIn'})
    for m in mods:
        if m.text[:6] == 'Module':
            print m.text
        else:
            print "\t"+m.text
    print "\n course {}, consist of {} modules".format(course_title, len(mods)/2)
