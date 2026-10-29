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

--Hourly Provider rate
 SELECT provider, SUM(minutes)/60.0 * hourly_rate
   ...> FROM appointments
   ...> JOIN Providers ON appointments.provider = providers.name
   ...> WHERE status = 'completed'
   ...> GROUP BY provider;


--Row number of appointments per provider ordered by minutes
SELECT id, provider, minutes, ROW_NUMBER() OVER (PARTITION BY provider ORDER BY minutes DESC) AS rank_in_provider
FROM appointments
WHERE status = 'completed';

--Rank of appointments per provider ordered by minutes
SELECT id, provider, minutes, RANK() OVER (PARTITION BY provider ORDER BY minutes DESC) AS rank_in_provider
FROM appointments
WHERE status = 'completed';