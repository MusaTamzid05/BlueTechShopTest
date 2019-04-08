from review_table import ReviewTable

def main():

    for review_data in ReviewTable.get_users_with_review_more_equal_to(5):
        print("{} => {}".format(review_data[0] , review_data[1]))

if __name__ == "__main__":
    main()
