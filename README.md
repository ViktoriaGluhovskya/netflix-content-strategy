# Netflix Content Strategy – Analysis of Global Trends

In this project, I analyzed Netflix’s global content library to understand which content types and genres dominate, how they are distributed by country, and how trends have evolved over the years.  
I completed the full cycle of work — from cleaning and structuring the data in MySQL to building interactive dashboards in Tableau.

---

## Project Aim

My goal was to explore Netflix’s global catalog, identify the most popular content types, genres, and production countries, and analyze how the structure of the catalog has changed over time.  
The objective was to transform raw data into actionable insights that could guide strategic decisions in content planning and audience engagement.

---

## Datasets Used

The analysis is based on a cleaned and normalized version of the **Netflix Movies & TV Shows** dataset (source: Kaggle), stored and managed in a **MySQL** relational database.

**Database Structure:**
- **Titles** – core dataset containing the title name, type (Movie/TV Show), release year, duration, age rating, and description.  
- **Genres** – list of all unique genres available in the catalog.  
- **Title–Genres Mapping** – relationship table linking each title to one or more genres.  
- **Countries** – list of all countries represented in the dataset.  
- **Title–Countries Mapping** – relationship table linking each title to its production countries.  
- **Credits** – cast and crew information for each title, including directors and lead actors.

---

## Steps Taken

### Data Preparation & Database Setup
- Loaded the original CSV into MySQL.  
- Designed and implemented a **normalized relational database** structure based on an Entity–Relationship Diagram (ERD).  
- Split data into multiple linked tables (`titles`, `genres`, `title_genres`, `countries`, `title_countries`, `credits`).  
- Cleaned and standardized the data:  
  - Removed duplicates and irrelevant records.  
  - Standardized column formats (dates, text casing).  
  - Replaced or removed null values where appropriate.

### SQL Analysis
- Wrote SQL queries to aggregate data by type, genre, country, release year, and rating.  
- Calculated key KPIs such as **% Movies vs % TV Shows**, **Top Genres**, **Top Countries**, **Average Movie Duration**, and **Average TV Show Seasons**.  
- Performed joins and aggregations to prepare datasets for visualization.

### Visualization & Insights
- Connected MySQL database to **Tableau**.  
- Created interactive dashboards including KPI cards, trend charts, geographic maps, and genre/rating breakdowns.  
- Added filters and interactive elements to allow deeper exploration.

---

## Key KPIs

| KPI                                | Value            | Insight                                                                 |
|------------------------------------|------------------|-------------------------------------------------------------------------|
| Movies Share                       | 69.6%            | Movies dominate the catalog, but TV Shows hold a significant share.    |
| TV Shows Share                     | 30.4%            | Indicates strong presence of long-form series content.                  |
| Top Genre                          | International Movies | Reflects Netflix’s focus on global, diverse content.              |
| Top Production Country             | United States    | The US remains the largest content producer, followed by India and UK. |
| Average Movie Duration             | 99 min           | Most movies fall within standard feature-length range.                   |
| Average TV Show Seasons            | 1.8 seasons      | Many TV shows are limited series or short-format productions.           |

---

## Research Questions Addressed

| Research Question                                                                 | Answer / Insight                                                                                          |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Which genres are most frequent on the platform?                                  | *International Movies* and *Dramas* are the leading genres across the catalog.                           |
| How has the ratio of movies to TV shows changed over the years?                  | Movies consistently outnumber TV shows, though the share of TV shows has grown slightly in recent years. |
| How is content distributed by country of production?                             | The US dominates, but India, the UK, and other countries contribute significantly to the catalog.        |
| Which age ratings are most common?                                                | TV-MA and TV-14 are the most frequent, indicating a focus on adult and young adult audiences.            |
| What are the dominant formats in terms of movie duration and number of TV show seasons? | Movies average around 99 minutes; most TV shows have 1–3 seasons, often as limited series.               |

---

## Challenges Faced

### 1. Data Quality Issues  
**Problems:**  
- Missing values in key columns such as `director`, `cast`, and `country`.  
- Duplicate titles appearing across different release years.  
- Inconsistent formats in date and duration fields (e.g., “90 min” vs “1 Season”).  

**Solution:**  
- Standardized text and date formats.  
- Removed duplicates using `title + release_year` as a unique key.  
- Handled missing values with placeholders or by excluding incomplete records when necessary.

---

### 2. Normalizing the Dataset in MySQL  
**Problems:**  
- Original CSV was denormalized, mixing multiple entities in single columns (e.g., multiple countries in one cell).  
- Many-to-many relationships between titles, genres, and countries were not represented.  

**Solution:**  
- Designed an **Entity–Relationship Diagram (ERD)** to model the dataset correctly.  
- Split data into multiple normalized tables (`titles`, `genres`, `countries`, `credits`) and created mapping tables (`title_genres`, `title_countries`).  
- Loaded cleaned data into MySQL for efficient querying.

---

### 3. Querying Across Multiple Tables  
**Problems:**  
- Calculating KPIs like “Top Genre by Country” required complex joins and aggregations.  
- Performance slowed when joining large mapping tables.  

**Solution:**  
- Used optimized SQL queries with indexes on foreign keys.  
- Verified query outputs against Tableau visualizations for consistency.

---

### 4. Connecting MySQL to Tableau  
**Problems:**  
- Tableau connections to MySQL occasionally timed out during large queries.  

**Solution:**  
- Created pre-aggregated tables in MySQL to reduce data transfer.  
- Applied filters and parameters in Tableau to optimize dashboard performance.

---

## Visuals & Dashboard

I created an interactive dashboard in **Tableau** that includes:  
- KPI cards for Movies vs TV Shows share.  
- Genre breakdown with filters for type and release year.  
- Geographic map of top production countries.  
- Trend lines for yearly content releases.  
- Rating distribution across age categories.  
- Average movie duration and average number of TV show seasons.  

File: `netflix_dashboard.twbx`  
(Optional link to Tableau Public can be added)


---

## Final Verdict

Section,Details
- Content,"Maintain strong focus on Movies (dominant share: 69%); 
- Increase TV Show share to capture binge-watch audience; Most TV Shows ≤ 3 seasons create more long-running series to keep viewers engaged;
- Age rating strategy: majority TV-MA & TV-14 (teen & adult viewers);
- Opportunity to expand PG & family-friendly content"
- Genres,"Top genres: International Movies, Dramas, Comedies;
- Invest in high-demand genres like Documentaries & Action/Trends"
- Trends,"Peak growth after 2015 original productions expansion; Seasonal release spikes align marketing with high-output months"

**Recommendation:**  
Continue investing in international productions and maintain a balanced mix of movies and TV shows to cater to diverse audience preferences.

---
The analysis and visualizations were built using the following tools:
	•	Kaggle – source of the original dataset (Netflix Movies & TV Shows)
	•	Slack – communication
	•	Canva – quick design work for presentation assets
	•	Python – data cleaning and transformation (Pandas)
	•	Jupyter Notebook – interactive coding environment for exploration
	•	MySQL – relational database for storing the normalized data and running SQL queries
	•	Tableau – interactive dashboards and visualizations

---


