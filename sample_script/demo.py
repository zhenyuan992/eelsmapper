"""Run eelsmapper on the included sample dataset."""

from pathlib import Path
import sys

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from eelsmapper.pipeline import run_pipeline


def load_sample_data(path=None):
    if path is None:
        path = REPO_ROOT / "sample_data" / "specs.npz"
    path = Path(path)

    with np.load(path) as npz:
        key = "arr_0" if "arr_0" in npz.files else npz.files[0]
        data = npz[key]

    return data


def main():
    data = load_sample_data()
    print(f"Loaded sample data with shape: {data.shape}")

    results = run_pipeline(data)

    print("Pipeline outputs:")
    for name, value in results.items():
        shape = getattr(value, "shape", None)
        print(f"- {name}: shape={shape}")


if __name__ == "__main__":
    main()
