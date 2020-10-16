import pandas as pd

def final_merge(covid_df, pop_df):
    covid_df = covid_df
    pop_df = pop_df
    final = pd.merge(covid_df, pop_df, on=['FIPS'], how='left')
    final['Population'] = final['Population'].fillna(0).astype(int)
    final.columns = ['Date', 'County', 'State', 'FIPS', 'Daily Cases', 'Daily Deaths', 'Population']
    final = final.sort_values(by=['Date', 'State', 'County'], ascending=[True, True, True])
    return final