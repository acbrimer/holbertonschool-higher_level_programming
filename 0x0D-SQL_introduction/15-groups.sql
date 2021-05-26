-- Histogram of scores
SELECT
    t.score
    , COUNT(t.id) as "number"
FROM second_table as t
GROUP BY t.score;
