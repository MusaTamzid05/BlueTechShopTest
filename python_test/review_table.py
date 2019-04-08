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


