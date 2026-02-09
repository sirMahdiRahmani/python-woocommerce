from base import *

terms = wcapi.get(f"products?filter[pa_team_name]=perspolis&filter[pa_age_group]=adults").json()

print(json.dumps(terms, indent=2))