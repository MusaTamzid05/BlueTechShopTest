import json
from review import Review
from review_table import ReviewTable

def main():
    with open("data.json" , "r") as f:
        data = json.load(f)

        for review_data in data:
            ReviewTable.insert(Review(review_data))

        print("data added")





if __name__ == "__main__":
    main()

