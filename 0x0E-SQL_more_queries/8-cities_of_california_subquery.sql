-- Selects cities where state_id = cali
SELECT
    c.id
    , c.state_id
    , c.name
FROM cities AS c
    WHERE c.state_id IN (SELECT s.id FROM states AS s WHERE s.name = 'California')
