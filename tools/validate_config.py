import json, pathlib, sys
required=["config/farm_policy_v1.json","config/engine_registry.json","schemas/job.schema.json","schemas/artifact.schema.json","schemas/evidence.schema.json"]
for p in required:
    with open(p,encoding="utf-8") as f: json.load(f)
print("CONFIG_VALID", len(required))
