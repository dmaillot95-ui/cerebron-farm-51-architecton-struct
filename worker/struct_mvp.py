import json, math, pathlib
# Deterministic axial-bar benchmark: F=10000 N, A=0.001 m2, L=2 m, E=200 GPa
F=10000.0; A=0.001; L=2.0; E=200e9
stress=F/A
strain=stress/E
displacement=F*L/(A*E)
expected={"stress_pa":1.0e7,"strain":5.0e-5,"displacement_m":1.0e-4}
actual={"stress_pa":stress,"strain":strain,"displacement_m":displacement}
passed=all(math.isclose(actual[k],v,rel_tol=1e-12,abs_tol=1e-15) for k,v in expected.items())
out={"benchmark":"axial_bar_closed_form","engine":"PY-STRUCT-MVP","actual":actual,"expected":expected,"passed":passed,"evidence_level":"E2","limitations":["closed-form sanity benchmark","not finite-element analysis","not physical test"]}
pathlib.Path("artifacts").mkdir(exist_ok=True)
pathlib.Path("artifacts/struct_mvp.json").write_text(json.dumps(out,indent=2),encoding="utf-8")
print(json.dumps(out,indent=2))
raise SystemExit(0 if passed else 1)
