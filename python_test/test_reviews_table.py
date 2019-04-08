import unittest
from review_table import ReviewTable

class TestReviewTable(unittest.TestCase):

    UNIQUE_REVIWERS_COUNT = 15
    def test_unique_reviewers_twitter(self):
        self.assertEqual(ReviewTable.get_unique_reviewers_count() , TestReviewTable.UNIQUE_REVIWERS_COUNT)


    def test_unique_reviewers_more_than_five_review(self):
        reviewer_without_name = 1
        self.assertEqual(len(ReviewTable.get_users_with_review_more_equal_to(5)) , TestReviewTable.UNIQUE_REVIWERS_COUNT  + reviewer_without_name)




if __name__ == "__main__":
    unittest.main()
