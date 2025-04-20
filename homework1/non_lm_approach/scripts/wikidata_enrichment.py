# this connects to the Wikidata API, fetches each entity’s JSON, and extracts values for important cultural properties like instance_of, heritage_status, and part_of_culture

import requests

WIKIDATA_PROPERTIES = {
    "country_of_origin": "P495",
    "country": "P17",
    "located_in": "P131",
    "part_of_culture": "P2596",
    "instance_of": "P31",
    "heritage_status": "P1435",
}

def fetch_wikidata_entity(qid: str) -> dict | None:
    """Fetch raw JSON for a given Wikidata QID."""
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f" Error fetching QID {qid}: {e}")
        return None

def extract_cultural_properties(entity_json: dict, qid: str) -> dict:
    """Extract specified cultural properties from a Wikidata entity JSON."""
    result = {
        "qid": qid,
        "country_of_origin": [],
        "country": [],
        "located_in": [],
        "part_of_culture": [],
        "instance_of": [],
        "heritage_status": [],
    }

    try:
        claims = entity_json["entities"][qid]["claims"]
    except KeyError:
        print(f" QID {qid} missing expected structure.")
        return result

    for key, prop_id in WIKIDATA_PROPERTIES.items():
        if prop_id in claims:
            values = []
            for claim in claims[prop_id]:
                value = claim.get("mainsnak", {}).get("datavalue", {}).get("value")
                if isinstance(value, dict) and "id" in value:
                    values.append(value["id"])
                elif isinstance(value, str):
                    values.append(value)
            result[key] = values

    return result
