SELECT 
    s.show_id,
    s.title,
    s.type,
    s.release_year,
    s.duration,
    s.rating,
    COALESCE(GROUP_CONCAT(DISTINCT g.name ORDER BY g.name SEPARATOR ', '), '') AS genres,
    COALESCE(GROUP_CONCAT(DISTINCT c.name ORDER BY c.name SEPARATOR ', '), '') AS countries
FROM shows s
LEFT JOIN show_genres    sg ON sg.show_id   = s.show_id
LEFT JOIN genres         g  ON g.genre_id   = sg.genre_id
LEFT JOIN show_countries sc ON sc.show_id   = s.show_id
LEFT JOIN countries      c  ON c.country_id = sc.country_id
GROUP BY s.show_id, s.title, s.type, s.release_year, s.duration, s.rating
ORDER BY s.release_year DESC;

DESCRIBE countries;
DESCRIBE show_countries;

LEFT JOIN countries c ON c.country_id = sc.country_id
