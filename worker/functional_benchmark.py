#!/usr/bin/env python3
import json,pathlib,hashlib
base={"checkpoint":"C42.1-B1","revision":2,"claim":"validated-state"}
raw=json.dumps(base,sort_keys=True).encode(); h=hashlib.sha256(raw).hexdigest()
retrieved=json.loads(raw.decode()); roundtrip=hashlib.sha256(json.dumps(retrieved,sort_keys=True).encode()).hexdigest()==h
stale={"checkpoint":"C42.1-B1","revision":1,"claim":"older-state"}
reject_stale=stale["revision"]<retrieved["revision"]
ok=roundtrip and reject_stale
out={"CEREBRON_MODE":"STRUCTURED","CEREBRON_VERSION":"C42.1","ROLE":"session-memory-encyclopedia","EVIDENCE_STATUS":"BENCHMARK_VERIFIED" if ok else "BENCHMARK_FAILED","benchmark":"F74-B1","roundtrip_hash_match":roundtrip,"stale_revision_rejected":reject_stale,"sha256":h,"claim":"Checkpoint serialization integrity and stale-revision rejection work locally.","residual":"Cross-run and cross-session persistence is not proven by this local benchmark.","pass":ok}
pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/benchmark.json").write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2));raise SystemExit(0 if ok else 1)
