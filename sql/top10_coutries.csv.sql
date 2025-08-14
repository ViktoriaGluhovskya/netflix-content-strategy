/*
-- Query: SELECT 
  c.name AS country,
  COUNT(*) AS total_titles
FROM show_countries sc
JOIN countries c ON c.id = sc.country_id
JOIN shows s ON s.id = sc.show_id
WHERE c.name IS NOT NULL
  AND TRIM(c.name) <> ''
  AND UPPER(TRIM(c.name)) <> 'UNKNOWN'
GROUP BY c.name
ORDER BY total_titles DESC
LIMIT 10
-- Date: 2025-08-14 22:56
*/
INSERT INTO `` (`country`,`total_titles`) VALUES ('United States',3690);
INSERT INTO `` (`country`,`total_titles`) VALUES ('India',1046);
INSERT INTO `` (`country`,`total_titles`) VALUES ('United Kingdom',806);
INSERT INTO `` (`country`,`total_titles`) VALUES ('Canada',445);
INSERT INTO `` (`country`,`total_titles`) VALUES ('France',393);
INSERT INTO `` (`country`,`total_titles`) VALUES ('Japan',318);
INSERT INTO `` (`country`,`total_titles`) VALUES ('Spain',232);
INSERT INTO `` (`country`,`total_titles`) VALUES ('South Korea',231);
INSERT INTO `` (`country`,`total_titles`) VALUES ('Germany',226);
INSERT INTO `` (`country`,`total_titles`) VALUES ('Mexico',169);
