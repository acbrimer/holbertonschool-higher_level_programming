-- Select top 3 cities ordered by avg temp desc
SELECT
*
FROM
(
    SELECT
        t.city
        , AVG(t.value) as avg_temp
    FROM temperatures as t
    GROUP BY t.city
    ORDER BY avg_temp desc
) as a
LIMIT 3;
