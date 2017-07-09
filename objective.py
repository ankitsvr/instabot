from constants import *
import requests
from get_user_id import get_user_id
import re
import urllib

def get_user_post(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print "user not exist"
        exit()
    url=BASE_URL+'users/%s/media/recent/?access_token=%s' %(user_id,APP_ACCESS_TOKEN)
    print "GET requested url :%s" %url
    req_media=requests.get(url).json()
    # print req_media
    search ="#instapic"
    for posts in req_media['data']:
        print posts['caption']['text']
            # print "%s found in post with id %s" % (search,posts['id'])
get_user_post("rahul_r2557")