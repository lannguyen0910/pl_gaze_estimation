import numpy as np
from typing import Tuple
from omegaconf import DictConfig


def get_dataset_stats(config: DictConfig) -> Tuple[np.ndarray, np.ndarray]:
    mean = np.array(config.DATASET.MEAN)
    std = np.array(config.DATASET.STD)
    return mean, std
