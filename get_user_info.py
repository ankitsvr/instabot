#fuction for user information
from __future__ import print_function   #giv capability of print fuction used in 3.x python
import requests
from get_user_id import *
from constants import *
import sys
import time

#Fetch user info from instagram
def get_user_info(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print ('User does not exist!')
    exit()
  #url for instagram user
  request_url = BASE_URL + 'users/%s?access_token=%s' %(user_id, APP_ACCESS_TOKEN)
  print ('GET request url : %s' % (request_url))
  user_info = requests.get(request_url).json()

  #fetching meta data
  if user_info['meta']['code'] == 200:
      if len(user_info['data']):

          user='Username: %s' % (user_info['data']['username'])
          id='ID: %s' % (user_info['data']['id'])
          follower= 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
          following='No. of people you are following: %s' % (user_info['data']['counts']['follows'])
          no_of_post= 'No. of posts: %s' % (user_info['data']['counts']['media'])
          info_list=[user,id,follower,following,no_of_post]

          #loop for printing all info store in info list
          for x in range(len(info_list)):
              print(info_list[x],end=' ')
              time.sleep(1)

      else:
          print ('There is no data for this user!')
  else:
      print ('Status code other than 200 received!')

# take input from user as sys argument
if not len(sys.argv[1:]):
    print ("username must be suplied as argument")
else:
    get_user_info(sys.argv[1:])