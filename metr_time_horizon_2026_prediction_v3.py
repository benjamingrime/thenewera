import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from scipy.optimize import curve_fit

# =============================================================================
# METR Task Horizon Prediction: The Rubin Jump (2019-2026)
# Data: METR TH1.1 (January 2026 update) -- 50% success time horizons
# =============================================================================

_dir = os.path.dirname(os.path.abspath(__file__))

# --- 1. Real METR Data ---
models = [
    "GPT-2", "GPT-3", "GPT-3.5", "GPT-4", "GPT-4o",
    "Claude 3.5 Sonnet", "o1-preview", "Claude 3.5 Sonnet v2", "o1",
    "Claude 3.7 Sonnet", "o3", "Claude 4 Opus", "GPT-5",
    "Claude Opus 4.5", "GPT-5.2",
]

# Months since Jan 2020
t_data = np.array([
    -10, 0, 26, 38,             # GPT-2 (Feb 2019), GPT-3, GPT-3.5, GPT-4
    52, 54, 56, 57, 59,         # GPT-4o -> o1
    61, 63, 64, 67,             # Claude 3.7 -> GPT-5
    70, 71,                     # Opus 4.5, GPT-5.2
], dtype=float)

# 50% time horizon in hours (from METR TH1.1)
y_data = np.array([
    0.00067,  # GPT-2:              2.4 sec
    0.0025,   # GPT-3:              9 sec
    0.010,    # GPT-3.5:            36 sec
    0.058,    # GPT-4:              3.5 min
    0.15,     # GPT-4o:             9 min
    0.18,     # Claude 3.5 Sonnet:  10.8 min
    0.37,     # o1-preview:         22 min
    0.50,     # Claude 3.5 Son v2:  30 min
    0.63,     # o1:                 37.9 min
    1.00,     # Claude 3.7 Sonnet:  60 min
    1.57,     # o3:                 94 min
    1.68,     # Claude 4 Opus:      101 min
    2.30,     # GPT-5:              138 min
    4.82,     # Claude Opus 4.5:    289 min
    6.57,     # GPT-5.2:            394 min
])

# Task description annotations for key thresholds (like the Dec 2025 METR chart)
task_annotations = {
    0.50: "Fix bugs in small python libraries",
    1.00: "Train classifier",
    1.57: "Exploit a buffer overflow\nin libsed1950",
    4.82: "Train adversarially robust image model",
    6.57: "Full-day engineering task",
}

# --- 2. Trend Line Definitions ---

# A. Expert Consensus: Doubling every 7 months
#    FIXED: Anchored at GPT-5.2 (month 71, 6.57 hrs) -- the latest known data
#    point. Anchoring at GPT-4 gave only 5.5 hrs for Dec 2026, which is already
#    exceeded by Dec 2025 data. The consensus line must pass through current reality.
ANCHOR_T = 71    # GPT-5.2 (Dec 2025)
ANCHOR_Y = 6.57  # 394 min

def consensus_curve(t):
    return ANCHOR_Y * (2 ** ((t - ANCHOR_T) / 7))

# B. Current Trend (Blackwell Era): Exponential fit to actual data
#    y = a * exp(b * t)
def exp_model(t, a, b):
    return a * np.exp(b * t)

popt, pcov = curve_fit(
    exp_model, t_data, y_data,
    p0=[1e-6, 0.15],
    bounds=([0, 0], [np.inf, np.inf]),
    maxfev=10000,
)
a_fit, b_fit = popt
doubling_time_current = np.log(2) / b_fit  # months

# C. Rubin-Accelerated Trend
#    Post-Month 78 (Q3 2026 Rubin ships): doubling time halves
#    Justification in rubin_inflection_analysis.md
RUBIN_MONTH = 78  # Q3 2026
b_rubin = b_fit * 2

def rubin_curve(t):
    if t <= RUBIN_MONTH:
        return exp_model(t, a_fit, b_fit)
    else:
        y_at_transition = exp_model(RUBIN_MONTH, a_fit, b_fit)
        return y_at_transition * np.exp(b_rubin * (t - RUBIN_MONTH))

# --- 3. Generate Projections ---
t_proj = np.linspace(-12, 84, 600)  # Feb 2019 to Dec 2026

y_consensus = np.array([consensus_curve(t) for t in t_proj])
y_current = exp_model(t_proj, a_fit, b_fit)
y_rubin = np.array([rubin_curve(t) for t in t_proj])

# Dec 31, 2026 predictions (Month 84)
pred_consensus = consensus_curve(84)
pred_current = exp_model(84, a_fit, b_fit)
pred_rubin = rubin_curve(84)

# --- 4. Visualization (METR-style) ---
# Style: white background, minimal, clean -- matching metr.org charts

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Segoe UI', 'Helvetica', 'Arial', 'sans-serif'],
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.edgecolor': '#cccccc',
    'axes.labelcolor': '#333333',
    'xtick.color': '#666666',
    'ytick.color': '#666666',
    'text.color': '#333333',
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})

fig, ax = plt.subplots(figsize=(14, 9))

# --- Shaded acceleration zone ---
ax.fill_between(t_proj, y_current, y_rubin,
                where=(y_rubin > y_current),
                alpha=0.08, color='#76B900', zorder=1)

# --- Trend lines ---
ax.plot(t_proj, y_consensus, '--', color='#BBBBBB', linewidth=1.5, zorder=2,
        label='Expert Consensus (7-month doubling)')
ax.plot(t_proj, y_current, color='#E8A838', linewidth=2.5, zorder=3,
        label=f'Current Trend ({doubling_time_current:.1f}-month doubling)')
ax.plot(t_proj, y_rubin, color='#76B900', linewidth=3, zorder=3,
        label=f'Rubin-Accelerated ({doubling_time_current / 2:.1f}-month doubling post-Q3\'26)')

# --- Rubin vertical marker ---
ax.axvline(x=RUBIN_MONTH, color='#76B900', linestyle=':', alpha=0.4, linewidth=1, zorder=2)

# --- Data points ---
ax.scatter(t_data, y_data, color='#3D8C40', s=50, zorder=5, edgecolors='white', linewidths=0.8)

# Only label key milestone models (skip the crowded middle)
key_labels = {
    'GPT-2':           (6, 6, 'left'),
    'GPT-3':           (6, 6, 'left'),
    'GPT-3.5':         (6, 6, 'left'),
    'GPT-4':           (6, 6, 'left'),
    'o3':              (6, 6, 'left'),
    'Claude Opus 4.5': (-6, 8, 'right'),
    'GPT-5.2':         (6, -6, 'left'),
}

for i, name in enumerate(models):
    if name not in key_labels:
        continue
    ox, oy, ha = key_labels[name]
    display_name = 'GPT-5.2 (high)' if name == 'GPT-5.2' else name
    ax.annotate(display_name, (t_data[i], y_data[i]),
                xytext=(ox, oy), textcoords='offset points',
                fontsize=8, color='#444444', ha=ha, va='bottom',
                zorder=6)

# --- Dec 2026 prediction markers ---
for pred_val, color in [
    (pred_consensus, '#999999'),
    (pred_current, '#E8A838'),
    (pred_rubin, '#76B900'),
]:
    ax.plot(84, pred_val, 'o', color=color, markersize=7, zorder=5,
            markeredgecolor='white', markeredgewidth=0.8)

# Prediction callouts -- positioned to avoid overlap
ax.annotate(
    f'{pred_rubin:.0f} hrs ({pred_rubin / 24:.0f} days)',
    xy=(84, pred_rubin), xytext=(-130, 30), textcoords='offset points',
    fontsize=11, color='#76B900', fontweight='bold',
    arrowprops=dict(arrowstyle='->', color='#76B900', lw=1.5),
    zorder=6)

ax.annotate(
    f'{pred_current:.0f} hrs ({pred_current / 24:.1f} days)',
    xy=(84, pred_current), xytext=(-140, -25), textcoords='offset points',
    fontsize=10, color='#E8A838', fontweight='bold',
    arrowprops=dict(arrowstyle='->', color='#E8A838', lw=1.2),
    zorder=6)

ax.annotate(
    f'{pred_consensus:.0f} hrs (1 day)',
    xy=(84, pred_consensus), xytext=(-110, -22), textcoords='offset points',
    fontsize=9, color='#999999',
    arrowprops=dict(arrowstyle='->', color='#999999', lw=1),
    zorder=6)

# --- Y-axis: human-readable time labels ---
def format_hours(val, pos):
    if val < 1/60:
        return f'{val * 3600:.0f} sec'
    elif val < 1:
        return f'{val * 60:.0f} min'
    elif val < 24:
        return f'{val:.0f} hrs'
    else:
        return f'{val / 24:.0f} days'

ax.yaxis.set_major_formatter(mticker.FuncFormatter(format_hours))

# --- X-axis: year labels (METR style) ---
year_ticks = [0, 12, 24, 36, 48, 60, 72, 84]
year_labels = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '']
ax.set_xticks(year_ticks)
ax.set_xticklabels(year_labels, fontsize=10)
ax.set_xlabel('Model release date', fontsize=11, color='#666666')

# Subtle vertical lines at year boundaries (like METR charts)
for yt in year_ticks[:-1]:
    ax.axvline(x=yt, color='#e0e0e0', linewidth=0.7, zorder=0)

# --- Title & subtitle (separate lines, no overlap) ---
fig.text(0.06, 0.96,
         'Time-horizon of tasks AI can complete at 50% success rate',
         fontsize=15, fontweight='bold', color='#222222', va='top')
fig.text(0.06, 0.92,
         'Task duration (for humans)  |  METR TH1.1 data + Rubin acceleration model',
         fontsize=10, color='#888888', va='top')

# --- Axis limits ---
ax.set_xlim(-14, 87)
ax.set_ylim(bottom=0, top=max(pred_rubin, pred_current) * 1.15)
ax.grid(False)

# Source attribution
fig.text(0.06, 0.02, 'Data: METR TH1.1 (Jan 2026)  |  metr.org',
         fontsize=8, color='#aaaaaa')
fig.text(0.94, 0.02, 'Rubin specs: NVIDIA CES 2026',
         fontsize=8, color='#aaaaaa', ha='right')

# --- Legend ---
ax.legend(loc='upper left', fontsize=9, frameon=False, labelcolor='#555555')

plt.subplots_adjust(top=0.88, bottom=0.10, left=0.08, right=0.95)
plt.savefig(os.path.join(_dir, 'metr_rubin_prediction.png'), dpi=200, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.show()

# --- 5. Console Output ---
print("=" * 70)
print("METR TASK HORIZON PREDICTION -- DEC 31, 2026")
print("=" * 70)
print(f"\nFitted Parameters (Current Trend):")
print(f"  y = {a_fit:.2e} * exp({b_fit:.4f} * t)")
print(f"  Doubling time: {doubling_time_current:.1f} months")
print(f"  (vs. Expert Consensus: 7.0 months)")
print()
print(f"Consensus anchored at GPT-5.2 (Dec 2025, {ANCHOR_Y} hrs)")
print(f"  -> 7-month doubling from current reality, not from GPT-4")
print()
print(f"PREDICTIONS FOR DEC 31, 2026 (Month 84):")
print(f"  Expert Consensus (7-mo doubling):    {pred_consensus:>8.1f} hours ({pred_consensus / 24:.1f} days)")
print(f"  Current Trend (Blackwell scaling):   {pred_current:>8.1f} hours ({pred_current / 24:.1f} days)")
print(f"  Rubin-Accelerated (HBM4 + CoDesign): {pred_rubin:>8.1f} hours ({pred_rubin / 24:.1f} days)")
print()
print(f"See rubin_inflection_analysis.md for full technical justification.")
print("=" * 70)
