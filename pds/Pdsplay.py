#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

seriesd = pd.Series(np.random.randn(100))

print(seriesd.head())