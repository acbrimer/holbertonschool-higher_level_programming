-- Get max temps
SELECT
    t.state
    , m.max_temp
FROM temperatures as t
INNER JOIN (
    SELECT
        MAX(ti.value) as max_temp
    FROM temperatures as ti
) as m
    ON t.value = m.max_temp
ORDER BY t.state;
