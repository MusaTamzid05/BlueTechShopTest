

class UserInfoTable:

    @staticmethod
    def insert(user_info):

        connection = Database.get_connection()

        if connection is None:
            return False

        cur = connection.cursor()
        try:
            cur.execute("INSERT INTO userinfo (name , description , profile_image_url , followers_count) VALUES (%s , %s , %s , %s)" , (user_info.name , user_info.description , user_info.profile_image_url , user_info.followers_count))
            connection.commit()
        finally:

            cur.close()
            connection.close()

        return True
