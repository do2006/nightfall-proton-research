# NightFall Proton — Public Research Release 1.0

**Evidence for persistent, governed cognitive learning — without publishing the proprietary engine.**

NightFall Proton is a NightFall Technologies research system integrating durable cognitive state with the NightFall Mimetic Cognitive Fabric (MCF) and CSC learning path. This repository lets researchers, developers, partners, and customers inspect published claims, evaluation boundaries, and verification artifacts without receiving the production implementation.

**Company:** NightFall Technologies  
**Canonical website:** https://www.nightfalltechnologies.com/  
**Proton progress record:** https://www.nightfalltechnologies.com/progress#nmmq-implementations

## What is being demonstrated

The public evidence covers recurring-experience qualification, bounded candidate capabilities, counterfactual analysis, multiple proof classes, company/owner-authorized transactional promotion, bounded activation, drift quarantine, rollback/recovery controls, and cross-platform validation.

The central lifecycle is: experience → recurrence → bounded counterfactual analysis → candidate → proof → authorization → transactional promotion → activation → monitoring → quarantine / rollback.

## Start here

1. Read `docs/TECHNICAL_REPORT.md`.
2. Inspect `evidence/EVIDENCE_MANIFEST.md` and `evidence/claims.json`.
3. Run `python verify.py` to verify repository artifact hashes.
4. Run `python benchmarks/run_public_checks.py` to evaluate the machine-readable public claims.
5. Read `benchmarks/SPEC.md` and `demo/DEMONSTRATION_PROTOCOL.md` for the external evaluation design.

## Published evidence snapshot

| Property | Published result |
| --- | --- |
| Phase 17 scenarios | 120 passed per platform |
| Failure-injection cases | 36 passed per platform |
| Property executions | 10,000 per platform |
| Native WSL2 libFuzzer runs | 10,000 |
| Sanitizer findings | 0 |
| Proton recurrence threshold demonstrated | 3 observations |
| Proton proof classes recorded | replay, historical, adversarial, canary |
| Recovery controls | rollback + quarantine |

These are NightFall-produced research results. They are published for scrutiny and reproduction; they are not represented as independent third-party certification.

## What is intentionally not here

This is **not** an open-source release of Proton. Production Proton/MCF/CSC source, crystal-generation and qualification internals, proprietary algorithms and orchestration, model artifacts, private databases, credentials, private signing material, infrastructure details, and unrelated NightFall intellectual property remain private.

See `docs/DISCLOSURE_MODEL.md` for the disclosure boundary.

## Historical integrity

The August 2026 Phase 17 CSC Research Alpha certification covered an owner-controlled local research pilot and explicitly did not authorize public release at that time. Later September 2026 Proton integration and promotion work produced the Proton-specific evidence summarized here. This repository preserves that chronology rather than rewriting the earlier certification scope.

## Verification philosophy

The objective is **falsifiability without reconstruction**: publish enough information to test whether stated properties hold, while withholding implementation detail that would provide a recipe for reproducing NightFall's proprietary system.

## Business and research

NightFall Proton and the underlying NightFall technologies are developed by NightFall Technologies. For current project information, research chronology, business inquiries, and contact information, use the canonical NightFall Technologies website.

Copyright © 2026 NightFall Technologies. All rights reserved.
