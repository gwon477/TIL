WITH OP AS(
    SELECT ID,CREATOR, 0 AS LIKES
    FROM OLD_POSTS
)

SELECT * FROM OP 
UNION
SELECT * FROM NEW_POSTS
ORDER BY ID DESC