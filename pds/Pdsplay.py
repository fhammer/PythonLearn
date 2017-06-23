#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from play import FuncPy

seriesd = pd.Series(np.random.randn(100))

print(seriesd.head())
FuncPy.say_hello(seriesd.head())
