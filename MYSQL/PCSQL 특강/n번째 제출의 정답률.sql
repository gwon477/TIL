WITH Submission_Order AS (
    -- 각 제출에 대해 제출 순서 번호를 부여합니다.
    SELECT S.USER_ID, S.PROBLEM_ID, S.SUBMITTED, S.TIMESTAMP, 
    ROW_NUMBER() OVER (PARTITION BY S.USER_ID, S.PROBLEM_ID ORDER BY S.TIMESTAMP) AS NTH_SUBMISSION
    FROM SUBMISSIONS S
), Correct_Check AS (
    -- 각 제출에 대해 정답 여부를 확인합니다.
    SELECT SO.NTH_SUBMISSION,
        CASE 
            WHEN SO.SUBMITTED = P.CORRECT_ANSWER THEN 1
            ELSE 0
        END AS IS_CORRECT
    FROM Submission_Order AS SO JOIN PROBLEMS AS P ON SO.PROBLEM_ID = P.PROBLEM_ID
), Correct_Rate AS (
    -- 각 제출 순서별로 정답률을 계산합니다.
    SELECT NTH_SUBMISSION, ROUND(AVG(IS_CORRECT) * 100,0) AS CORRECT_RATE
    FROM Correct_Check
    GROUP BY NTH_SUBMISSION
)

-- 제출 순서와 정답률을 출력합니다.
SELECT NTH_SUBMISSION, CORRECT_RATE
FROM Correct_Rate
ORDER BY NTH_SUBMISSION;