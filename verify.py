from pathlib import Path
import hashlib, sys

ROOT = Path(__file__).resolve().parent
manifest = ROOT / "SHA256SUMS.txt"
errors = []
for line in manifest.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    expected, rel = line.split("  ", 1)
    p = ROOT / Path(rel)
    if not p.is_file():
        errors.append(f"MISSING {rel}")
        continue
    actual = hashlib.sha256(p.read_bytes()).hexdigest()
    if actual != expected:
        errors.append(f"HASH_MISMATCH {rel}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("PASS: public release files match SHA256SUMS.txt")
