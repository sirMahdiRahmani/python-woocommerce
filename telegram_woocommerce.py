from woocommerce import API
import json


class TeamName():
    perspolis = "perspolis"
    esteghlal = "esteghlal"
    sepahan = "sepahan"
    tractor = "tractor"


class LeagueName():
    premiere_league = "premiere-league"
    league1 = "league1"


class AgeGroups():
    adults = "adults"
    u21 = "u21"
    u18 = "u18"


class TelegramWoocommerce():
    def __init__(self):
        self.url = "http://127.0.0.1:2323"
        self.customer_key = "ck_1c3bdeac877b437f9a0e676d535a3b6d2a403a24"
        self.customer_secret = "cs_686fde0ef54e7b377da66801189ba8553c46ecc2"
        self.team_name = ""
        self.league_name = ""
        self.age_group = ""
        self.customer_id = 0


        self.wpapi = API(
            url=self.url,
            consumer_key=self.customer_key,
            consumer_secret=self.customer_secret,
            wp_api=True,
            version="wc/v3",
            query_string_auth=True # Force Basic Authentication as query string true and using under HTTPS
        )

        self.wcapi = API(
            url=self.url,
            consumer_key=self.customer_key,
            consumer_secret=self.customer_secret,
            wp_api=False,
            version="v3",
            query_string_auth=True # Force Basic Authentication as query string true and using under HTTPS
        )

    def get_filtered_product(self, teamName = "", leagueName = "", ageGroup = ""):

        filter_url = "products?"

        if teamName != "":
            self.team_name = teamName
            filter_url += f"&filter[pa_team_name]={teamName}"

        if leagueName != "":
            self.league_name = leagueName
            filter_url += f"&filter[pa_league_name]={leagueName}"

        if ageGroup != "":
            self.age_group = ageGroup
            filter_url += f"&filter[pa_age_group]={ageGroup}"

        result = self.wcapi.get(filter_url).json()

        return result["products"]
        
    def get_customer(self, username):
        result = self.wpapi.get("customers", params={"email": f"{username}@smart-football.ir"}).json()
        if len(result) == 0:
            return []
        return result[0]
    
    def create_customer(self, username, firstname="", lastname=""):

        data = {
            "email": f"{username}@smart-football.ir",
            "first_name": f"{firstname}",
            "last_name": f"{lastname}",
            "username": f"{username}",
            "billing": {
                "first_name": f"{firstname}",
                "last_name": f"{lastname}",
                "company": "",
                "address_1": "Tehran",
                "address_2": "",
                "city": "Tehran",
                "state": "CA",
                "postcode": "",
                "country": "Tehran",
                "email": f"{username}@smart-football.ir",
                "phone": "(555) 555-5555"
            }
        }

        return self.wpapi.post(f"customers", data).json()

    def create_order(self, customer_id, products_id):
        list_of_products = []
        for p in products_id:
            list_of_products.append(
                {
                    "product_id": p,
                    "quantity": 1
                }
            )
        
        data = {
            "payment_method": "bacs",
            "payment_method_title": "Direct Bank Transfer",
            "set_paid": False,
            "customer_id": 4,
            "billing": {
                "first_name": "John",
                "last_name": "Doe",
                "address_1": "969 Market",
                "address_2": "",
                "city": "San Francisco",
                "state": "CA",
                "postcode": "94103",
                "country": "US",
                "email": "john.doe@example.com",
                "phone": "(555) 555-5555"
            },
            "line_items": list_of_products
        }
        
        return self.wpapi.post("orders", data).json()

    def delete_order(self, order_id):
        return self.wpapi.delete(f"orders/{order_id}", params={"force": True}).json()
    
# tw = TelegramWoocommerce()
# print(json.dumps(tw.create_order(4, [12]), indent=2)) 