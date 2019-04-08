from twython import Twython
import os

class UserInfo:
    '''
    Has all the field of userinfo table except 'id'.
    '''

    def __init__(self , name , description , profile_image_url , followers_count):
        self.name = name
        self.description = description
        self.profile_image_url = profile_image_url
        self.followers_count = followers_count


class Twitter:

    def __init__(self):

        self.t = Twython(app_key = os.environ["APP_KEY"] ,
                         app_secret = os.environ["APP_SECRET"] ,
                         oauth_token = os.environ["OAUTH_TOKEN"],
                         oauth_token_secret = os.environ["OAUTH_TOKEN_SECRET"]
                         )

        def search(self , twitter_handle):

            try:

                users  = self.t.lookup_user(screen_name = [twitter_handle])

                if len(users) == 0:
                    return None


                user = users[0]
                return UserInfo(user["screen_name"] , user["description"] , user["profile_image_url"] , user["followers_count"])

            except  Exception: # TO-DO : find the proper exception !!
                return None

