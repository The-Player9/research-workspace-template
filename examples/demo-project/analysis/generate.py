"""File 1 of 3: produces the expensive intermediates.

Run rarely, may need special hardware in a real project. Writes one file per
completed unit, atomically, and skips units that already exist, so an
interrupted run continues instead of restarting.

    python generate.py            # fill in what is missing
    python generate.py --rebuild  # ignore existing units
"""

import argparse

import numpy as np

import helpers as h


def run_unit(seed, noise):
    x, y = h.make_dataset(seed, noise)
    (x_tr, y_tr), (x_te, y_te) = h.split(x, y)
    slope, offset = h.fit_linear(x_tr, y_tr)
    pred_te = slope * x_te + offset
    return {
        "seed": np.array(seed),
        "noise": np.array(noise),
        "slope": np.array(slope),
        "offset": np.array(offset),
        "r2_test": np.array(h.r_squared(y_te, pred_te)),
        "x_test": x_te,
        "y_test": y_te,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rebuild", action="store_true")
    args = parser.parse_args()

    done, made = 0, 0
    for noise in h.NOISE_LEVELS:
        for seed in h.SEEDS:
            path = h.unit_path(seed, noise)
            if path.exists() and not args.rebuild:
                done += 1
                continue
            h.atomic_savez(path, **run_unit(seed, noise))
            made += 1
            print(f"  wrote {path.name}")

    print(f"generate.py: {made} unit(s) written, {done} already present")


if __name__ == "__main__":
    main()
