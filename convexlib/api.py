import requests

class ConvexApi:
    def __init__(self, email, password, kind = ''):
        # self.data_routes = "/api/v8/alloy"

        if kind == 'pro':
            self.base_url = f"https://pro.convexvalue.com"
        if kind == 'live':
            self.base_url = f"https://live.convexvalue.com"
        else:
            self.base_url = f"https://convexvalue.com"

        self.session = requests.Session()
        self.login(email, password)

    def login(self, email, password):
        login_url = f"{self.base_url}/api/v8/user/login"
        login_data = {"email": email, "password": password}

        response = self.session.post(login_url, json=login_data)

        if response.status_code == 200:
            print("Login successful")
        else:
            print(f"Login failed with status code: {response.status_code}")
            response.raise_for_status()

    def get_und(self,symbols,params):
        data = {"symbols":symbols,"params":params}
        return self.make_request(endpoint="/api/v8/alloy/core/data/und",method="POST",data=data)

    def make_request(self, endpoint, method="GET", data=None):
        url = f"{self.base_url}{endpoint}"

        if method == "GET":
            response = self.session.get(url)
        elif method == "POST":
            response = self.session.post(url, json=data)
        # Add more methods as needed

        response.raise_for_status()
        return response.json()  # Adjust based on the expected response format

# # Example usage:
# email = "email"
# password = "your_password"
#
# convex_instance = ConvexApi(email, password)
#
# # Now you can make requests using the instantiated object
# data = convex_instance.make_request("some_endpoint")
# print(data)
