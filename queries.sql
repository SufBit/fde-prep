--appointments per provider
SELECT provider, COUNT(*) FROM appointments
GROUP BY provider
ORDER BY COUNT(*) DESC;

--appointments per status
SELECT status, COUNT(*) FROM appointments
GROUP by status
ORDER BY COUNT(*) DESC;

--total minutes per provider for completed appointments
SELECT provider, SUM(minutes), COUNT(*) FROM appointments
WHERE status = 'completed'
GROUP BY provider;

