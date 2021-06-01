-- Gets cities with state names
SELECT
    c.id
    , c.name
    , s.name
FROM states AS s
INNER JOIN cities as c
    ON s.id = c.state_id
