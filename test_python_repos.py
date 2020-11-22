import unittest
import Ch16.python_repos


class Tests(unittest.TestCase):

    # The status code has returned as successful.
    def testReposStatusCode(self):
        self.assertEqual(Ch16.python_repos.r.status_code, 200)

    # The number of returned repositories is 30.
    def testRepositoriesReturned(self):
        self.assertEqual(30, len(Ch16.python_repos.repo_dicts))

    # The number of repositories are greater than a certain amount.
    def testTotalRepositories(self):
        self.assertGreater(Ch16.python_repos.response_dict['total_count'], 600000)

    # Repositories should have required keys.
    def testKeys(self):
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in Ch16.python_repos.repo_dict.keys())


if __name__ == '__main__':
    unittest.main()