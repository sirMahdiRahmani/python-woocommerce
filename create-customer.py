from woocommerce import API
import json

wcapi = API(
    url="http://127.0.0.1:2323",
    consumer_key="ck_1c3bdeac877b437f9a0e676d535a3b6d2a403a24",
    consumer_secret="cs_686fde0ef54e7b377da66801189ba8553c46ecc2",
    wp_api=True,
    version="wc/v3",
    query_string_auth=True # Force Basic Authentication as query string true and using under HTTPS
)

TEAM_NAME_ATT_ID = 1
AGE_GROUP_ATT_ID = 2
LEAGUE_NAME_ATT_ID = 3

def get_products_by_attributes(team_term_id=None, age_term_id=None, league_term_id=None):
    params = {
        "per_page": 100
    }

    attributes = []
    index = 0

    if team_term_id:
        attributes.append({
            "attribute": "pa_team_name",
            "term_id": team_term_id
        })

    if age_term_id:
        attributes.append({
            "attribute": "pa_age_group",
            "term_id": age_term_id
        })

    if league_term_id:
        attributes.append({
            "attribute": "pa_league_name",
            "term_id": league_term_id
        })

    # Woo library expects nested params like attributes[0][attribute]
    for i, attr in enumerate(attributes):
        params[f"attributes[{i}][attribute]"] = attr["attribute"]
        params[f"attributes[{i}][term_id]"] = attr["term_id"]

    response = wcapi.get("products", params=params)

    if response.status_code != 200:
        print("Error:", response.text)
        return []

    return response.json()

def get_term_id_by_name(attribute_id, name):
    r = wcapi.get(f"products/attributes/{attribute_id}/terms", params={
        "search": name
    })
    terms = r.json()
    return terms[0]["id"] if terms else None

# print(json.dumps(wcapi.get("products?").json(), indent=2))
# print(json.dumps(wcapi.get("products/attributes/1/terms").json(), indent=2))
# print(get_term_id_by_name(TEAM_NAME_ATT_ID, "perspolis"))
t_id = get_term_id_by_name(TEAM_NAME_ATT_ID, "sepahan")
print(json.dumps(get_products_by_attributes(team_term_id=t_id), indent=2))
print(t_id)