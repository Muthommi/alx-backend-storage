-- SQL script to rank country origin of bands
-- Group bands by origin and sum the number for each country

SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
