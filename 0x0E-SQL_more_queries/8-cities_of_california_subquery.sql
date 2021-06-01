-- Selects cities where state_id = cali
SELECT
    c.id
    , c.state_id
    , c.name
FROM cities AS c
    WHERE c.state_id = (SELECT s.id FROM states AS s WHERE s.name = 'California' LIMIT 1)
