# HPO Similarity Checker

## Overview

This repo contains a Python program that identifies patient JSON files with highly similar Human Phenotype Ontology (HPO) terms.

The program extracts HPO IDs from JSON files, compares the terms using the HPO graph, and prints the filenames that contain at least one pair of closely related terms.

---

## Repository organization

```text
project-name/
├── bin/
│   └── nodeFinder.py
├── examples/
│   ├── patient1.json
│   └── patient2.json
├── DOCUMENTATION.md
└── README.md
```
---

## Requirements

This program requires Python 3.

The program uses the following standard Python libraries:

```text
json
os
sys
itertools
functools
```

It also requires the following external Python packages:

```text
networkx
obonet
```

To install the required external packages, run:

```bash
pip install networkx obonet
```

---

## How to run

From the main project folder, run:

```bash
python bin/nodeFinder.py examples
```

This command runs `nodeFinder.py` on the JSON files inside the `examples/` folder.

---
## Similarity definition

In this program, two HPO terms are considered similar if their shortest-path distance in the HPO graph is 2 or less.

This cutoff is used to identify phenotype terms that may be closely related or potentially redundant.

---

## Notes

* The program reads the Human Phenotype Ontology from an online `.obo` file using `obonet`.
* The current program only prints the filenames that contain similar HPO terms.
* See `DOCUMENTATION.md` for a more detailed explanation of the program and its functions.
