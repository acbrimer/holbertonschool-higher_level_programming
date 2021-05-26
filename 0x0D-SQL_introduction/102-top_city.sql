-- Select top 3 cities ordered by avg temp desc
SELECT
*
FROM
(
    SELECT
        t.city
        , AVG(t.value) as avg_temp
    FROM temperatures as t
    WHERE t.month in (8, 9)
    GROUP BY t.city
) as a
ORDER BY a.avg_temp
LIMIT 3;
