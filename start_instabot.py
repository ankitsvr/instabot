#start your bot and made the option for every avalaiblity in this file
from __future__ import print_function
from self_info import self_info
from get_user_info import get_user_info
from like_a_post import like_a_post
from  get_users_post import get_user_post
from post_comment import post_comment
from delete_neg_comnt import del_neg_comment

def init_bot():
    option_list = ['\t\t\t\t*************************Welcome to instabot*****************************',
                   'A.Get your own details', 'B..Get details of user by username', 'C..get your own recent post',
                   'D..get recent post of user by username ', 'E..Like most recent user post',
                   'F..make comment on user recent post ', 'G..Delete negative comment from recent post']

    for x in range(0,len(option_list)):
        print(option_list[x],end='\n\n')
    select_option = raw_input("Enter your choice::")
    if select_option == 'A':
        self_info()

    elif select_option == 'B':
        insta_username = raw_input("Enter username: ")
        get_user_info(insta_username)

    elif select_option == 'C':
        get_own_post()

    elif select_option == 'D':
        insta_username = raw_input("Enter username::")
        get_user_post(insta_username)

    elif select_option == 'E':
        insta_username = raw_input("Enter username::")
        like_a_post(insta_username)

    elif select_option == 'F':
        insta_username = raw_input("Enter username::")
        post_comment(insta_username)

    elif select_option == 'G':
        insta_username = raw_input("Enter Username::")
        del_neg_comment(insta_username)


init_bot()


