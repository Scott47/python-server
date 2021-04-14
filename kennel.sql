SELECT a.name, l.name as 'location_name'
FROM Location l
JOIN Animal a ON a.location_id = l.id;


