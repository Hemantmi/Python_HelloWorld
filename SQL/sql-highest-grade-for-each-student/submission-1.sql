-- Write your query below


SELECT student_id,exam_id,score
FROM (
SELECT *, ROW_NUMBER() over (PARTITION BY student_id order by score desc, exam_id asc) as rownum
FROM exam_results
)
where rownum=1
order by student_id asc