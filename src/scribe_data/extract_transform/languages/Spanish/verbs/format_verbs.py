"""
Format Verbs
------------

Formats the verbs queried from Wikidata using query_verbs.sparql.
"""

import collections
import os
import sys

PATH_TO_SCRIBE_ORG = os.path.dirname(sys.path[0]).split("Scribe-Data")[0]
PATH_TO_SCRIBE_DATA_SRC = f"{PATH_TO_SCRIBE_ORG}Scribe-Data/src"
sys.path.insert(0, PATH_TO_SCRIBE_DATA_SRC)
from scribe_data.utils import export_formatted_data, load_queried_data

LANGUAGE = "Spanish"
QUERIED_DATA_TYPE = "verbs"

file_path = sys.argv[0]

verbs_list, update_data_in_use, data_path= load_queried_data(LANGUAGE, QUERIED_DATA_TYPE, file_path)

verbs_formatted = {}

all_conjugations = [
    "presFPS",
    "presSPS",
    "presTPS",
    "presFPP",
    "presSPP",
    "presTPP",
    "pretFPS",
    "pretSPS",
    "pretTPS",
    "pretFPP",
    "pretSPP",
    "pretTPP",
    "impFPS",
    "impSPS",
    "impTPS",
    "impFPP",
    "impSPP",
    "impTPP",
]

for verb_vals in verbs_list:
    if verb_vals["infinitive"] not in verbs_formatted:
        verbs_formatted[verb_vals["infinitive"]] = {}

        for conj in all_conjugations:
            if conj in verb_vals.keys():
                verbs_formatted[verb_vals["infinitive"]][conj] = verb_vals[conj]
            else:
                verbs_formatted[verb_vals["infinitive"]][conj] = ""

    else:
        for conj in all_conjugations:
            if conj in verb_vals.keys():
                verbs_formatted[verb_vals["infinitive"]][conj] = verb_vals[conj]

verbs_formatted = collections.OrderedDict(sorted(verbs_formatted.items()))

export_formatted_data(LANGUAGE, QUERIED_DATA_TYPE, verbs_formatted, update_data_in_use)
os.remove(data_path)
