import subprocess,sys,json,pathlib
r=subprocess.run([sys.executable,"worker/struct_mvp.py"],check=False)
assert r.returncode==0
x=json.loads(pathlib.Path("artifacts/struct_mvp.json").read_text())
assert x["passed"] is True
assert x["evidence_level"]=="E2"
