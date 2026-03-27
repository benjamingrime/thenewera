# The Rubin Effect: Modelling Hardware-Driven AI Task Horizon Gains in Late 2026

## Summary

Using real METR TH1.1 benchmark data (January 2026), we fit an exponential model to the 50% task-completion time horizons of frontier AI models from GPT-2 (2019) through GPT-5.2 (December 2025). We then model the impact of NVIDIA's Rubin R200 GPU (shipping Q3 2026) as a one-time capability boost, derived from generational capability scaling (γ = 0.48 from o1→o3 ARC-AGI cost data, independently corroborated at 0.454 by arXiv:2511.19492).

**Predictions for December 31, 2026** (1 working day = 8 hours)**:**

| Scenario | Task Horizon | Working Days |
|---|---|---|
| Expert Consensus (7-month doubling) | ~24 hours | 3 days |
| Current Trend (3.5-month doubling) | ~84 hours | ~11 days |
| Rubin-Adjusted (γ=0.48, 1.82x boost) | ~153 hours | ~19 days |

*Rubin uncertainty range: 141–162 hours depending on realised hardware cost reduction (3.0x–4.0x). Lower bound of ~130 hours if Rubin acts only as within-model inference scaling (γ≈0.35).*

---

## 1. The Data: What METR Actually Measures

METR's "50% time horizon" answers the question: *How long would a human expert take to complete tasks that this AI model can solve 50% of the time?*

Tasks are drawn from RE-Bench (ML research engineering), HCAST (general software engineering), and SWAA (software atomic actions) -- approximately 228 tasks in the TH1.1 suite.

### Observed Data Points (METR TH1.1, January 2026)

| Model | Release | 50% Time Horizon |
|---|---|---|
| GPT-2 | Feb 2019 | 2.4 seconds |
| GPT-3 (davinci-002) | May 2020 | 9 seconds |
| GPT-3.5 Turbo | Mar 2022 | 36 seconds |
| GPT-4 | Mar 2023 | 3.5 minutes |
| GPT-4o | May 2024 | 9 minutes |
| Claude 3.5 Sonnet | Jun 2024 | 10.8 minutes |
| o1-preview | Sep 2024 | 22 minutes |
| Claude 3.5 Sonnet v2 | Oct 2024 | 30 minutes |
| o1 | Dec 2024 | 37.9 minutes |
| Claude 3.7 Sonnet | Feb 2025 | 60 minutes |
| o3 | Apr 2025 | 94 minutes |
| Claude 4 Opus | May 2025 | 101 minutes |
| GPT-5 | Aug 2025 | 138 minutes |
| Claude Opus 4.5 | Nov 2025 | 289 minutes |
| GPT-5.2 | Dec 2025 | 394 minutes (~6.6 hours) |

---

## 2. The Three Trend Lines

### A. Past Trend (Hopper-Era Acceleration)

METR's original March 2025 paper established that task horizons had been doubling approximately every 7 months since 2019. This became the widely-cited "headline finding."

**Critical correction:** The original prompt (and Gemini's implementation) anchored the consensus line at GPT-4 (March 2023, 3.5 minutes). Extrapolating from there at 7-month doubling gives only ~5.5 hours by December 2026 -- but we are *already* at 6.6 hours as of December 2025 with GPT-5.2. The consensus line was underpredicting the present.

We anchor the consensus line at the latest data point (GPT-5.2, month 71, 6.57 hours) and project forward at the 7-month doubling rate. This represents the "conservative" scenario where the recent acceleration reverts to the long-term mean.

**Formula:** `y = 6.57 * 2^((t - 71) / 7)`

**December 2026 prediction:** ~24 hours (3 working days)

### B. Current Trend (Blackwell-Era Acceleration)

Fitting `y = a * exp(b * t)` to all 15 data points with positive parameter bounds yields:

- `a = 4.34e-06`
- `b = 0.1997`
- **Doubling time: 3.5 months**

This is 2x faster than the 7-month consensus. METR's own TH1.1 update (January 2026) confirmed the acceleration, reporting a doubling time of ~89 days (~3 months) for post-2024 models.

The acceleration is attributable to:
- Blackwell B200/GB200 hardware enabling larger-scale training runs
- Test-time compute scaling (o1, o3 reasoning models)
- Agentic scaffolding improvements (tool use, multi-step workflows)

**December 2026 prediction:** ~84 hours (~11 working days)

### C. Future Trend (Rubin-Era Acceleration)

This is where the analysis diverges from simple extrapolation. We model the NVIDIA Rubin R200 (shipping Q3 2026) as a one-time multiplicative boost to inference capability, derived from generational capability scaling between inference compute and task horizon.

**December 2026 prediction:** ~153 hours (~19 working days), range 141-162 hours

---

## 3. The Rubin Effect: Technical Reasoning

### Why This Is Not Just "More Compute"

Every previous GPU generation has provided incremental improvements. Rubin is notable because it simultaneously alleviates *three* independent bottlenecks that are specifically binding for the current generation of reasoning/agentic AI models:

### 3.1 The Memory Bandwidth Wall (2.75x)

| Spec | Blackwell B200 | Rubin R200 | Ratio |
|---|---|---|---|
| Memory type | HBM3e | HBM4 | -- |
| Bandwidth per GPU | 8 TB/s | 22 TB/s | **2.75x** |
| Capacity | 192 GB | 288 GB | 1.5x |

**Why this matters for task horizons:**

Autoregressive LLM decoding (token-by-token generation) is *memory-bandwidth-bound*, not compute-bound. Each generated token requires reading the full KV-cache from HBM. The speed of "thinking" -- the chain-of-thought reasoning that models like o1/o3 use to solve harder tasks -- is directly limited by how fast you can read from memory.

At 2.75x bandwidth, the same reasoning chain executes 2.75x faster. A 10-minute chain-of-thought becomes a 3.6-minute chain-of-thought for the same cost. This doesn't just save time -- it means labs can afford to let models reason *longer* on harder tasks within the same budget.

### 3.2 FP4 Compute Precision (5x)

| Spec | Blackwell B200 | Rubin R200 | Ratio |
|---|---|---|---|
| NVFP4 inference | 10 PFLOPS | 50 PFLOPS | **5x** |
| FP8 compute | 10 PFLOPS | ~16 PFLOPS | 1.6x |

**Why this matters for task horizons:**

NVIDIA's NVFP4 format uses a dual-level scaling scheme (per-tensor and per-block) that preserves accuracy competitive with FP8 for transformer inference. The 3rd-generation Transformer Engine in Rubin automates FP4/FP8 precision selection per layer.

For the prompt prefill phase (processing the context/instructions), which is compute-bound rather than memory-bound, Rubin delivers 5x throughput. This makes test-time compute -- the key technique behind reasoning -- 3-5x cheaper per token.

When reasoning is 3-5x cheaper, labs can scale test-time compute 3-5x more aggressively. METR's data and well-known results already show that additional test-time compute yields predictive gains on harder tasks.

### 3.3 The Co-Design Multiplier (2x)

| Spec | Blackwell (NVLink 5) | Rubin (NVLink 6) | Ratio |
|---|---|---|---|
| Chip-to-chip bandwidth | 1.8 TB/s | 3.6 TB/s | **2x** |
| NVL72 aggregate BW | ~130 TB/s | 260 TB/s | 2x |

**Why this matters for task horizons:**

Multi-step agentic loops (Reason -> Act -> Observe -> Reason) benefit linearly from latency reduction. Each step in an agent loop involves:
1. Reading context from the previous step
2. Generating a reasoning chain
3. Executing a tool call
4. Processing the result

When each step is 2-3x faster (from combined bandwidth + compute gains), a 10-step agent loop doesn't just complete 2-3x faster -- the reduced latency allows the model to take *more* steps within the same time budget, compounding the benefit.

Additionally, models will be natively optimized for Rubin's architecture:
- FP4-native training and inference (no post-training quantization accuracy loss)
- Agentic reasoning architectures designed around the latency/throughput profile
- Estimated ~2x software efficiency gain over the 12 months following Rubin deployment

### 3.4 The Combined Effect: From Cost Reduction to Horizon Boost

The three hardware factors interact across two distinct inference phases:

- **Decode phase** (token-by-token generation -- memory-bandwidth-bound): **2.75x** speedup from HBM4
- **Prefill phase** (processing prompts/context -- compute-bound): **up to 5x** speedup from FP4
- **Multi-GPU coordination**: **2x** from NVLink 6

Real-world LLM serving blends these phases. For a typical agentic workload (long reasoning chains with moderate context), the effective **end-to-end inference cost reduction is approximately 3-4x** (see NVIDIA's own estimate of "3-4x for typical LLM serving" from their Rubin technical blog). We use **3.5x** as our central estimate.

#### The scaling relationship: two regimes

How much additional task-horizon capability does extra compute buy? The answer depends critically on *what kind* of compute increase you're measuring.

**The motivating data** comes from the o1→o3 transition, comparing ARC-AGI inference costs against METR task horizons:

| Model | ARC-AGI cost/task (high compute) | METR 50% horizon |
|---|---|---|
| o1 | $3.80 | 37.9 min |
| o3 | $26.00 | 94 min |
| **Ratio** | **6.8x** | **2.48x** |

If the relationship were linear (H ∝ C), 6.8x more inference spend would yield 6.8x more horizon. Instead we observe only 2.48x -- consistent with a **power-law** relationship:

$$H \propto C^{\gamma} \quad \text{where } \gamma = \frac{\log(2.48)}{\log(6.8)} = 0.48$$

But what does this γ=0.48 actually measure? The o1→o3 transition was not simply "the same model using more tokens." o3 had substantially more RL training, architectural improvements, and better inference efficiency per token. The 2.48x horizon gain reflects *both* training-time progress *and* inference-time scaling, blended together. We call this the **generational capability elasticity**: the relationship between cost and capability *across hardware/model generations*.

#### Within-model scaling: the lower bound

When you hold the model fixed and only vary inference compute, the exponent is much lower. Empirical evidence from multiple sources:

| Experiment | Cost/compute ratio | Capability ratio | Implied γ |
|---|---|---|---|
| o3 low→medium on ARC-AGI | 2.07x ($1.22→$2.52/task) | 1.29x (41%→53%) | **0.35** |
| GPT-5 minimal→high on AA Intelligence Index | ~23x (3.5M→82M tokens) | 1.55x (score 44→68) | **0.14** |
| GPT-5 medium→high on SWE-bench | 1.5x (714→1053 reasoning tokens) | 0.96x (49.0%→47.1%) | **negative** |
| GPT-5.1-Codex-Max token budget | 6.4x (5M→32M budget) | "modest" gains | **~0.1** |

The pattern is consistent: giving the *same model* more compute yields rapidly diminishing returns. γ for within-model scaling is approximately **0.1-0.35**, with the higher end (o3 low→medium) reflecting a case where the model was specifically designed to benefit from variable compute allocation.

This sets a **lower bound** on the Rubin effect. If Rubin only provided "more tokens for the same model," the boost would be approximately 3.5^0.35 = 1.55x.

#### Why the cross-generation exponent applies to Rubin

But Rubin is not "turn the dial up on GPT-5.2." It is the hardware platform that enables the *next model generation* -- the GPT-6/o5-class systems that will be trained and optimised on Rubin architecture. This is the cross-generation dynamic, where γ≈0.48 applies, because:

1. **Cheaper inference enables more RL training.** Reinforcement learning for reasoning models requires running billions of inference-time verification loops during training. When inference is 3.5x cheaper, labs can afford 3.5x more RL iterations, producing qualitatively better reasoning chains -- the same dynamic that separated o3 from o1.

2. **Cheaper inference enables deeper default reasoning.** Models deployed on Rubin hardware can use longer chains-of-thought as their default operating mode (not just a "high compute" option), because the cost per reasoning step is fundamentally lower.

3. **The model development cycle accelerates.** Experimentation, evaluation, and iteration all involve inference. A 3.5x reduction in inference cost compresses the entire R&D feedback loop, enabling more architectural experiments per unit time.

4. **Historical precedent.** Each NVIDIA GPU generation (Volta→Ampere→Hopper→Blackwell) has enabled a new frontier model generation within 6-12 months of deployment. The relationship between hardware cost-performance and model capability is empirically cross-generational.

The o1→o3 transition -- 6.8x more inference cost enabling 2.48x more horizon via a blend of training and inference improvements -- is the *template* for what Rubin enables, not an anomaly. The γ=0.48 captures this generational dynamic.

#### Independent corroboration: arXiv:2511.19492

A recent paper ("Forecasting AI Time Horizon Under Compute Slowdowns," arXiv:2511.19492) provides independent corroboration of this exponent. Their core model links time-horizon growth directly to compute growth:

$$\frac{d \log Y}{dt} = c \cdot \frac{d \log(\text{compute})}{dt}$$

where $c = \frac{\partial \log Y}{\partial \log C}\bigg|_A \cdot (1 + \lambda/\beta)$ (Proposition 1). The key parameter $\frac{\partial \log Y}{\partial \log C}\bigg|_A$ -- the elasticity of time horizon with respect to training compute, holding algorithms fixed -- is estimated at **0.454** from shared-slope regression across Llama 3.1 and Qwen 2.5 model families (30 data points, R²=0.949; Appendix C).

This 0.454 measures *training-compute* elasticity (how task horizon scales with training FLOPs across model sizes), while our 0.48 measures *cross-generation inference-cost* elasticity (how horizon scales with inference spend across model generations). These are conceptually different quantities -- yet they converge to within 6% of each other. This convergence suggests that the sub-linear exponent γ≈0.45-0.48 is a robust feature of the current scaling regime, not an artifact of any single dataset or measurement approach.

#### The spending slowdown and why it doesn't apply here

The same paper argues that compute *spending* growth must slow after ~2028, causing time-horizon growth to decelerate proportionally. Their headline: "1-month time horizons at 80% reliability occur 77 years later than simple trend extrapolation suggests."

This claim is directionally correct. Dollar-denominated compute growth cannot sustain 4-5x/year indefinitely -- the financial constraints are real. But their model has a critical blind spot: it treats hardware efficiency (FLOPs per dollar) as improving at a fixed historical rate, missing discrete hardware transitions.

Their equation decomposes as:

$$\frac{d \log(\text{FLOPs})}{dt} = \frac{d \log(\$)}{dt} + \frac{d \log(\text{FLOPs}/\$)}{dt}$$

If dollar spending growth slows ($d\log(\$)/dt \to 0$), effective compute can still grow if FLOPs/$ improves fast enough. Rubin provides a **discrete 3.5x step-jump** in FLOPs/$ -- a hardware discontinuity that their smooth-rate assumption does not capture.

Crucially, their spending slowdown kicks in post-2028. Rubin ships Q3 2026. Our prediction window (December 2026) falls entirely within the period where even the pessimistic view agrees compute is still compounding aggressively. The medium-term question -- whether the NVIDIA hardware roadmap sustains 2-3x/year FLOPs/$ improvements after Rubin -- is real, but it is a 2028+ question, not a 2026 one.

#### Estimating the Rubin boost

We fix γ=0.48 and model uncertainty through the hardware cost reduction estimate, which is the less-well-determined input:

| Cost reduction | Source | Rubin boost (γ=0.48) |
|---|---|---|
| 3.0x | Conservative: HBM4 bandwidth + partial FP4 gains | 1.68x |
| **3.5x** | **Central: NVIDIA estimate for typical LLM serving** | **1.82x** |
| 4.0x | Optimistic: full FP4 + NVLink 6 compound gains | 1.93x |

For reference, if Rubin acts only as "more tokens for the same model" (within-model γ≈0.35), the central boost would be 3.5^0.35 = 1.55x -- a useful lower bound.

**Applying to the projection:**

1. **Rubin delivers 3.0-4.0x cheaper inference** (hardware specs, sections 3.1-3.3)
2. **Labs deploy equivalently more inference per task** at the same cost ceiling (economic incentive)
3. **Under generational scaling: 3.5^0.48 = 1.82x one-time horizon multiplier** (central estimate)
4. This is equivalent to shifting the timeline forward by ~3.0 months (ln(1.82) / b_fit)

The Rubin effect is a **one-time multiplicative jump** at month 78, not a change in the growth rate. After the jump, the exponential trend continues at the same rate `b`. The doubling time remains 3.5 months. This is physically correct: a hardware generation change alters the cost-performance ratio (a constant), not the rate of algorithmic progress (the exponent).

#### In code

```python
b_fit = 0.1997                         # fitted growth rate (3.5-month doubling)
gamma = 0.48                           # generational capability elasticity
cost_reduction = 3.5                   # Rubin inference cost ratio (central)
cost_reduction_con = 3.0               # conservative
cost_reduction_opt = 4.0               # optimistic
rubin_boost = cost_reduction ** gamma  # = 1.82x one-time horizon multiplier

# Post-Rubin: same growth rate, shifted curve
# H_rubin(t) = H_trend(t) * rubin_boost   for t > 78
```

#### Revision history

*v1: Incorrectly applied a linear scaling relationship to derive 1.8 additional doublings from 3.5x cost reduction, permanently doubling the growth rate. v2: Corrected to power-law model with γ=0.48 from ARC-AGI data, single estimate with γ uncertainty range. v3 (current): Reframed γ=0.48 as generational capability elasticity, supported by two-regime analysis (within-model γ≈0.15-0.35 vs cross-generation γ≈0.48). Uncertainty now driven by hardware cost reduction range (3.0-4.0x) rather than γ variation. Added independent corroboration from arXiv:2511.19492 (training-compute elasticity 0.454) and spending-slowdown analysis.*

---

## 4. The Underestimation Delta

Comparing the three METR snapshots reveals a consistent pattern of expert underestimation:

| Snapshot | Latest Model | Horizon | Consensus Would Have Predicted |
|---|---|---|---|
| Jan 2025 (METR original) | Claude 3.7 Sonnet | 60 min | ~25 min (from GPT-4 anchor) |
| Jun 2025 (80,000 Hours) | o3 | 94 min | ~35 min |
| Dec 2025 (METR TH1.1) | GPT-5.2 | 394 min | ~75 min |

The "Underestimation Delta" grows over time because the actual trend is exponential with a shorter doubling period (~3.5 months) than the consensus (~7 months). Each successive snapshot finds models further above the consensus line than the last.

By December 2026:
- The consensus line predicts ~24 hours
- The current trend predicts ~84 hours (3.5x higher)
- With Rubin, ~153 hours (~19 working days, 6.4x higher, range 141-162 hrs)

This pattern -- experts consistently underestimating by anchoring to the long-term mean while the actual trend accelerates -- illustrates why the "current trend" line is a better baseline than the consensus. The Rubin hardware boost adds a meaningful but bounded uplift on top of the already-fast 3.5-month doubling trend.

---

## 5. Caveats

1. **METR's own warnings**: Automatic scoring overestimates real-world performance. Models often produce code that passes test suites but has quality/integration issues requiring human cleanup.

2. **Confidence intervals are wide**: Claude Opus 4.5's 95% CI spans from 1h49m to 20h25m. Point estimates should be read as central tendencies, not precise predictions.

3. **The Rubin acceleration is a model, not a measurement**: We are projecting the *hardware capability* impact, not accounting for potential algorithmic plateaus, regulatory constraints, or other exogenous factors.

4. **Doubling time may not stay constant**: The 3.5-month doubling could slow down (diminishing returns on scaling) or speed up further (algorithmic breakthroughs). The Rubin model assumes the acceleration holds for 6 months post-deployment.

5. **Task horizon != productivity**: METR notes that even ~1-hour models are far from providing 2x developer productivity in real workflows. The gap between "can solve isolated benchmark tasks" and "can autonomously run multi-day projects" involves coordination, planning, error recovery, and other capabilities not fully captured by the benchmark.

6. **γ=0.48 is a cross-generation blend**: The generational capability elasticity γ=0.48 captures both training-time improvements and inference-time scaling between model generations. Within-model inference scaling alone yields γ≈0.15-0.35. Our Rubin model assumes hardware generations enable model generations (the cross-generation dynamic), which is historically accurate but not guaranteed. If Rubin hardware is deployed only with existing models, the boost would be ~1.55x rather than ~1.82x.

7. **Compute spending slowdown is real but delayed**: arXiv:2511.19492 correctly identifies that 4-5x/year compute spending growth is unsustainable. Their model implies significant deceleration post-2028. Our December 2026 prediction falls within the period where this constraint is not yet binding, but extensions beyond 2027 should account for spending flattening.

---

## 6. Methodology

**Curve fitting**: `scipy.optimize.curve_fit` with model `y = a * exp(b * t)`, positive parameter bounds `[0, inf]`, initial guess `p0 = [1e-6, 0.15]`. All 15 data points used (GPT-2 through GPT-5.2).

**Consensus line**: `y = 6.57 * 2^((t - 71) / 7)` -- anchored at latest data point, 7-month doubling per original METR finding.

**Rubin adjustment**: One-time multiplicative boost of 3.5^0.48 = 1.82x applied at month 78 (Q3 2026). Growth rate `b` is unchanged post-Rubin. The generational capability elasticity γ = 0.48 is calibrated from o1→o3 ARC-AGI inference cost data ($3.80 vs $26/task for horizons of 37.9 vs 94 min), independently corroborated at 0.454 by arXiv:2511.19492 (Llama/Qwen training-compute regression, R²=0.949). Uncertainty modelled via hardware cost reduction range (3.0x–4.0x) yielding boosts of 1.68x–1.93x. Lower bound using within-model γ≈0.35: boost of 1.55x.

**Data sources**:
- METR TH1.1 (January 2026): https://metr.org/blog/2026-1-29-time-horizon-1-1/
- METR original paper: arXiv:2503.14499
- NVIDIA Rubin R200 specs: CES 2026 announcement, NVIDIA developer blog
- Blackwell B200 baseline: NVIDIA official datasheets
- arXiv:2511.19492: "Forecasting AI Time Horizon Under Compute Slowdowns" (training-compute elasticity, spending projections)
- ARC Prize o3 analysis: https://arcprize.org/blog/analyzing-o3-with-arc-agi (within-model inference scaling data)
- Artificial Analysis GPT-5 benchmarks: https://artificialanalysis.ai/articles/gpt-5-benchmarks-and-analysis (reasoning effort token usage)
- SWE-bench GPT-5 analysis: GPT-5 medium vs high reasoning effort on SWE-bench Verified
