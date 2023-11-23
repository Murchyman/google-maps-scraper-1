from src.gmaps import Gmaps
star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/google-maps-scraper/'''

queries = ["hair salon in townsville"]
fields = [
   Gmaps.Fields.NAME, 
     Gmaps.Fields.IS_SPENDING_ON_ADS,
    Gmaps.Fields.WORKDAY_TIMING,
          Gmaps.Fields.CLOSED_ON,
   Gmaps.Fields.MAIN_CATEGORY, 
   Gmaps.Fields.RATING, 
   Gmaps.Fields.REVIEWS, 
   Gmaps.Fields.WEBSITE, 
   Gmaps.Fields.PHONE, 
   Gmaps.Fields.LINK, 
]
Gmaps.places(queries, fields=fields, max=100, has_website=False)