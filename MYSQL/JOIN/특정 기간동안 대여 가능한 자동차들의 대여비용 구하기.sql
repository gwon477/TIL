-- https://school.programmers.co.kr/learn/courses/30/lessons/157339

WITH CAN AS (
    SELECT DISTINCT car_id
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS CRH
    WHERE NOT EXISTS (
        SELECT *
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS R
        WHERE R.CAR_ID = CRH.CAR_ID
        AND R.START_DATE <= '2022-11-30'
        AND R.END_DATE >= '2022-11-01'
    )
), AAA AS (
    SELECT car_id, car_type, daily_fee
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE car_id IN (SELECT car_id FROM CAN) AND (car_type='SUV' OR car_type='세단')
), DDD AS (
    SELECT car_type, discount_rate
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    WHERE (car_type='세단' OR car_type='SUV') AND DURATION_TYPE='30일 이상'
), FFF AS (
    SELECT AAA.car_id AS car_id, AAA.car_type AS car_type, 
           ROUND(AAA.daily_fee * (1 - DDD.discount_rate * 0.01) * 30, 0) AS fee
    FROM AAA 
    JOIN DDD ON AAA.car_type = DDD.car_type
)

SELECT * 
FROM FFF
WHERE fee >= 500000 AND fee < 2000000
ORDER BY fee DESC, car_type ASC, car_id DESC;