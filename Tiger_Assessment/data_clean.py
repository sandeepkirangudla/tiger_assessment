import pandas as pd


def clean(covid_df, pop_df):
    """
    This function cleans data frame and returns data frames.
    """
    covid_df = covid_df
    pop_df = pop_df

    # Maps to the correct column names
    pop_df_col_map = {'STATE': 'State_ID', 'COUNTY': 'County_ID', 'POPESTIMATE2019': 'Population'}
    pop_df.columns = [pop_df_col_map.get(x, "No_key") for x in pop_df.columns]

    covid_df_col_map = {'date': 'Date', 'county': 'County', 'state': 'State', 'CTYNAME': 'County',
                        'fips': 'FIPS', 'cases': 'Cases', 'deaths': 'Deaths'}
    covid_df.columns = [covid_df_col_map.get(x, "No_key") for x in covid_df.columns]

    # Combining State FIPS ID and County FIPS ID to 1 column and adding leading zeros
    pop_df['State_ID'] = pop_df['State_ID'].map('{:0>2}'.format)
    pop_df['County_ID'] = pop_df['County_ID'].map('{:0>3}'.format)
    pop_df['FIPS'] = pop_df['State_ID'] + pop_df['County_ID']
    pop_df = pop_df.drop(['State_ID', 'County_ID'], axis=1)
    covid_df['FIPS'] = covid_df['FIPS'].fillna(0).astype(int)
    covid_df['FIPS'] = covid_df['FIPS'].map('{:0>5}'.format)

    # standardizing the date column
    covid_df['Date'] = pd.to_datetime(covid_df['Date'], format='%Y-%m-%d')

    # sorting covid_df by Date for better understanding
    covid_df = covid_df.sort_values(by='Date', ascending=True, ignore_index=True)

    return (covid_df, pop_df)