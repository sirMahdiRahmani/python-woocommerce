from woocommerce import API


wcapi = API(
    url="http://172.18.0.4",
    consumer_key="ck_78dccc986fdfa4b7e1c28a7f319d93699d4aeee5",
    consumer_secret="cs_5383d40226e6dd1cc7b9c0eb292e93d15936a85d",
    wp_api=True,
    version="wc/v3",
    query_string_auth=True # Force Basic Authentication as query string true and using under HTTPS
)

# data = {
#     "email": "john.doe@example.com",
#     "first_name": "John",
#     "last_name": "Doe",
#     "username": "john.doe",
#     "billing": {
#         "first_name": "John",
#         "last_name": "Doe",
#         "company": "",
#         "address_1": "969 Market",
#         "address_2": "",
#         "city": "San Francisco",
#         "state": "CA",
#         "postcode": "94103",
#         "country": "US",
#         "email": "john.doe@example.com",
#         "phone": "(555) 555-5555"
#     },
#     "shipping": {
#         "first_name": "John",
#         "last_name": "Doe",
#         "company": "",
#         "address_1": "969 Market",
#         "address_2": "",
#         "city": "San Francisco",
#         "state": "CA",
#         "postcode": "94103",
#         "country": "US"
#     }
# }

# print(wcapi.post("customers", data).json())
# print(wcapi.get("products").json())


data = data = {
    "name": "Color",
    "slug": "pa_color",
    "type": "select",
    "order_by": "menu_order",
    "has_archives": True
}


print(wcapi.post("products/attributes", data).json())
