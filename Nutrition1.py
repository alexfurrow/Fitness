Nutrition1

import pandas as pd
import numpy as np
import glob

path = "C:\\Users\\alexa\\OneDrive\\Desktop\\Nutrition\\FoodData_Central_foundation_food_csv_2022-04-28"
all_files = glob.glob(path+"/*.csv")
all_files = pd.DataFrame(all_files)
