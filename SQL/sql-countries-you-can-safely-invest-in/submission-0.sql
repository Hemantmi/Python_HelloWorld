SELECT
    co.name AS country
FROM Person p
JOIN Country co
    ON LEFT(p.phone_number, 3) = co.country_code
JOIN Calls c
    ON p.id = c.caller_id
    OR p.id = c.callee_id
GROUP BY co.name
HAVING AVG(c.duration) > (
    SELECT AVG(duration)
    FROM Calls
);