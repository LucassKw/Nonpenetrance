import json
import os
import sys
from itertools import combinations
from functools import lru_cache
import networkx as nx
import obonet


# Build an undirected HPO graph
graph = nx.Graph(obonet.read_obo("http://purl.obolibrary.org/obo/hp.obo"))

# Function to extract phenotype IDs
def pheno_ids(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    ids = []

    for feature in data.get("phenotypicFeatures", []):
        feature_type = feature.get("type", {})
        an_id = feature_type.get("id")
        if an_id in graph:
            ids.append(an_id)

    return ids


@lru_cache(maxsize=200_000)
def shortest_paths_from(source):
    return nx.single_source_shortest_path_length(graph, source)

# check distance
def sim_check(term_ids):
    pairs = list(combinations(term_ids, 2))

    sources = {term1 for term1, term2 in pairs}

    distmap = {
        source: shortest_paths_from(source)
        for source in sources
    }

    for term1, term2 in pairs:
        distance = distmap[term1].get(term2)

        if distance and distance <= 2:
            return True

    return False

# run whole folder
def run_folder(json_folder):
    json_files = [f for f in os.listdir(json_folder) if f.endswith(".json")]

    sim_term_files = []

    for json_name in json_files:
        json_path = os.path.join(json_folder, json_name)
        phenotype_ids = pheno_ids(json_path)

        if sim_check(phenotype_ids):
            sim_term_files.append(json_name)

    print(sim_term_files)


if len(sys.argv) > 1:
    run_folder(sys.argv[1])