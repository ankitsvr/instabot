import requests
from constants import *
from get_post_id import *
def like_a_post(insta_username):
    post_id=get_post_id(insta_username)
    req_url=BASE_URL+'media/%s/likes' % post_id
    payload='access_token' %APP_ACCESS_TOKEN
    print 'GET request url %s' %req_url
    like_post=requests.get(req_url,payload).json()

    if like_post['meta']['code']==200:
        print " successfully liked"

    else:
        print "like not completed"


