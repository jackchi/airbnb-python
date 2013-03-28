# Airbnb Search API #

## Introduction ##

Original Code by John Matt ()
Updated by Jack Chi (fuching.chi@gmail.com)
This is the unofficial Airbnb API that lets you retrieve all the Airbnb listings! Filter by location, check-in date, number of guests and more.

Search Airbnb listings


Location <string>: Required	
Example: San Francisco, CA

Checkin <date> : Optional	
Example: 3/21/2013

Checkout <date> : Optional	
Example: 3/22/2013

Number of guests <string> : Optional	
Example: 2

Page to display, as displayed in Airbnb (defaults to 1)	<string> : Optional
Example: 1

Sample JSON:

{
  "results_count": "1 – 21 of 5293 listings",
  "total_pages": "48",
  "results": [
    {
      "unitThumb": "https://a2.muscache.com/pictures/10417846/x_small.jpg",
      "unitLink": "https://www.airbnb.com/rooms/748256",
      "unitName": "Valencia Corridor Parking Available",
      "ownerThumb": "https://a1.muscache.com/users/516404/profile_pic/1305688889/tiny.jpg",
      "ownerProfile": "https://www.airbnb.com/users/show/516404",
      "unitPrice": "$65 USD",
      "priceModifier": "Per night",
      "unitDesc": "Private room —     San Francisco          Mission District",
      "unitAddress": "San Francisco          Mission District",
      "unitReviews": "14"
    }
  ]
}

## Usage ##

### On Mac ###
```bash
cd airbnb-python-client
python Airbnb.py
```