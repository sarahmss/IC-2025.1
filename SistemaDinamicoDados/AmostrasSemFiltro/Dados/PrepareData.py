import pandas as pd
import numpy as np

for i in range(4, 5, 1):
    Data = pd.read_csv(f"../Dados/Data{i}.csv")
    Data = Data.drop(columns=["VD", "VE", "tempo"])
    Data.index = (np.arange(0, len(Data), 1).astype(float) * 0.07).round(5)
    Data = Data.rename(columns={
        "Setpoint VD": "Wd",
        "Setpoint VE": "We",
        "Theta": "theta(Wd,We)",
        "X": "x(Wd,We)",
        "Y": "y(Wd,We)",
    })
    Data.to_csv(f"../Dados/Data{i}.csv")