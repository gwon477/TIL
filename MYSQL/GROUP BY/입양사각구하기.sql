WITH RECURSIVE TI (num) AS (
    SELECT 0
    UNION ALL
    SELECT num + 1 FROM TI
    WHERE num < 23
), AA AS(
    SELECT COUNT(ANIMAL_ID) AS COUNT, DATE_FORMAT(DATETIME, '%H') AS HOUR
    FROM ANIMAL_OUTS
    GROUP BY HOUR
)

SELECT num AS HOUT, IFNULL(COUNT,0) AS COUNT
FROM TI LEFT OUTER JOIN AA ON TI.num = AA.HOUR