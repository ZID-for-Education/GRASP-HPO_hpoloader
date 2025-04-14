from . import hpo_mods
from pkgutil import iter_modules
import json
import time

occam_schema = {}
occam_schema["hpo"] = {"label": "HPO Algorithms"}
occam_schema["iterations"] = {"label": "Iterations",
                              "type": "int",
                              "default": 100,
                              "description": "Number of iterations for hyperparameter optimization."}
for importer, modname, ispkg in iter_modules(hpo_mods.__path__):
    if modname != "__init__":
        occam_schema["hpo"][modname] = {"label": modname,
                                        "type": "boolean",
                                        "default": False,
                                        "description": f"Use {modname} for hyperparameter optimization."}

filename = 'occam_schema' + '.json'
with open(filename, 'w') as f:
    json.dump(occam_schema, f, indent=4)