import requests

def get_item_names_for_category(id: str) -> list[str]:
    result = requests.get("https://query.wikidata.org/bigdata/namespace/wdq/sparql", params={"query": f"""
        SELECT DISTINCT ?itemLabel WHERE {{
            SERVICE wikibase:label {{ bd:serviceParam wikibase:language "de". }}
        {{
            SELECT DISTINCT ?item WHERE {{
                ?item p:P31 ?statement0.
                ?statement0 (ps:P31/(wdt:P279*)) wd:{id}.
            }}
        }}
    }}""", "format": "json"}).json()
    # P31: instance
    # P279: subclass
    return [r["itemLabel"]["value"] for r in result["results"]["bindings"]]
