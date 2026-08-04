"""File 2 of 3: every figure and every reported number, from stored data.

Runs in seconds, needs no special hardware, and writes `Output.txt` in which
each number carries the place it appears in the manuscript. A number that is in
the manuscript but not in `Output.txt` is an open item, not a rounding
difference.

    python evaluate.py
"""

import numpy as np

import helpers as h


def load_all():
    units = []
    for noise in h.NOISE_LEVELS:
        for seed in h.SEEDS:
            path = h.unit_path(seed, noise)
            if not path.exists():
                raise SystemExit(f"missing intermediate: {path.name} — run generate.py first")
            units.append(dict(np.load(path)))
    return units


def self_check(units):
    """Recompute something the generation script stored and assert agreement.

    Catches silent format drift between the two scripts, which is the failure
    mode that produces confidently wrong numbers.
    """
    worst = 0.0
    for u in units:
        pred = float(u["slope"]) * u["x_test"] + float(u["offset"])
        worst = max(worst, abs(h.r_squared(u["y_test"], pred) - float(u["r2_test"])))
    return worst


def main():
    units = load_all()
    lines = ["Demo project — reported numbers", "=" * 40, ""]

    drift = self_check(units)
    lines.append(f"[self-check] max deviation recomputed vs. stored R2: {drift:.2e}")
    lines.append("")

    lines.append("[Table 1] slope and offset per noise level (mean +/- std over 5 seeds)")
    lines.append(f"  ground truth: slope = {h.TRUE_SLOPE}, offset = {h.TRUE_OFFSET}")
    for noise in h.NOISE_LEVELS:
        sel = [u for u in units if float(u["noise"]) == noise]
        slope = np.array([float(u["slope"]) for u in sel])
        offset = np.array([float(u["offset"]) for u in sel])
        lines.append(
            f"  noise {noise:.2f}: slope {slope.mean():.4f} +/- {slope.std():.4f}, "
            f"offset {offset.mean():.4f} +/- {offset.std():.4f}"
        )
    lines.append("")

    lines.append("[Section 3.2, sentence 2] test R2 per noise level (mean +/- std over 5 seeds)")
    for noise in h.NOISE_LEVELS:
        r2 = np.array([float(u["r2_test"]) for u in units if float(u["noise"]) == noise])
        lines.append(f"  noise {noise:.2f}: R2 = {r2.mean():.4f} +/- {r2.std():.4f}")
    lines.append("")

    r2_clean = np.mean([float(u["r2_test"]) for u in units if float(u["noise"]) == 0.0])
    r2_worst = np.mean([float(u["r2_test"]) for u in units if float(u["noise"]) == max(h.NOISE_LEVELS)])
    lines.append("[Abstract, last sentence] degradation from clean to worst noise level")
    lines.append(f"  R2 {r2_clean:.4f} -> {r2_worst:.4f} (drop {r2_clean - r2_worst:.4f})")
    lines.append("")

    made_figure = write_figure(units)
    lines.append(f"[Figure 1] {'written to results/figure_1.png' if made_figure else 'skipped (matplotlib not installed)'}")

    h.OUTPUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print(f"\nevaluate.py: wrote {h.OUTPUT_FILE.name}")


def write_figure(units):
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return False

    h.RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    means = [np.mean([float(u["r2_test"]) for u in units if float(u["noise"]) == n]) for n in h.NOISE_LEVELS]
    stds = [np.std([float(u["r2_test"]) for u in units if float(u["noise"]) == n]) for n in h.NOISE_LEVELS]

    fig, ax = plt.subplots(figsize=(4, 3), constrained_layout=True)
    ax.errorbar(h.NOISE_LEVELS, means, yerr=stds, marker="o", capsize=3)
    ax.set_xlabel("noise level")
    ax.set_ylabel(r"test $R^2$")
    fig.savefig(h.RESULTS_DIR / "figure_1.png", dpi=150)
    plt.close(fig)
    return True


if __name__ == "__main__":
    main()
