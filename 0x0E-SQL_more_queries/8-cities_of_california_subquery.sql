-- Selects cities where state_id = cali
SELECT
    c.id
    , c.state_id
    , c.name
FROM hbtn_0d_usa.cities as c
    WHERE c.state_id = (SELECT s.id FROM hbtn_0d_usa.states as s WHERE s.name = 'California' LIMIT 1)
