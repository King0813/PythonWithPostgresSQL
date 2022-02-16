SELECT * FROM moma_works WHERE classification = 'Photograph';

SELECT height, width FROM moma_works
WHERE classification = 'Photograph' AND height > 0 AND width > 0;