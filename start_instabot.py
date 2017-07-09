#start your bot and made the option for every avalaiblity in this file
from __future__ import print_function
from self_info import self_info
from get_user_info import get_user_info
from like_a_post import like_a_post
import get_users_post
import post_comment
import delete_neg_comnt

def init_bot():
    option_list = ['/n/n', '\t\t\t\t*************************Welcome to instabot*****************************',
                   '1.Get your own details', '2..Get details of user by username', '3..get your own recent post',
                   '4..get recent post of user by username ', '5..Like most recent user post',
                   '6..make comment on user recent post ', '7..Delete negative comment from recent post']

    for x in range(0,len(option_list)):
        print(option_list[x])
        select_option = raw_input("Enter your choice::")
        if select_option == 'A':
            self_info.self_info()

        elif select_option == 'B':
            insta_username = raw_input("Enter username: ")
            get_user_info.get_user_info(insta_username)

        elif select_option == 'C':
            get_own_post()

        elif select_option == 'D':
            insta_username = raw_input("Enter username::")
            get_users_post.get_user_post(insta_username)

        elif select_option == 'E':
            insta_username = raw_input("Enter username::")
            like_a_post.like_a_post(insta_username)

        elif select_option == 'F':
            insta_username = raw_input("Enter username::")
            post_comment.post_comment(insta_username)

        elif select_option == 'G':
            insta_username = raw_input("Enter Username::")
            delete_neg_comnt.del_neg_comment(insta_username)
    init_bot()


init_bot()


