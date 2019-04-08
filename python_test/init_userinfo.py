from review_table import ReviewTable
from user_info_table import UserInfoTable

'''
The code has not been tested.Their was problem getting the twitter api key.
At the time i tried(8th April 2019) , if you create a app with twitter , twitter will review it and
mail you after review is complete.At time i was coding this,i did not get any reply.
'''
def main():

    twitter_api = Twitter()

    for twitter_handle in ReviewTable.get_unique_reviewers_twitter():
        user_info = twitter_handle.search(twitter_handle)

        if user_info is None:
            continue

        UserInfoTable.insert(user_info_table)




if __name__ == "__main__":
    main()



