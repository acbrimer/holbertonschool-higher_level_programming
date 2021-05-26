-- Lists second table ordered by score
SELECT
    t.score
    , t.name
FROM second_table as t
WHERE t.score >= 10
ORDER BY t.score desc;
