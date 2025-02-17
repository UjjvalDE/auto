SELECT user_id, COUNT(*) as trip_count 
FROM Trips 
WHERE start_location NOT LIKE '%,%' AND end_location NOT LIKE '%,%' 
GROUP BY user_id ORDER BY trip_count DESC;