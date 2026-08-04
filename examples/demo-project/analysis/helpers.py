"""Shared configuration and functions for the demo analysis.

File 3 of 3. Holds everything both other scripts need, so neither imports the
other. Expensive dependencies are imported lazily inside the functions that
need them, which is what lets `evaluate.py` run without them.
"""

from pathlib import Path

# --- configuration -------------------------------------------------------
SEEDS = [1, 2, 3, 4, 5]
N_SAMPLES = 400
NOISE_LEVELS = [0.0, 0.02, 0.05]
TRUE_SLOPE = 2.5
TRUE_OFFSET = 0.8
SEED_SPLIT = 0.7  # train fraction

HERE = Path(__file__).resolve().parent
INTERMEDIATE_DIR = HERE / "intermediate"
RESULTS_DIR = HERE / "results"
OUTPUT_FILE = HERE / "Output.txt"


def make_dataset(seed, noise):
    """Synthetic stand-in for a measurement. Deterministic given (seed, noise)."""
    import numpy as np

    rng = np.random.default_rng(seed)
    x = rng.uniform(0.0, 1.0, N_SAMPLES)
    y = TRUE_SLOPE * x + TRUE_OFFSET + rng.normal(0.0, noise, N_SAMPLES)
    return x, y


def fit_linear(x, y):
    """Least-squares fit, returned as (slope, offset)."""
    import numpy as np

    a = np.vstack([x, np.ones_like(x)]).T
    slope, offset = np.linalg.lstsq(a, y, rcond=None)[0]
    return float(slope), float(offset)


def r_squared(y_true, y_pred):
    import numpy as np

    ss_res = float(np.sum((y_true - y_pred) ** 2))
    ss_tot = float(np.sum((y_true - np.mean(y_true)) ** 2))
    return 1.0 - ss_res / ss_tot


def split(x, y):
    n_train = int(SEED_SPLIT * len(x))
    return (x[:n_train], y[:n_train]), (x[n_train:], y[n_train:])


def atomic_savez(path, **arrays):
    """Write to a temporary file, then rename.

    A crash during the write must not corrupt the previous state, which is the
    whole point of a resumable job.
    """
    import numpy as np

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # The temporary name must end in .npz: np.savez appends the suffix itself
    # when it is missing, and the rename would then miss the written file.
    tmp = path.parent / (path.name + ".tmp.npz")
    np.savez(tmp, **arrays)
    tmp.replace(path)


def unit_path(seed, noise):
    return INTERMEDIATE_DIR / f"fit_seed{seed}_noise{noise:.2f}.npz"
