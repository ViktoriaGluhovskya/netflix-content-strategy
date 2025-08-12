import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, insert, select
from datetime import datetime

engine = create_engine("mysql+mysqlconnector://root:Babolat575@localhost:3306/Netflix_Content_Strategy")  
conn = engine.connect()
meta = MetaData()
meta.reflect(bind=engine)



df = pd.read_csv("netflix_titles.csv")
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

def get_or_create_ids(value, table):
    if pd.isna(value):
        return []
    ids = []
    for item in map(str.strip, str(value).split(",")):
        result = conn.execute(select(table.c.id).where(table.c.name == item)).fetchone()
        if result:
            ids.append(result[0])
        else:
            res = conn.execute(insert(table).values(name=item))
            ids.append(res.inserted_primary_key[0])
    return ids

for _, row in df.iterrows():
    ins = insert(shows).values(
        show_id=row["show_id"],
        type=row["type"],
        title=row["title"],
        date_added=row["date_added"].date() if pd.notna(row["date_added"]) else None,
        release_year=int(row["release_year"]) if pd.notna(row["release_year"]) else None,
        rating=row["rating"],
        duration=row["duration"],
        description=row["description"]
    )
    result = conn.execute(ins)
    db_show_id = result.inserted_primary_key[0]

    for cid in get_or_create_ids(row["country"], countries):
        conn.execute(insert(show_countries).values(show_id=db_show_id, country_id=cid))

    for aid in get_or_create_ids(row["cast"], actors):
        conn.execute(insert(show_actors).prefix_with("IGNORE").values(show_id=db_show_id, actor_id=aid))

    for gid in get_or_create_ids(row["listed_in"], genres):
        conn.execute(insert(show_genres).values(show_id=db_show_id, genre_id=gid))

    for did in get_or_create_ids(row["director"], directors):
        conn.execute(insert(show_directors).values(show_id=db_show_id, director_id=did))


conn.close()
print("NF .")


