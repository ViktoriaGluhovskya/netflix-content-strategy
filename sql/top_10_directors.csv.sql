/*
-- Query: SELECT d.name AS director, COUNT(*) AS total_directed
FROM show_directors sd
JOIN directors d ON sd.director_id = d.id
GROUP BY d.name
ORDER BY total_directed DESC
LIMIT 11
-- Date: 2025-08-14 22:44
*/
INSERT INTO `` (`director`,`total_directed`) VALUES ('Unknown',2634);
INSERT INTO `` (`director`,`total_directed`) VALUES ('Rajiv Chilaka',22);
INSERT INTO `` (`director`,`total_directed`) VALUES ('Jan Suter',21);
INSERT INTO `` (`director`,`total_directed`) VALUES ('Raúl Campos',19);
INSERT INTO `` (`director`,`total_directed`) VALUES ('Suhas Kadav',16);
INSERT INTO `` (`director`,`total_directed`) VALUES ('Marcus Raboy',16);
INSERT INTO `` (`director`,`total_directed`) VALUES ('Jay Karas',15);
INSERT INTO `` (`director`,`total_directed`) VALUES ('Cathy Garcia-Molina',13);
INSERT INTO `` (`director`,`total_directed`) VALUES ('Jay Chapman',12);
INSERT INTO `` (`director`,`total_directed`) VALUES ('Martin Scorsese',12);
INSERT INTO `` (`director`,`total_directed`) VALUES ('Youssef Chahine',12);
