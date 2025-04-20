# this stores all the property IDs used for classification in one place

# Wikidata property mappings for cultural enrichment
WIKIDATA_PROPERTIES = {
    "country_of_origin": "P495",
    "country": "P17",
    "located_in": "P131",
    "part_of_culture": "P2596",
    "instance_of": "P31",
    "heritage_status": "P1435",
}

# Set of cultural labels used in classification
CULTURAL_LABELS = [
    "Cultural Agnostic",
    "Cultural Representative",
    "Cultural Exclusive"
]

# Mapping for any post-processing (optional)
LABEL_NORMALIZATION = {
    "cultural agnostic": "Cultural Agnostic",
    "cultural representative": "Cultural Representative",
    "cultural exclusive": "Cultural Exclusive"
}

