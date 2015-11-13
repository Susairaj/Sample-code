SELECT *
FROM (
SELECT * FROM one.tbl_test t1
UNION ALL
SELECT * FROM two.tbl_test t2
) tbl
GROUP BY sno
HAVING count(*) = 1
ORDER BY sno