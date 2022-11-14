import pandas as pd
Sheet_df = pd.read_excel(r'C:\Projects\Vendor dates\Vendor dates.xlsx')
Sheet_df = Sheet_df.dropna()
print(Sheet_df)