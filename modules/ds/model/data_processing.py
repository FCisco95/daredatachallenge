import pandas as pd

def perform_eda_and_preprocessing(df):

 # Calculate win-loss ratio
    df['win_loss_ratio'] = df['partidosganados'] / df['partidosjugados']

    # Convert tournament winnings to binary values
    df['won_tournament_2020'] = (df['2020_Torneos ganados'] > 0).astype(int)

    # Extract birth year from date of birth
    df['birth_year'] = pd.to_datetime(df['fechanacimiento']).dt.year

    # Calculate age based on birth year
    df['age'] = 2020 - df['birth_year']

    # Drop unnecessary columns
    columns_to_drop = ['fechanacimiento', 'birth_year']
    df = df.drop(columns=columns_to_drop)

    return df