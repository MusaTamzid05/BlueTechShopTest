import unittest
from review_table import ReviewTable

class TestReviewTable(unittest.TestCase):

    UNIQUE_REVIWERS_COUNT = 15
    def test_unique_reviewers_twitter(self):
        self.assertEqual(ReviewTable.get_unique_reviewers_count() , TestReviewTable.UNIQUE_REVIWERS_COUNT)




if __name__ == "__main__":
    unittest.main()
