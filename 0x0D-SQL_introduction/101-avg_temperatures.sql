-- Select cities ordered by avg temp desc

SELECT
    i.city
    , i.avg_temp
FROM 
(
    SELECT DISTINCT
        t.city
        , AVG(t.value) as avg_temp
    FROM temperatures as t
    GROUP BY t.city
) as i
ORDER BY i.avg_temp desc;
