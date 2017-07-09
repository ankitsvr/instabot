from constants import *
import requests
from get_user_id import get_user_id


def get_hash_tag(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print "user not exist"
        exit()
    url=BASE_URL+'users/%s/media/recent/?access_token=%s' %(user_id,APP_ACCESS_TOKEN)
    print "GET requested url :%s" %url
    req_media=requests.get(url).json()
    file=open("name.txt",'w')
    for posts in req_media['data']:
        file.write(posts['caption']['text'].encode('utf-8'))

    file.close()

wordcloud()



get_hash_tag("rahul_r2557")


