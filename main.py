from get_files_selic import process_selic_data

def main():
    '''
    Main function to execute the SELIC, INFLATION, STOCKS and FIIs data processing
    '''
    url = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/pagamentos-e-parcelamentos/taxa-de-juros-selic"
    final_df = process_selic_data(url)
    print(final_df.head())

if __name__ == "__main__":
    main()