#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import random
from dataclasses import dataclass
from typing import List, Tuple, Optional
import numpy as np
from math import cos, sin

DEGREE_OF_WAVE = 100

@dataclass
class Wave:
    wave_coefs: List[Tuple[float]]
    number_of_xs: int = 10 ** 4
    cached_values: Optional[List[float]] = None

    @property
    def xs(self):
        return np.linspace(-1, 1, self.number_of_xs)

    @property
    def values(self):
        return [sum([self.wave_coefs[i][0] * cos(i * x) + self.wave_coefs[i][1] * sin(i * x) for i
                in range(len(self.wave_coefs))]) for x in self.xs]

    def plot(self):
        import matplotlib.pyplot as plt
        plt.plot(self.xs, self.values)
        plt.show()

def main():
    coefs = [(random(), random()) for _ in range(DEGREE_OF_WAVE + 1)]
    wave = Wave(coefs)
    wave.plot()

if __name__ == '__main__':
    main()
