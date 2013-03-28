# To use the Airbnb API in your code, just import the generated code
# add your developer key (you can find it in your dashboard: http://www.mashape.com/account/index )
# and relax!
# This is a sample of the initialization of the client.. then call its methods!


from Airbnb import Airbnb

# basic instantiation. @TODO Put your authentication keys here.
client = Airbnb("ffnGO1suGtJEjqgz4n7ykeuCbDP1hexv")

# A sample function call. These parameters are not properly filled in.
# See Airbnb.py to find all function names and parameters.
response = client.search("Accident, Maryland")

# now you can do something with the response.
print vars(response)
