import pandas as pd


# This class has the necessary functions to generate summary statistics
class SummaryStats:
    """
    This class gives basic summary statistics
    """

    def freq(df):
        """
        This function gives frequency table of the dataframe and prints the frequency table.
        """
        df = df.select_dtypes(include=['object'])
        col = df.columns
        for i in col:
            print(pd.crosstab(index=df[i], columns='count').sort_values(by='count', ascending=False), '\n')

    def summarize(df, path):
        """
        This function give final cumulative summary table of the dataframe and outputs to a specified path.
        """
        df['Cumulative Cases'] = df.groupby(by=['FIPS'])['Daily Cases'].transform(lambda x: x.cumsum())
        df['Cumulative Deaths'] = df.groupby(by=['FIPS'])['Daily Deaths'].transform(lambda x: x.cumsum())
        df = df[['Date', 'County', 'State', 'FIPS', 'Population', 'Daily Cases', 'Daily Deaths',
                 'Cumulative Cases', 'Cumulative Deaths']]
        df.to_csv(path + '\summary.csv', index=False)
