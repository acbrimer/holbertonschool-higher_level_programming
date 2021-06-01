-- Lists all genres not assosciated with Dexter
SELECT
    g.name
FROM tv_genres AS g
WHERE g.id NOT IN (
    SELECT 
        sg.genre_id
    FROM tv_shows AS s
    INNER JOIN tv_show_genres AS sg
        ON s.id = sg.show_id
    WHERE s.title = 'Dexter'
)
ORDER BY g.name;
