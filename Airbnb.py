import sys
import urllib
sys.path.append("mashape")

from mashape.http.http_client import HttpClient
from mashape.http.content_type import ContentType
from mashape.auth.mashape_auth import MashapeAuth
from mashape.auth.basic_auth import BasicAuth
from mashape.auth.query_auth import QueryAuth
from mashape.auth.custom_header_auth import CustomHeaderAuth
from mashape.auth.oauth_auth import OAuthAuth
from mashape.auth.oauth10a_auth import OAuth10aAuth
from mashape.auth.oauth2_auth import OAuth2Auth


class Airbnb:

    auth_handlers = []
    PUBLIC_DNS = "airbnb.p.mashape.com"

    def __init__(self, mashape_key):
        self.auth_handlers.append(MashapeAuth(mashape_key))

    def search(self, location, checkin=None, checkout=None, guests=None, page=None, mashape_callback=None):
        parameters = {
                "location": location,
                "checkin": checkin,
                "checkout": checkout,
                "guests": guests,
                "page": page}
        

        mashape_client = HttpClient()
        response = mashape_client.do_call(
                "GET",
                "https://" + self.PUBLIC_DNS + "/s",
                parameters,
                self.auth_handlers,
                ContentType.FORM,
                mashape_callback,
                True)
        return response


