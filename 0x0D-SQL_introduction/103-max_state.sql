-- Get max temps
SELECT
    t.state
    , MAX(t.value) as max_temp
FROM temperatures as t
GROUP BY t.state
ORDER BY t.state;
