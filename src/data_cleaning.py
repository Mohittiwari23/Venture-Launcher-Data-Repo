import pandas as pd

def load_df(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def filter_df(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['Countries of investment'].astype(str).str.contains("India",case=False,na=False)]

def save_df(df: pd.DataFrame, file_path: str) -> None:
    df.to_csv(file_path, index=False)

def filter_na_url(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['Website'].notnull()]

def normalize_stages(stage_str):
    if pd.isnull(stage_str):
        return []
    stages = [s.split('.')[-1].strip() for s in stage_str.split(',')]
    return stages

def parse_cheque(val):
    try:
        return float(str(val).replace('$','').replace(',','').strip())
    except:
        return None

def drop_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop(columns=['Stage of investment','First cheque minimum','First cheque maximum','Countries of investment'])

if __name__ == "__main__":
    df = load_df("C:/Users/inbox/PycharmProjects/PythonProject/data/raw/Dec 2024 - OpenVC.csv")
    df_filtered = filter_df(df)
    df_filtered = filter_na_url(df_filtered)
    save_df(df_filtered, "C:/Users/inbox/PycharmProjects/PythonProject/data/interim/Dec 2024 - OpenVC.csv")
    df_filtered['Preferred Stages'] = df_filtered['Stage of investment'].apply(normalize_stages)
    df_filtered['Cheque Min'] = df_filtered['First cheque minimum'].apply(parse_cheque)
    df_filtered['Cheque Max'] = df_filtered['First cheque maximum'].apply(parse_cheque)
    df_filtered = drop_columns(df_filtered)
    save_df(df_filtered, "C:/Users/inbox/PycharmProjects/PythonProject/data/processed/Dec 2024 - OpenVC.csv")
    print("Data filtered")