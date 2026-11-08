SELECT curso, AVG(notas) as media_curso
FROM alumnos
GROUP BY curso
ORDER BY media_curso DESC;

SELECT id, nombre, max(notas) as maxima_nota
FROM alumnos;

SELECT id, nombre, curso, notas
FROM alumnos
WHERE notas > (SELECT avg(notas) FROM alumnos)
ORDER BY notas DESC;

SELECT curso, count(id) as number_alumnos
FROM alumnos
GROUP BY curso;

SELECT id, nombre, curso, notas
FROM alumnos
ORDER BY notas DESC
LIMIT 3;