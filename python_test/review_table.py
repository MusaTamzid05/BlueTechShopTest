from database import Database

class ReviewTable:

    @staticmethod
    def insert(review):

        connection = Database.get_connection()

        if connection is None:
            return False

        cur = connection.cursor()
        try:
            cur.execute("INSERT INTO reviews (points, title  , description , taster_name , taster_twitter_handle , price , designation , variety , region_1 , region_2, province , country , winery) VALUES (%s, %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s)" , (review.points , review.title , review.description ,  review.taster_name , review.taster_twitter_handle , review.price , review.designation , review.variety , review.region_1 , review.region_2 , review.province , review.country ,review.winery))
            connection.commit()
        finally:

            cur.close()
            connection.close()

        return True

    @staticmethod
    def get_unique_reviewers_count():
        connection = Database.get_connection()

        if connection is None:
            return 0

        cur = connection.cursor()
        try:
            cur.execute("SELECT COUNT(DISTINCT taster_twitter_handle)  FROM reviews;" )
            return cur.fetchone()[0]
        except AttributeError as e:
            print(e)
            return 0
        finally:

            cur.close()
            connection.close()


    @staticmethod
    def get_users_with_review_more_equal_to(count):
        connection = Database.get_connection()

        if connection is None:
            return 0

        cur = connection.cursor()
        try:
            cur.execute("SELECT taster_twitter_handle, COUNT(*) from reviews GROUP BY taster_twitter_handle HAVING COUNT(*) >= %s;" ,(count , ) )
            return cur.fetchall()
        except AttributeError as e:
            print(e)
            return 0
        finally:

            cur.close()
            connection.close()


    @staticmethod
    def get_unique_reviewers_twitter():
        connection = Database.get_connection()

        if connection is None:
            return []
        cur = connection.cursor()
        try:
            cur.execute("SELECT DISTINCT taster_twitter_handle  FROM reviews;" )
            user_data = cur.fetchall()

            if len(user_data) == 0:
                return []

            twitter_handle = []

            for data in user_data:
                if data[0] is not None:
                    twitter_handle.append(data[0])

            return twitter_handle

        except AttributeError as e:
            print(e)
            return []
        finally:
            cur.close()
            connection.close()


