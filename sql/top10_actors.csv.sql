/*
-- Query: SELECT a.name AS actor, COUNT(*) AS total_titles
FROM show_actors sa
JOIN actors a ON a.id = sa.actor_id
WHERE a.name IS NOT NULL
  AND TRIM(a.name) <> ''
  AND UPPER(TRIM(a.name)) <> 'UNKNOWN'
GROUP BY a.name
ORDER BY total_titles DESC
LIMIT 10
-- Date: 2025-08-14 22:51
*/
INSERT INTO `` (`actor`,`total_titles`) VALUES ('Anupam Kher',43);
INSERT INTO `` (`actor`,`total_titles`) VALUES ('Shah Rukh Khan',35);
INSERT INTO `` (`actor`,`total_titles`) VALUES ('Julie Tejwani',33);
INSERT INTO `` (`actor`,`total_titles`) VALUES ('Takahiro Sakurai',32);
INSERT INTO `` (`actor`,`total_titles`) VALUES ('Naseeruddin Shah',32);
INSERT INTO `` (`actor`,`total_titles`) VALUES ('Rupa Bhimani',31);
INSERT INTO `` (`actor`,`total_titles`) VALUES ('Akshay Kumar',30);
INSERT INTO `` (`actor`,`total_titles`) VALUES ('Om Puri',30);
INSERT INTO `` (`actor`,`total_titles`) VALUES ('Yuki Kaji',29);
INSERT INTO `` (`actor`,`total_titles`) VALUES ('Paresh Rawal',28);
