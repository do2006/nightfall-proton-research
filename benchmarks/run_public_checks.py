from pathlib import Path
import json, sys

root = Path(__file__).resolve().parents[1]
claims = json.loads((root / "evidence" / "claims.json").read_text(encoding="utf-8"))
by_id = {x["id"]: x for x in claims["claims"]}
checks = [
    ("P17 scenarios", by_id["P17-SCENARIOS"]["windows"] == 120 and by_id["P17-SCENARIOS"]["wsl2"] == 120),
    ("P17 failure injection", by_id["P17-FAILURE-INJECTION"]["windows"] == 36 and by_id["P17-FAILURE-INJECTION"]["wsl2"] == 36),
    ("P17 property executions", by_id["P17-PROPERTY"]["windows"] == 10000 and by_id["P17-PROPERTY"]["wsl2"] == 10000),
    ("P17 fuzz/sanitizer", by_id["P17-FUZZ"]["wsl2_libfuzzer_runs"] == 10000 and by_id["P17-FUZZ"]["sanitizer_findings"] == 0),
    ("Proton recurrence", by_id["PROTON-RECURRENCE"]["count"] == 3),
    ("Proton proof classes", set(by_id["PROTON-VALIDATION"]["classes"]) == {"replay","historical","adversarial","canary"}),
    ("Proton recovery controls", by_id["PROTON-RECOVERY"]["rollback_required"] is True and by_id["PROTON-RECOVERY"]["quarantine"] == "block-activation"),
]
for name, ok in checks:
    print(("PASS" if ok else "FAIL") + ": " + name)
sys.exit(0 if all(ok for _, ok in checks) else 1)
