-- Counts shows by genre
SELECT
    g.name AS genre
    , COUNT(sg.show_id) AS number_of_shows
FROM tv_show_genres AS sg
INNER JOIN tv_genres AS g
    ON sg.genre_id = g.id
GROUP BY g.name
ORDER BY number_of_shows DESC;
