from review_table import ReviewTable

def main():
    print("Total unique user reviews {}".format(ReviewTable.get_unique_reviewers_count()))


if __name__ == "__main__":
    main()
