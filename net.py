import ast
import logging
import mysql.connector
import pandas as pd

LOG_FILENAME = 'import_shows.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILENAME, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

logger.info("Starting CSV import into MySQL")

csv_path = 'netflix_titles_clean_strict.csv'
logger.info(f"Reading file {csv_path}")
df = pd.read_csv(csv_path)

def parse_list_cell(cell):
    if pd.isna(cell):
        return []
    return [item.strip().strip("'\"") for item in ast.literal_eval(cell)]

try:
    cnx = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='Babolat575',
        database='Netflix_new_db',
        charset='utf8mb4'.     
    )
    cursor = cnx.cursor()
    logger.info("Successfully connected to MySQL on port 3306")
except mysql.connector.Error as err:
    logger.error(f"Database connection failed: {err}")
    raise

def get_or_create(table, name):
    cursor.execute(f"SELECT id FROM {table} WHERE name = %s", (name,))
    row = cursor.fetchone()
    if row:
        return row[0]
    cursor.execute(f"INSERT INTO {table} (name) VALUES (%s)", (name,))
    cnx.commit()
    logger.debug(f"Inserted into {table}: {name}")
    return cursor.lastrowid

for idx, row in df.iterrows():
    try:
        logger.info(f"Processing row {idx+1}: show_id={row['show_id']}")
        # 4.1 Insert into shows
        cursor.execute("""
            INSERT INTO shows
              (show_id, type, title, date_added,
               release_year, rating, duration, description)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['show_id'],
            row['type'],
            row['title'],
            pd.to_datetime(row['date_added']).date(),
            int(row['release_year']),
            row['rating'],
            row['duration'],
            row['description']
        ))
        cnx.commit()
        show_pk = cursor.lastrowid
        logger.debug(f"Inserted show with PK={show_pk}")

        # 4.2 Countries
        for country in parse_list_cell(row['country']):
            country_pk = get_or_create('countries', country)
            cursor.execute(
                "INSERT IGNORE INTO show_countries (show_id, country_id) VALUES (%s, %s)",
                (show_pk, country_pk)
            )

        # 4.3 Actors
        for actor in parse_list_cell(row['cast']):
            actor_pk = get_or_create('actors', actor)
            cursor.execute(
                "INSERT IGNORE INTO show_actors (show_id, actor_id) VALUES (%s, %s)",
                (show_pk, actor_pk)
            )

        # 4.4 Genres
        for genre in parse_list_cell(row['listed_in']):
            genre_pk = get_or_create('genres', genre)
            cursor.execute(
                "INSERT IGNORE INTO show_genres (show_id, genre_id) VALUES (%s, %s)",
                (show_pk, genre_pk)
            )

        # 4.5 Directors
        for director in parse_list_cell(row['director']):
            director_pk = get_or_create('directors', director)
            cursor.execute(
                "INSERT IGNORE INTO show_directors (show_id, director_id) VALUES (%s, %s)",
                (show_pk, director_pk)
            )

        cnx.commit()
        logger.info(f"Successfully imported show_id={row['show_id']} (PK={show_pk})")
    except Exception as e:
        logger.exception(f"Error processing show_id={row['show_id']}: {e}")

# 5. Close connection
cursor.close()
cnx.close()
logger.info("Import complete; MySQL connection closed")

