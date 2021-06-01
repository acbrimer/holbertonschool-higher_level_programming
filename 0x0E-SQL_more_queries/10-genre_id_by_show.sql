-- Gets tv shows w/ at least 1 genre in n-n join
SELECT
    s.title
    , g.genre_id
FROM tv_shows AS s
INNER JOIN tv_show_genres AS g
    ON s.id = g.show_id
ORDER BY s.title, g.genre_id
