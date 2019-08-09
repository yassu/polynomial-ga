#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import random
from entities import Wave

DEGREE_OF_WAVE = 100


def main():
    coefs = [(random(), random()) for _ in range(DEGREE_OF_WAVE + 1)]
    wave = Wave(coefs)
    wave.plot()

if __name__ == '__main__':
    main()
