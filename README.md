# NightFall Proton

### Public Research & Verification Release

**Persistent, governed cognition with evidence-gated capability promotion, quarantine, and rollback.**

[![Public Release](https://img.shields.io/badge/release-v1.0.0-111111)](https://github.com/do2006/nightfall-proton-research/releases/tag/v1.0.0)
[![Verification](https://github.com/do2006/nightfall-proton-research/actions/workflows/verify.yml/badge.svg)](https://github.com/do2006/nightfall-proton-research/actions/workflows/verify.yml)
[![NightFall Technologies](https://img.shields.io/badge/NightFall-Technologies-8b0000)](https://www.nightfalltechnologies.com/)

> **Public proof. Private implementation.**  
> This repository publishes falsifiable claims, evaluation methods, evidence summaries, and integrity checks for NightFall Proton while keeping the proprietary Proton/MCF/CSC engine private.

**NightFall Technologies** · https://www.nightfalltechnologies.com/  
**Current Proton milestone** · https://www.nightfalltechnologies.com/progress#nmmq-implementations  
**Stable release** · https://github.com/do2006/nightfall-proton-research/releases/tag/v1.0.0

---

## Research question

How can a persistent agent convert repeated experience into reusable capability while preserving **evidence traceability, bounded applicability, explicit authority, failure-closed drift handling, quarantine, and rollback?**

Proton's published lifecycle is:

```text
experience
   ↓
recurrence qualification
   ↓
bounded counterfactual analysis
   ↓
untrusted candidate
   ↓
replay + historical + adversarial + canary evidence
   ↓
explicit authorization
   ↓
transactional promotion
   ↓
bounded activation
   ↓
monitoring ──→ quarantine / rollback
```

## Evidence snapshot

| Property | Published result |
| --- | ---: |
| Phase 17 scenarios | **120 / platform** |
| Failure-injection cases | **36 / platform** |
| Property executions | **10,000 / platform** |
| Native WSL2 libFuzzer runs | **10,000** |
| Sanitizer findings | **0** |
| Recorded recurrence observations | **3** |
| Recorded proof classes | replay · historical · adversarial · canary |
| Recovery controls | rollback · quarantine |

These are **NightFall-produced research results**, published for scrutiny. They are not represented as independent third-party certification.

## Verify it

```bash
python verify.py
python benchmarks/run_public_checks.py
```

The first command checks the repository evidence files against `SHA256SUMS.txt`. The second validates the machine-readable public claims in `evidence/claims.json`.

## Research map

| Start here | Purpose |
| --- | --- |
| [Technical report](docs/TECHNICAL_REPORT.md) | Architecture, lifecycle, verification properties, and scope |
| [Claim → evidence matrix](evidence/CLAIM_MATRIX.md) | Maps each published claim to its evidence basis |
| [Evidence manifest](evidence/EVIDENCE_MANIFEST.md) | Compact public evidence record |
| [Machine-readable claims](evidence/claims.json) | Structured claims used by public checks |
| [Black-box evaluation spec](benchmarks/SPEC.md) | How an external evaluator can challenge the claims |
| [Demonstration protocol](demo/DEMONSTRATION_PROTOCOL.md) | Behavior-focused public demonstration sequence |
| [Independent evaluation request](docs/INDEPENDENT_EVALUATION.md) | What we want third parties to test |
| [Disclosure model](docs/DISCLOSURE_MODEL.md) | Exact public/private boundary |

## What is deliberately private

This is **not an open-source release of Proton**. The repository does not contain production Proton/MCF/CSC source, capability-generation and qualification internals, proprietary orchestration or algorithms, model artifacts, private databases, credentials, signing secrets, or infrastructure configuration.

The objective is **falsifiability without reconstruction**: enough information to challenge the published properties without providing a recipe for reproducing NightFall's proprietary system.

## Independent evaluation

Critical evaluation is welcome. We specifically want outside researchers and agent builders to test recurrence boundaries, candidate isolation, proof gating, scope enforcement, drift handling, quarantine, rollback, recovery, and whether the current evidence supports the claims being made.

See [Independent Evaluation](docs/INDEPENDENT_EVALUATION.md).

## Historical scope

The August 2026 Phase 17 CSC Research Alpha certification covered an owner-controlled local research pilot and did **not** authorize public release at that time. Later September 2026 Proton integration and promotion work produced the Proton-specific evidence summarized here. This repository preserves that chronology.

## About NightFall Technologies

NightFall Technologies is an independent technology R&D company developing systems across advanced computing, distributed cognition, security, communications, storage, and verifiable infrastructure.

**Website:** https://www.nightfalltechnologies.com/  
**Contact:** dwayneoneill@nightfalltechnologies.com

---

Copyright © 2026 NightFall Technologies. All rights reserved. Publication of these research materials does not grant a license to the proprietary Proton, MCF, CSC, or other NightFall implementations.
