-- Select from second table
SELECT
    t.score
    , t.name
FROM second_table as t
WHERE t.name is not null
ORDER BY t.score desc;
