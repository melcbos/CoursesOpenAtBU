from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
from pushbullet import Pushbullet
from courseList import targets, term
import requests
import pycurl
import time
url = 'https://www.bu.edu/phpbin/course-search/section/?'

#could improve by sorting with set of targets and use only response
def get_open_courses(request_links, targets, term):
    content = []
    for request in request_links:
        r = requests.get(request)
        content.append(r.json()['results'])

    courses_list_available = []
    for i in range(len(targets)):
        for key in content[i]:
            if key ==  term + targets[i]:
                print(key, content[i][key])
                if int(content[i][key]) > 0:
                    print('open')
                    courses_list_available.append(key + " is open")
    return courses_list_available
def main():
 
    request_links_list =[]
    for course in targets:
        print(course)
        temp = 'https://www.bu.edu/phpbin/summer/rpc/openseats.php?sections%5B%5D=' + term + course
        request_links_list.append(temp)
    
    courses_open = get_open_courses(request_links_list, targets, term)
    print(courses_open)

    
    pb = Pushbullet(config['pb_token'])

    last_open_courses = list()

    while True:
        print("Starting check... ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        courses_open = get_open_courses(request_links_list, targets, term)

        if len(courses_open) == 0:
            print("No new courses found!!!")
        else:

            title = "Open Class"
            message =""
            for item in courses_open:
                message += item + " "

            #pb.push_note(title, message)

            print(message)
            return;
        
        time.sleep(600)


if __name__== "__main__":
    main()

