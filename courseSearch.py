from pushbullet import Pushbullet
from datetime import datetime
from courseList import targets, term
import requests
import time
import yaml
url = 'https://www.bu.edu/phpbin/course-search/section/?'

#could improve by sorting with set of targets
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


    #test input in config file for token
    config = None

    with open('config.yml', 'r') as config_file:
        try:
            config = yaml.load(config_file)
        except yaml.YAMLError as err:
            print(err)
            exit(1)

    if config is None:
        print('Error with your config')
        exit(1)
    elif 'pb_token' not in config:
        print('Config must contain your Pushbullet Access Token!')
        exit(1)

    pb = Pushbullet(config['pb_token'])   


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

            pb.push_note(title, message)

            print(message)
            break;
        
        time.sleep(300)


if __name__== "__main__":
    main()

