import pandas as pd
from pandas import DataFrame

def process_selic_data(url: str) -> DataFrame:
    #Read the tables from url
    tables = pd.read_html(url)
    final_data = []

    #Process relevant data
    for i,table in enumerate(tables[1:5]):

        table.columns = table.iloc[0]
        table = table[1:].reset_index(drop=True)

        table.fillna(0, inplace=True)
        table = table.replace('%', '', regex=True)
        table = table.replace(',', '.', regex=True)

        table_melted = table.melt(id_vars=['Mês/Ano'],var_name='Year',value_name='Value')
        final_data.append(table_melted)

    # Concatenate all data into one DataFrame
    final_df = pd.concat(final_data, ignore_index=True)
    final_df[['Year','Value']] = final_df[['Year','Value']].apply(pd.to_numeric)
    final_df.sort_values(by=['Year'], inplace=True, ascending=False)
    final_df.reset_index(drop=True, inplace=True)

    # Display the result
    return(final_df)


