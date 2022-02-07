
import tornado.web
import requests
import SecretOperation 




class  IdentityCompanyName(tornado.web.RequestHandler):
    def get(self):
        SecretOperation.saveData(self.get_query_argument("scan_amount"),self.get_query_argument("increased_traffic"),self.get_query_argument("minimal_area"))
        raise Exception("No way home")
        self.write("Hello, world")

class  IdentityPerson(tornado.web.RequestHandler):
    def get(self):
        SecretOperation.saveData(self.get_query_argument("scan_amount"),self.get_query_argument("increased_traffic"),self.get_query_argument("minimal_area"))
        self.write("Hello, world")


# identity_person
# identity_person_address
# identity​_person​_name​_first
# name_categories
# trivia_search
# barcode_encode_types
# barcode_decode_types
# ​qrcode​_business_card
# qrcode_skype
# qrcode_sms
# qrcode_url
# qrcode​_raw

