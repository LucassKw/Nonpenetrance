# Documentation

## Program purpose

This program checks JSON files for highly similar Human Phenotype Ontology (HPO) terms.

It reads each `.json` file in a folder, extracts the HPO IDs from the `phenotypicFeatures` section, and compares every pair of HPO terms within each file. If any two HPO terms are within a shortest-path distance of 2 or less in the HPO graph, the file is flagged as containing similar phenotype terms.

The final output is a printed Python list of JSON filenames that contain at least one pair of similar HPO terms.

---

## Input

The program takes one command-line argument:

```bash
python nodeFinder.py path/to/json_folder