-- Lists second table ordered by score
SELECT
    t.score
    , t.name
FROM second_table as t
ORDER BY t.score desc;
