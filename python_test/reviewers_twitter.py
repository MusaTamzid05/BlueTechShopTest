from review_table import ReviewTable

def main():

    print("Showing all the users twitter handle.")

    for user in ReviewTable.get_unique_reviewers_twitter():
        print(user)


if __name__ == "__main__":
    main()
