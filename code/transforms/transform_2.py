import numpy as np
import pandas as pd

def add_random_column(self, frame):
    self.log.info('Running add_random_column')
    sLength = len(frame[0:])
    frame['random_column'] = pd.Series(np.random.randn(sLength))
    return frame