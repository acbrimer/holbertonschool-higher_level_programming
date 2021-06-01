-- Lists all shows without comedy genre
SELECT
    s.title
FROM tv_shows AS s
WHERE s.id NOT IN (
    SELECT
        sg.show_id
    FROM tv_geners AS g
    INNER JOIN tv_show_genres AS sg
        ON g.id = sg.genre_id
    WHERE g.name = 'Comedy'
)
ORDER BY s.title;
