#import libraries for natural language processing
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from get_post_id import *
from constants import *
import requests
#define a function for deleting the negative comment
def del_neg_comnt(insta_username):
    post_id=get_post_id(insta_username)
    req_url=BASE_URL+'media/%s/comments/?access_token=%s' %(post_id,APP_ACCESS_TOKEN)
    print "GET request URl %s" %req_url
    comnt_info=requests.get(req_url).json()
    #check whether server repond to the request or not
    if comnt_info['meta']['code']==200:
        if len(comnt_info['data']):
            #ananlyze comment with bayanalyzer to find out tha comment is negative or not
            for x in range(0,len(comnt_info['data'])):
                comnt_id=comnt_info['data'][x]['id']
                comnt_text=comnt_info['data'][x]['text']
                anlz=TextBlob(comnt_text, analyzer=NaiveBayesAnalyzer())
                if (anlz.sentiment.p_neg > anlz.sentiment.p_pos):
                    print "Negative comment %s: "%comnt_text
                    delete_url=BASE_URL+'media/%s/comments/%s/?access_token=%s' %(post_id,comnt_id,APP_ACCESS_TOKEN)
                    print "Delete request url:%s " %delete_url
                    delete_info=requests.delete(delete_url).json()

                    if delete_info['meta']['code']==200:
                        print 'comment delete successfully'

                    else:
                        print "unable to delete comment"

                else:
                    "positive comment %s\n" %comnt_text

        else:
            print 'ther is no comment in post'
    else:
        print 'status code other than 200'


del_neg_comnt(raw_input("enter username: "))