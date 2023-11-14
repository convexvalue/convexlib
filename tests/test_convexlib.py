import unittest
from convexlib.api import ConvexApi

class TestConvexLib(unittest.TestCase):
    def setUp(self):
        # You can perform setup actions here, such as creating instances or setting up test data
        self.convex_instance = ConvexApi("sample", "sample","pro")

    def tearDown(self):
        # You can perform cleanup actions here, such as closing resources or resetting state
        pass

    def test_login(self):
        # Check if the login was successful
        self.assertIsNotNone(self.convex_instance.session.cookies.get("id"))

    # def test_make_request(self):
    #     # Assuming there's an endpoint that returns a specific response, modify this based on your API
    #     response_data = self.convex_instance.make_request("test_endpoint")
    #
    #     # Assert that the response data is what you expect
    #     self.assertEqual(response_data, {"key": "value"})

if __name__ == '__main__':
    unittest.main()
