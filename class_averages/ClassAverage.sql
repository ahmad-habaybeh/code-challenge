CREATE TABLE `class` (
  `identifier` varchar(5) NOT NULL,
  `location` varchar(20) DEFAULT NULL,
  `school` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`identifier`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `students` (
  `identifier` varchar(5) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `score` decimal(8,2) DEFAULT NULL,
  `class_identifier` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`identifier`),
  KEY `classfk_idx` (`class_identifier`),
  CONSTRAINT `classfk` FOREIGN KEY (`class_identifier`) REFERENCES `class` (`identifier`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

------------------------------------------------------------------
INSERT INTO `class` (`identifier`,`location`,`school`) VALUES ('122','Dtown','boys');
INSERT INTO `class` (`identifier`,`location`,`school`) VALUES ('133','Uptown','girls');

--------------------------------------------------------------------------
INSERT INTO `students` (`identifier`,`name`,`score`,`class_identifier`) VALUES ('1111','name1',98.00,'122');
INSERT INTO `students` (`identifier`,`name`,`score`,`class_identifier`) VALUES ('1222','name2',65.00,'122');
INSERT INTO `students` (`identifier`,`name`,`score`,`class_identifier`) VALUES ('22222','name8',80.00,'122');
INSERT INTO `students` (`identifier`,`name`,`score`,`class_identifier`) VALUES ('3333','name3',98.00,'122');
INSERT INTO `students` (`identifier`,`name`,`score`,`class_identifier`) VALUES ('4444','name6',98.00,'122');
INSERT INTO `students` (`identifier`,`name`,`score`,`class_identifier`) VALUES ('45454','name88',66.00,'133');
INSERT INTO `students` (`identifier`,`name`,`score`,`class_identifier`) VALUES ('65656','name5',34.00,'133');
INSERT INTO `students` (`identifier`,`name`,`score`,`class_identifier`) VALUES ('6666','name09',78.00,'133');

-----------------------------------------------------------------------------
-- 1- How many students are in each school?
SELECT 
    b.school, COUNT(0) students_count
FROM
    students a,
    class b
WHERE
    a.class_identifier = b.identifier
GROUP BY b.school;

-- 2.What is the highest, lowest and average score for EACH school?
SELECT 
    b.school,
    MAX(a.score) highest_score,
    MIN(a.score) min_score,
    AVG(a.score) average_score
FROM
    students a,
    class b
WHERE
    a.class_identifier = b.identifier
GROUP BY b.school;

-- 3.What is the highest, lowest and average score for ALL the schools?
SELECT 
    MAX(a.score) highest_score,
    MIN(a.score) min_score,
    AVG(a.score) average_score
FROM
    students a,
    class b
WHERE
    a.class_identifier = b.identifier;

-- 4. What school has the highest score, and what is the highest score?
SELECT 
    b.school, MAX(a.score) highest_score
FROM
    students a,
    class b
WHERE
    a.class_identifier = b.identifier
GROUP BY b.school
HAVING MAX(a.score) = (SELECT 
        MAX(a1.score)
    FROM
        students a1,
        class b1
    WHERE
        a1.class_identifier = b1.identifier);


-- 5. What schools has the lowest score, and what si the lowest score?
SELECT 
    b.school, MIN(a.score) min_score
FROM
    students a,
    class b
WHERE
    a.class_identifier = b.identifier
    group by b.school
HAVING MIN(a.score) = (SELECT 
        MIN(a1.score)
    FROM
        students a1,
        class b1
    WHERE
        a1.class_identifier = b1.identifier);