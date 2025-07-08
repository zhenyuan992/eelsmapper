# assuming you have installed with !pip install eelsmapper

from eelsmapper.pipeline import run_pipeline
import numpy as np

data = np.load("specs.npz")["arr_0"]
data = data.reshape(-1,data.shape[-1])

run_pipeline( data )