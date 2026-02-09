from woocommerce import API
import json


TEAM_NAME_ATT_ID = 1
AGE_GROUP_ATT_ID = 2
LEAGUE_NAME_ATT_ID = 3

wpapi = API(
    url="http://127.0.0.1:2323",
    consumer_key="ck_1c3bdeac877b437f9a0e676d535a3b6d2a403a24",
    consumer_secret="cs_686fde0ef54e7b377da66801189ba8553c46ecc2",
    wp_api=True,
    version="wc/v3",
    query_string_auth=True # Force Basic Authentication as query string true and using under HTTPS
)

wcapi = API(
    url="http://127.0.0.1:2323",
    consumer_key="ck_1c3bdeac877b437f9a0e676d535a3b6d2a403a24",
    consumer_secret="cs_686fde0ef54e7b377da66801189ba8553c46ecc2",
    wp_api=False,
    version="v3",
    query_string_auth=True # Force Basic Authentication as query string true and using under HTTPS
)
