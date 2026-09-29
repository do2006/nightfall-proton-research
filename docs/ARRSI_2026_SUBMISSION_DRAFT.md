# ARRSI 2026 Submission Package — Draft Content

## Anonymous title
Evidence-Gated Persistent Cognition: Evaluating Bounded Capability Promotion, Quarantine, and Rollback

## Submission type
Short systems/evaluation paper (target: up to 4 pages excluding references, ACL format).

## Abstract
Persistent agent systems need mechanisms for deciding when repeated experience should become reusable capability without turning every successful trace into trusted behavior. We describe and evaluate an evidence-gated persistent-cognition pipeline in which recurring observations produce bounded candidates, counterfactual analysis remains untrusted, promotion requires multiple evidence classes and explicit authority, and promoted capabilities retain scope, expiration, quarantine, and rollback controls. We report a research-alpha validation baseline spanning Windows and Linux/WSL2 and a later capability-promotion case that records recurrence, replay, historical, adversarial, and canary evidence. The contribution is primarily an evaluation and systems case study: how to make claims about persistent improvement traceable, bounded, reversible, and externally challengeable while separating durable cognitive state from model weights. We discuss limitations, including internally produced evidence, synthetic fixtures in parts of the promotion path, and the absence of independent third-party certification.

## Core research question
How can a persistent agent convert repeated experience into reusable capability while preserving evidence traceability, bounded applicability, explicit authority, failure-closed drift handling, quarantine, and rollback?

## Evidence to report
- 120 scenarios passed per platform in the Phase 17 research-alpha baseline.
- 36 failure-injection cases passed per platform.
- 10,000 property executions per platform.
- 10,000 native WSL2 libFuzzer runs and zero sanitizer findings.
- Valid eight-hour Windows and WSL2 soak pair.
- Later bounded capability record with three recurring observations.
- Replay, historical, adversarial, and canary proof classes recorded.
- Rollback required and quarantine blocks activation while preserving evidence.

## Required limitations
- Results are internally produced research evidence, not third-party certification.
- The research-alpha baseline was owner-controlled and local.
- Some later capability evidence uses synthetic fixtures and is not production truth.
- No claim of full recursive self-improvement or autonomous model-weight self-modification.
- Proprietary implementation is not included in the public evidence release.

## ARRSI reporting checklist
Artifacts: public evidence repository and stable release.
Compute: report bounded resource limits and available platform/resource measurements.
Human intervention: explicitly report owner authorization in promotion.
Failed runs: include invalidated evidence/failed cases where applicable.
Evaluation budget: report scenario, failure-injection, property, fuzz, and soak counts.
Exact component improved: durable cognitive capability/routing state, not base model weights.
Held-out/ablation status: do not claim results not yet measured; identify as future work where absent.

## Double-blind note
Remove company, product, repository, domain, personal names, signing identity/fingerprint, and uniquely identifying project labels from the submitted manuscript. Public artifacts may be disclosed only if permitted without breaking anonymity; otherwise defer links to camera-ready.
