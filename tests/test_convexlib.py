import unittest
from convexlib.api import ConvexApi
import os
from dotenv import load_dotenv
load_dotenv()

class TestConvexLib(unittest.TestCase):
    def setUp(self):
        email = os.getenv('EMAIL')
        password = os.getenv('PASSWORD')
        # You can perform setup actions here, such as creating instances or setting up test data
        self.convex_instance = ConvexApi(email, password,"pro")

    def tearDown(self):
        # You can perform cleanup actions here, such as closing resources or resetting state
        pass

    def test_login(self):
        # Check if the login was successful
        self.assertIsNotNone(self.convex_instance.session.cookies.get("id"))

    def test_get_und(self):
        # Assuming there's an endpoint that returns a specific response, modify this based on your API
        response_data = self.convex_instance.get_und(symbols=["SPX","AAPL"],params=["price","value"])
        print(response_data)
        # Assert that the response data is what you expect
        # self.assertEqual(response_data, {"key": "value"})

    def test_get_chain(self):
        # get_chain(self,root,params,exps = undefined, rng = undefined):
        response_data = self.convex_instance.get_chain("AAPL",params=["volm_bs","volatility"],exps=[1,2,3],rng=0.10)
        print(response_data)

    def test_get_chain_as_rows(self):
        # get_chain(self,root,params,exps = undefined, rng = undefined):
        response_data = self.convex_instance.get_chain_as_rows("AAPL",params=["volm_bs","volatility"],exps=[2,3],rng=0.3)
        print(response_data)

if __name__ == '__main__':
    unittest.main()
