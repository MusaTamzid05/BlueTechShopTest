

class Review:

    def __init__(self , review_dict):

        self.points = review_dict["points"]
        self.title = review_dict["title"]
        self.description = review_dict["description"]
        self.taster_name = review_dict["taster_name"]
        self.taster_twitter_handle = review_dict["taster_twitter_handle"]
        self.price  = review_dict["price"]
        self.designation = review_dict["designation"]
        self.variety = review_dict["variety"]
        self.region_1 = review_dict["region_1"]
        self.region_2 = review_dict["region_2"]
        self.province = review_dict["province"]
        self.country = review_dict["country"]
        self.winery = review_dict["winery"]

