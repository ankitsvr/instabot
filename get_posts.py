from constants import *
import requests
def get_posts():
    url=BASE_URL+'users/self/media/recent/?access_token=%s' %(APP_ACCESS_TOKEN)
    print "GET request url %s " % url
    request_result=requests.get(url).json()

    if request_result['meta']['code']==200:
        if len(request_result['data']):
            return request_result['data'][0  ]

        else:
            print "data not recieved"

    else:
        print "user does not exist"

get_posts()
