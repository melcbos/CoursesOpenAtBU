# CoursesOpenAtBU
Find which courses are open with Python

## Local Setup ##
1. Install All Dependencies   
`pip3 install -r requirements.txt`
2. Create a [Pushbullet](https://www.pushbullet.com/) account and follow their instructions for setting up push notifications on the devices that you want to receive notifications.

3. Create your Pushbullet access token by going to your Pushbullet [account settings](https://www.pushbullet.com/#settings/account)
![Generating your Pushbullet access token](http://i.imgur.com/veHK8UI.png "Generating your Pushbullet access token")

4. Enter your access token into the pb_token configuration option in config.yml.

## To Do ##
5. Run the File  
`python3 courseSearch.py`
6. Wait to receive push notification through PushBullet
7. Once PushBullet arrives for any class, make sure to update course list and run file again because the program stops. 
