# Agent Evaluation Science Fall 2026 — Extended Abstract Draft

## Title
Evidence-Gated Persistent Cognition: A Black-Box Evaluation Framework for Promotion, Quarantine, and Rollback

## Authors
Dwayne O'Neill — NightFall Technologies

## Evaluation target
A persistent cognitive runtime in which durable goals, memory, routes, constraints, learned capabilities, and health/recovery state remain outside base model weights and are projected into live-model context as needed.

## Evaluation problem
A successful agent trace is not evidence that behavior should become trusted persistent capability. Evaluation therefore needs to distinguish observation, recurrence, candidate generation, qualification, trusted promotion, activation, drift, quarantine, and rollback as separate measurable stages.

## Framework
We define black-box checks for recurrence thresholds, candidate isolation, proof gating, scope enforcement, drift failure-closed behavior, quarantine, rollback, checkpoint recovery, and repeated-run reporting. The framework requires explicit runtime/evaluator versions, fixture hashes, pass/fail criteria, failures, exclusions, and limitations.

## Case evidence
An internal research-alpha baseline records 120 scenarios passed per platform, 36 failure injections per platform, 10,000 property executions per platform, 10,000 native WSL2 libFuzzer runs, zero sanitizer findings, and valid eight-hour Windows and WSL2 soaks. A later bounded capability record contains three recurring observations, replay/historical/adversarial/canary proof classes, explicit task boundaries, rollback requirements, and quarantine behavior.

## Interpretation
These results establish an internally evidenced evaluation path, not independent certification. The evaluation contribution is the decomposition of persistent learning claims into falsifiable lifecycle properties and the explicit retention of recovery controls after promotion.

## Limitations and next measurements
Evidence is internally produced; some later fixtures are synthetic; independent replication is pending. Future evaluation should add held-out tasks, ablations of proof classes and recurrence thresholds, external evaluator runs, quantitative capability deltas, and stronger measurements separating genuine accumulated improvement from retrieval/context effects.

## Public artifact
NightFall Proton Public Research Release 1.0 provides the black-box specification, machine-readable claims, claim-to-evidence matrix, integrity hashes, and demonstration protocol.
