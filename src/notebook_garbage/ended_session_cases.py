import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sessions.head(3)

sessions.groupby('school_id', 'stop_date').count()

continued_accounts = (sessions.groupby('school_id').agg({'stop_date' : [np.max]}) > pd.to_datetime("march 2018")).sum()

total_accounts = len(sessions.groupby('school_id').agg({'stop_date' : [np.max]}) > pd.to_datetime("march 2018"))

sessions.groupby('school_id').agg({'stop_date' : [np.max]}) > pd.to_datetime("march 2018")
