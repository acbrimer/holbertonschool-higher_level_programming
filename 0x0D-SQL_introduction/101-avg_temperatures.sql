-- Select cities ordered by avg temp desc
SELECT
    t.city
    , AVG(t.value) as "avg_temp"
FROM temperatures as t
GROUP BY t.city
ORDER BY "avg_temp" desc;
