import requests
from constants import *

def self_info():
    request_url=BASE_URL +'users/self/?access_token=%s' %(APP_ACCESS_TOKEN)
    print 'GET request url :%s' %(request_url)
    user_info=requests.get(request_url).json()

    if user_info['meta']['code']==200:
        if len(user_info['data']):
            print "Username: %s" %user_info['data']['username']
            print "No of follower: %s" % (user_info['data']['count']['followed_by'])
            print "no of post :%s" %(user_info['data']['count']['media'])
        else:
            print "user does not exist"
    else:
        print "Not able to access user instagram info"


