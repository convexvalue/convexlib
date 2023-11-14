# convexlib


```
pip install git+https://github.com/convexvalue/convexlib.git
```

```py
from convexlib.api import ConvexApi

# use "pro" or "live"
convex_instance = ConvexApi("your_email", "your_password","pro")

# requesting underlyings
und_data = convex_instance.get_und(symbols=["SPX","AAPL"],params=["price","value"])
```
