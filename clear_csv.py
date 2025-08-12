import pandas as pd
import pycountry

def clean_dataset_strict(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [col.strip().lower() for col in df.columns]
    
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df = df.replace({'': None, 'nan': None})
    
    df = df[df['show_id'].notnull() & df['title'].notnull()]              
    df = df.drop_duplicates(subset=['show_id'])                           
    
    df['date_added']   = pd.to_datetime(df['date_added'], errors='coerce').dt.date
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').astype('Int64')
    current_year = pd.Timestamp.now().year
    df = df[df['release_year'].le(current_year)]                          
    
    for col in ['country', 'director', 'cast', 'listed_in']:
        df[col] = df[col].apply(lambda x: [i.strip() for i in x.split(',')] if isinstance(x, str) else [])
    
    def normalize_countries(lst):
        out = set()
        for name in lst:
            try:
                out.add(pycountry.countries.lookup(name).name)
            except Exception:
                out.add(name)
        return list(out)
    df['country'] = df['country'].apply(normalize_countries)
    
    df['description'] = df['description'].fillna('').str.replace(r'\s+', ' ', regex=True).str.strip()
    
    required_fields = [
        'show_id', 'type', 'title',
        'date_added', 'release_year',
        'rating', 'duration',
        'description'
    ]
    df = df.dropna(subset=required_fields)
    
    multi_cols = ['country', 'director', 'cast', 'listed_in']
    mask = df[multi_cols].applymap(lambda x: isinstance(x, list) and len(x) > 0).all(axis=1)
    df = df[mask]
    
    return df

df_raw   = pd.read_csv("netflix_titles.csv", dtype=str)
df_clean = clean_dataset_strict(df_raw)
df_clean.to_csv("netflix_titles_clean_strict.csv", index=False)