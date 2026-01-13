-- =========================
-- DROP Tables
-- =========================
DELETE FROM questions;
DELETE FROM sub_module;
DELETE FROM module;
DELETE FROM programme;


-- =========================
-- Programme
-- =========================
INSERT INTO programme (id, name, created_at)
VALUES
('p1', 'STEP - SRM', NOW(3));

-- =========================
-- Modules
-- =========================
INSERT INTO module (id, programme_id, name, created_at)
VALUES
('m1', 'p1', 'Strings', NOW(3)),
('m2', 'p1', 'Core Java', NOW(3)),
('m3', 'p1', 'Advanced Java', NOW(3));

-- =========================
-- Topics
-- =========================
INSERT INTO sub_module (id, module_id, name, created_at)
VALUES
('sm1', 'm1', 'String Operations', NOW(3)),
('sm2', 'm1', 'String Manipulation & Algorithms', NOW(3)),
('sm3', 'm2', 'Control Flow Statements', NOW(3)),
('sm4', 'm2', 'Object-Oriented Programming', NOW(3)),
('sm5', 'm3', 'Object Class and Its Methods', NOW(3)),
('sm6', 'm2', 'Arrays', NOW(3)),
('sm7', 'm3', 'Design Patterns', NOW(3)),
('sm8', 'm2', 'Threads & Concurrency', NOW(3)),
('sm9', 'm3', 'Inner & Nested Classes', NOW(3));


-- Arpit
INSERT INTO questions (
    id, programme_id, module_id, submodule_id,
    question_type, answer_type, difficulty,
    stem_md, solution_md, score_weight,
    metadata_json, version, is_current, created_at, updated_at
)
VALUES

('q101', 'p1', 'm1', 'sm1',
 'ASSIGNMENT', 'CODE', 'EASY',
 'A chat app needs to display the initials of a user for an avatar. Read a full name as a string and print the first and last character of the name on separate lines.',
 'Read the full name as a String, use charAt(0) for the first character and charAt(length-1) for the last character, then print both.',
 3.00, JSON_OBJECT("tags", "java, strings, accessing-characters, scenario"), 1, TRUE, NOW(3), NOW(3)),

('q102', 'p1', 'm1', 'sm1',
 'SELF', 'CODE', 'EASY',
 'In an online ticket system, each booking id is formed by combining a city code and a numeric sequence (for example BLR + 1052 -> BLR1052). Write a program that reads the city code and the sequence number as separate inputs and combines them into one booking id without using the plus operator for string concatenation.',
 'Store the city code as a String and the sequence number as a String or convert it to String, then use String.concat or a StringBuilder append chain to produce the final booking id.',
 3.00, JSON_OBJECT("tags", "java, strings, concatenation, scenario"), 1, TRUE, NOW(3), NOW(3)),

('q103', 'p1', 'm1', 'sm2',
 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'A warehouse application stores product codes entered by staff with extra spaces and mixed case (for example "  ab-123  "). Write a program that reads a product code and normalises it by trimming spaces at both ends and converting the code to upper case before saving.',
 'Use String.trim to remove leading and trailing spaces and toUpperCase to convert the product code to upper case, then print or return the normalised value.',
 5.00, JSON_OBJECT("tags", "java, strings, trim, toUpperCase, data-cleaning"), 1, TRUE, NOW(3), NOW(3)),

('q104', 'p1', 'm1', 'sm1',
 'SELF', 'CODE', 'MEDIUM',
 'In a log monitoring tool, each log line is represented as a string. Write a program that reads a single log line and checks whether it contains the word "ERROR". If present, print the starting index of the word; otherwise print a message that there is no error.',
 'Use indexOf("ERROR") on the log string. If the result is -1, print that there is no error; otherwise print the index value.',
 5.00, JSON_OBJECT("tags", "java, strings, searching, indexOf, logs"), 1, TRUE, NOW(3), NOW(3)),

('q105', 'p1', 'm1','sm2',
 'ASSIGNMENT', 'CODE', 'HARD',
 'A customer support team wants to analyse how often vowels appear in complaint messages. Write a program that reads a full complaint sentence and counts the total frequency of each vowel (a, e, i, o, u) ignoring case. Print the count for each vowel.',
 'Convert the string to lower case, iterate over all characters, and maintain five counters for a, e, i, o, u. Whenever a vowel is found, increment the relevant counter and finally print all counts.',
 8.00, JSON_OBJECT("tags", "java, strings, counting, frequency, vowels"), 1, TRUE, NOW(3), NOW(3)),

('q106', 'p1', 'm1', 'sm2',
 'SELF', 'CODE', 'HARD',
 'Two different teams have generated coupon codes, and you want to check if two given coupon codes are anagrams of each other (they contain exactly the same characters in possibly different orders). Write a program that reads two strings and prints whether they are anagrams by comparing the frequency of each character.',
 'First check if the lengths match. If they do, either sort both strings and compare, or use an integer frequency array (for example of size 256 or 128) to count characters from the first string and subtract counts using the second string. If all counts are zero at the end, they are anagrams.',
 8.00, JSON_OBJECT("tags", "java, strings, anagram, frequency-count"), 1, TRUE, NOW(3), NOW(3)),

('q107', 'p1', 'm2', 'sm3',
 'ASSIGNMENT', 'CODE', 'EASY',
 'A cinema offers discounts on tickets based on age: below 12 is Child, 12 to 59 is Adult, and 60 or above is Senior. Read the age of a customer and print the category label using if else statements.',
 'Use an if else ladder: if age < 12 then print Child; else if age < 60 then print Adult; else print Senior.',
 3.00, JSON_OBJECT("tags", "java, control-flow, if-else, scenario"), 1, TRUE, NOW(3), NOW(3)),

('q108', 'p1', 'm2', 'sm3',
 'SELF', 'CODE', 'EASY',
 'A learning portal wants to show a multiplication table for a chosen number to help students practise. Read an integer n and display the multiplication table from n x 1 up to n x 10 using a loop.',
 'Use a for loop from 1 to 10 and print the values.',
 3.00, JSON_OBJECT("tags", "java, loops, table"), 1, TRUE, NOW(3), NOW(3)),

('q109', 'p1', 'm2', 'sm3',
 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'A school wants to print a progress chart showing stars for each student based on performance. For 3 students and 3 subjects, print rows using nested loops.',
 'Use nested loops for printing stars per subject for each student.',
 5.00, JSON_OBJECT("tags", "java, nested-loops, patterns"), 1, TRUE, NOW(3), NOW(3)),

('q110', 'p1', 'm2', 'sm4',
 'SELF', 'CODE', 'MEDIUM',
 'A bank needs a simple representation of an account. Create a BankAccount class with fields and methods for deposit, withdraw, and printing details.',
 'Create the class, constructor, and methods; demonstrate usage.',
 5.00, JSON_OBJECT("tags", "java, oops, class-design"), 1, TRUE, NOW(3), NOW(3)),

('q111', 'p1', 'm2', 'sm4',
 'ASSIGNMENT', 'CODE', 'HARD',
 'Create classes Customer and Item and an Order class that computes total cost and prints summary.',
 'Use composition and loops to sum item totals.',
 8.00, JSON_OBJECT("tags", "java, oops, composition, orders"), 1, TRUE, NOW(3), NOW(3)),

('q112', 'p1', 'm2', 'sm6',
 'SELF', 'CODE', 'MEDIUM',
 'A retail store tracks daily sales. Read 7 integers into an array and compute total and average.',
 'Store values in an array and iterate for sum.',
 5.00, JSON_OBJECT("tags", "java, arrays, sum-average"), 1, TRUE, NOW(3), NOW(3)),

('q113', 'p1', 'm2', 'sm6',
 'ASSIGNMENT', 'CODE', 'HARD',
 'An analytics dashboard stores API response times. Read N values and compute min, max, and median.',
 'Use loops for min/max and sort() for median.',
 8.00, JSON_OBJECT("tags", "java, arrays, median, analytics"), 1, TRUE, NOW(3), NOW(3)),

('q114', 'p1', 'm3', 'sm5',
 'SELF', 'CODE', 'EASY',
 'A logging system prints product details. Override toString for readable output.',
 'Override toString in Product class.',
 3.00, JSON_OBJECT("tags", "java, object-class, toString"), 1, TRUE, NOW(3), NOW(3)),

('q115', 'p1', 'm3', 'sm5',
 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'A university portal prevents duplicate Student entries. Override equals and hashCode.',
 'Compare rollNumber in equals and use it in hashCode.',
 5.00, JSON_OBJECT("tags", "java, hashset, equals-hashcode"), 1, TRUE, NOW(3), NOW(3)),

('q116', 'p1', 'm3', 'sm7',
 'SELF', 'CODE', 'MEDIUM',
 'An application must use a single ConfigManager. Implement Singleton.',
 'Private constructor + static instance + getInstance().',
 5.00, JSON_OBJECT("tags", "java, singleton"), 1, TRUE, NOW(3), NOW(3)),

('q117', 'p1', 'm3', 'sm7',
 'ASSIGNMENT', 'CODE', 'HARD',
 'A notification service uses a factory to return Email/SMS/Push implementations.',
 'Implement Notification interface + factory + demo calls.',
 8.00, JSON_OBJECT("tags", "java, factory-pattern"), 1, TRUE, NOW(3), NOW(3)),

('q118', 'p1', 'm3', 'sm9',
 'SELF', 'CODE', 'MEDIUM',
 'A Window class handles button clicks using inner classes. Create a non-static inner handler.',
 'Implement inner class referencing outer fields.',
 5.00, JSON_OBJECT("tags", "java, inner-class, UI"), 1, TRUE, NOW(3), NOW(3)),

('q119', 'p1', 'm3', 'sm9',
 'ASSIGNMENT', 'CODE', 'HARD',
 'Implement a Builder pattern inside ApplicationConfig.',
 'Use static nested Builder with chained methods.',
 8.00, JSON_OBJECT("tags", "java, builder, immutability"), 1, TRUE, NOW(3), NOW(3)),

('q120', 'p1', 'm3', 'sm7',
 'SELF', 'CODE', 'HARD',
 'A shopping platform supports multiple payment strategies. Implement the Strategy pattern.',
 'Create interface, strategies, and OrderProcessor.',
 8.00, JSON_OBJECT("tags", "java, strategy-pattern"), 1, TRUE, NOW(3), NOW(3)),



--  sam
('q1','p1','m1','sm1','ASSIGNMENT','CODE','MEDIUM',
 'Your junior teammate is debugging an application where the username characters must be checked one-by-one. Write a program that prints each character of a string individually.',
 'Use a loop with charAt() or convert to char array.',5.00,
 JSON_OBJECT("scenario","debugging username validation"),1,TRUE,NOW(3),NOW(3)),

('q2','p1','m1','sm1','SELF','CODE','EASY',
 'During onboarding, HR gives you two strings for first & last name. Combine them without using the + operator.',
 'Use StringBuilder or concat.',3.00,
 JSON_OBJECT("scenario","joining employee names"),1,TRUE,NOW(3),NOW(3)),

('q3','p1','m2','sm3','ASSIGNMENT','CODE','MEDIUM',
 'In a loan approval module, applicants are filtered with multiple conditions. Demonstrate conditional flows.',
 'Use multiple if/else + switch.',5.00,
 JSON_OBJECT("scenario","loan approval logic"),1,TRUE,NOW(3),NOW(3)),

('q4','p1','m2','sm3','SELF','CODE','MEDIUM',
 'Your team needs a module that prints patterns and sequences for dashboards. Demonstrate loops.',
 'Use for, while, do-while.',5.00,
 JSON_OBJECT("scenario","training dashboard loops"),1,TRUE,NOW(3),NOW(3)),

('q5','p1','m1','sm1','SELF','CODE','EASY',
 'Extract first and last characters from user input.',
 'Use charAt.',3.00,
 JSON_OBJECT("scenario","text processing utility"),1,TRUE,NOW(3),NOW(3)),

('q6','p1','m1','sm2','ASSIGNMENT','CODE','MEDIUM',
 'Marketing wants keywords merged into a tagline. Join an array of words into a sentence.',
 'Use String.join or StringBuilder.',4.00,
 JSON_OBJECT("scenario","marketing tagline generator"),1,TRUE,NOW(3),NOW(3)),

('q7','p1','m1','sm2','SELF','CODE','EASY',
 'A legacy API returns reversed IDs. Reverse them.',
 'Loop from end to start.',4.00,
 JSON_OBJECT("scenario","reverse legacy IDs"),1,TRUE,NOW(3),NOW(3)),

('q8','p1','m1','sm2','ASSIGNMENT','CODE','MEDIUM',
 'Fraud detection system checks for suspicious substring.',
 'Use contains or indexOf.',5.00,
 JSON_OBJECT("scenario","fraud pattern detection"),1,TRUE,NOW(3),NOW(3)),

('q9','p1','m1','sm2','SELF','CODE','EASY',
 'Email spam analyzer counts character frequency.',
 'Loop & count.',3.00,
 JSON_OBJECT("scenario","spam analyzer frequency"),1,TRUE,NOW(3),NOW(3)),

('q10','p1','m2','sm3','ASSIGNMENT','CODE','EASY',
 'Billing system assigns tier based on even/odd reading.',
 'Use % operator.',3.00,
 JSON_OBJECT("scenario","billing tier classification"),1,TRUE,NOW(3),NOW(3)),

('q11','p1','m2','sm3','SELF','CODE','MEDIUM',
 'Batch processor prints multiplication tables.',
 'Use loop.',5.00,
 JSON_OBJECT("scenario","QA batch checks"),1,TRUE,NOW(3),NOW(3)),

('q12','p1','m2','sm3','ASSIGNMENT','CODE','HARD',
 'UI template engine needs star patterns.',
 'Use nested loops.',6.00,
 JSON_OBJECT("scenario","UI onboarding visual patterns"),1,TRUE,NOW(3),NOW(3)),

('q13','p1','m2','sm4','SELF','CODE','MEDIUM',
 'Create an Order class with fields and methods.',
 'Model class with constructor and methods.',5.00,
 JSON_OBJECT("scenario","online order modelling"),1,TRUE,NOW(3),NOW(3)),

('q14','p1','m2','sm4','ASSIGNMENT','CODE','HARD',
 'Extend Employee class and override methods.',
 'Use inheritance + overriding.',6.00,
 JSON_OBJECT("scenario","employee role hierarchy"),1,TRUE,NOW(3),NOW(3)),

('q15','p1','m3','sm5','SELF','CODE','EASY',
 'Debugging tool needs list of methods.',
 'Use getMethods().',4.00,
 JSON_OBJECT("scenario","class inspector"),1,TRUE,NOW(3),NOW(3)),

('q16','p1','m3','sm5','ASSIGNMENT','CODE','MEDIUM',
 'CRM prevents duplicate students. Override equals & hashCode.',
 'Compare rollNumber.',5.00,
 JSON_OBJECT("scenario","duplicate customer prevention"),1,TRUE,NOW(3),NOW(3)),

('q17','p1','m3','sm7','SELF','CODE','MEDIUM',
 'Implement ConfigService Singleton.',
 'Private constructor + static instance.',5.00,
 JSON_OBJECT("scenario","config service singleton"),1,TRUE,NOW(3),NOW(3)),

('q18','p1','m3','sm7','ASSIGNMENT','CODE','HARD',
 'Factory Pattern for multiple file exporters.',
 'Interface + concrete classes.',7.00,
 JSON_OBJECT("scenario","file exporter factory"),1,TRUE,NOW(3),NOW(3)),

('q19','p1','m3','sm9','SELF','CODE','MEDIUM',
 'Inner class must access event properties.',
 'Define inner class.',5.00,
 JSON_OBJECT("scenario","event logging inner class"),1,TRUE,NOW(3),NOW(3)),

('q20','p1','m3','sm9','ASSIGNMENT','CODE','HARD',
 'Nested classes for UI callbacks.',
 'Use static + anonymous classes.',6.00,
 JSON_OBJECT("scenario","callback handlers"),1,TRUE,NOW(3),NOW(3)),

('q21','p1','m2','sm6','SELF','CODE','EASY',
 'Analytics engine needs max in array.',
 'Loop to find max.',3.00,
 JSON_OBJECT("scenario","analytics max finder"),1,TRUE,NOW(3),NOW(3)),

('q22','p1','m2','sm6','ASSIGNMENT','CODE','MEDIUM',
 'Inventory must be sorted without built-in sort().',
 'Use bubble/selection sort.',5.00,
 JSON_OBJECT("scenario","inventory sorter"),1,TRUE,NOW(3),NOW(3)),

('q23','p1','m2','sm6','SELF','CODE','HARD',
 'Search system needs binary search.',
 'Implement binary search.',6.00,
 JSON_OBJECT("scenario","search optimization"),1,TRUE,NOW(3),NOW(3)),

('q24','p1','m3','sm5','SELF','CODE','EASY',
 'Logging system wants readable object output.',
 'Override toString.',3.00,
 JSON_OBJECT("scenario","logging printer"),1,TRUE,NOW(3),NOW(3)),

('q25','p1','m3','sm7','ASSIGNMENT','CODE','MEDIUM',
 'Explain difference between interface & abstract class.',
 'Implement both + override.',6.00,
 JSON_OBJECT("scenario","learning platform OOP module"),1,TRUE,NOW(3),NOW(3)),

('q26','p1','m1','sm2','SELF','CODE','MEDIUM',
 'Customer IDs must be validated for palindrome.',
 'Reverse & compare.',5.00,
 JSON_OBJECT("scenario","customer id validator"),1,TRUE,NOW(3),NOW(3)),

('q27','p1','m2','sm3','ASSIGNMENT','CODE','HARD',
 'Dashboard needs Fibonacci sequence.',
 'Generate using loops.',5.00,
 JSON_OBJECT("scenario","dashboard fibonacci widget"),1,TRUE,NOW(3),NOW(3)),

('q28','p1','m2','sm4','SELF','CODE','EASY',
 'Demonstrate constructor overloading.',
 'Write multiple constructors.',4.00,
 JSON_OBJECT("scenario","registration model constructors"),1,TRUE,NOW(3),NOW(3)),

('q30','p1','m3','sm9','SELF','CODE','MEDIUM',
 'GUI uses anonymous classes for events.',
 'Implement anonymous classes.',5.00,
 JSON_OBJECT("scenario","GUI event handlers"),1,TRUE,NOW(3),NOW(3));
