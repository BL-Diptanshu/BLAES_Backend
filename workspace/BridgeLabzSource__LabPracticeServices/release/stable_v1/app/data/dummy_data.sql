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
INSERT INTO topic (id, module_id, name, created_at)
VALUES
('t1', 'm1', 'String Operations', NOW(3)),
('t2', 'm1', 'String Manipulation & Algorithms', NOW(3)),
('t3', 'm2', 'Control Flow Statements', NOW(3)),
('t4', 'm2', 'Object-Oriented Programming', NOW(3)),
('t5', 'm3', 'Object Class and Its Methods', NOW(3)),
('t6', 'm2', 'Arrays', NOW(3)),
('t7', 'm3', 'Design Patterns', NOW(3)),
('t8', 'm2', 'Threads & Concurrency', NOW(3)),
('t9', 'm3', 'Inner & Nested Classes', NOW(3));

-- =========================
-- Subtopics
-- =========================
INSERT INTO subtopic (id, topic_id, name, created_at)
VALUES
('s1', 't1', 'Accessing Characters', NOW(3)),
('s2', 't1', 'Concatenation', NOW(3)),
('s3', 't2', 'Basic String Manipulations', NOW(3)),
('s4', 't2', 'Searching & Matching', NOW(3)),
('s5', 't2', 'Counting & Frequency', NOW(3)),
('s6', 't3', 'Conditional Statements', NOW(3)),
('s7', 't3', 'Looping Statements', NOW(3)),
('s8', 't3', 'Nested and Complex Control Flows', NOW(3)),
('s9', 't4', 'Classes and Objects', NOW(3)),
('s10','t6','Array Manipulations', NOW(3)),
('s11','t5','Object Class Methods', NOW(3)),
('s12','t7','Singleton & Factory Patterns', NOW(3)),
('s13','t9','Nested & Inner Classes Usage', NOW(3));

-- =========================
-- Questions
-- =========================
-- INSERT INTO questions (
--     id, programme_id, module_id, topic_id, subtopic_id,
--     question_type, answer_type, difficulty,
--     stem_md, solution_md, score_weight,
--     metadata_json, version, is_current, created_at, updated_at
-- )
-- VALUES
-- ('q1', 'p1', 'm1', 't1', 's1', 'ASSIGNMENT', 'CODE', 'MEDIUM',
--  'Print each character of a string individually.',
--  'Use charAt() or toCharArray() in a loop.', 5.00, JSON_OBJECT("tags", "java, strings, charAt"), 1, TRUE, NOW(3), NOW(3)),

-- ('q2', 'p1', 'm1', 't1', 's2', 'SELF', 'CODE', 'EASY',
--  'Concatenate two strings without using + operator.',
--  'Use StringBuilder or String.concat().', 3.00, JSON_OBJECT("tags", "java, strings, concat"), 1, TRUE, NOW(3), NOW(3)),

-- ('q3', 'p1', 'm2', 't3', 's6', 'ASSIGNMENT', 'CODE', 'MEDIUM',
--  'Demonstrate if-else and switch statements.',
--  'Implement multiple conditions.', 5.00, JSON_OBJECT("tags", "java, core-java, conditional"), 1, TRUE, NOW(3), NOW(3)),

-- ('q4', 'p1', 'm2', 't3', 's7', 'SELF', 'CODE', 'MEDIUM',
--  'Use for, while, and do-while loops.',
--  'Print numbers, sum of numbers, and patterns.', 5.00, JSON_OBJECT("tags", "java, core-java, loops"), 1, TRUE, NOW(3), NOW(3));

-- =========================
-- Additional 50 Randomly Distributed Questions
-- =========================

-- INSERT INTO questions (
--     id, programme_id, module_id, topic_id, subtopic_id,
--     question_type, answer_type, difficulty,
--     stem_md, solution_md, score_weight,
--     metadata_json, version, is_current, created_at, updated_at
-- )
-- VALUES
-- ('q5', 'p1', 'm1', 't1', 's1', 'SELF', 'CODE', 'EASY',
--  'Find the first and last character of a string.',
--  'Use charAt(0) and charAt(length-1).', 3.00, JSON_OBJECT("tags", "java, strings, basics"), 1, TRUE, NOW(3), NOW(3)),

-- ('q6', 'p1', 'm1', 't1', 's2', 'ASSIGNMENT', 'CODE', 'MEDIUM',
--  'Join an array of words into a single sentence.',
--  'Use String.join() or StringBuilder.', 4.00, JSON_OBJECT("tags", "java, stringbuilder, join"), 1, TRUE, NOW(3), NOW(3)),

-- ('q7', 'p1', 'm1', 't2', 's3', 'SELF', 'CODE', 'EASY',
--  'Reverse a string without using built-in reverse().',
--  'Iterate from end to start and append characters.', 4.00, JSON_OBJECT("tags", "java, reverse, strings"), 1, TRUE, NOW(3), NOW(3)),

-- ('q8', 'p1', 'm1', 't2', 's4', 'ASSIGNMENT', 'CODE', 'MEDIUM',
--  'Check if a string contains a particular substring.',
--  'Use contains() or indexOf().', 5.00, JSON_OBJECT("tags", "java, substring, search"), 1, TRUE, NOW(3), NOW(3)),

-- ('q9', 'p1', 'm1', 't2', 's5', 'SELF', 'CODE', 'EASY',
--  'Count occurrences of a character in a string.',
--  'Loop through and increment counter for matches.', 3.00, JSON_OBJECT("tags", "java, counting, loops"), 1, TRUE, NOW(3), NOW(3)),

-- ('q10', 'p1', 'm2', 't3', 's6', 'ASSIGNMENT', 'CODE', 'EASY',
--  'Check if a number is even or odd using if-else.',
--  'Use modulus operator (%).', 3.00, JSON_OBJECT("tags", "java, conditional, basics"), 1, TRUE, NOW(3), NOW(3)),

-- ('q11', 'p1', 'm2', 't3', 's7', 'SELF', 'CODE', 'MEDIUM',
--  'Print multiplication table using for loop.',
--  'Use nested loops for multiple tables.', 5.00, JSON_OBJECT("tags", "java, loops, core"), 1, TRUE, NOW(3), NOW(3)),

-- ('q12', 'p1', 'm2', 't3', 's8', 'ASSIGNMENT', 'CODE', 'HARD',
--  'Implement a pattern program using nested loops.',
--  'Use nested for loops and string concatenation.', 6.00, JSON_OBJECT("tags", "java, patterns, nested-loops"), 1, TRUE, NOW(3), NOW(3)),

-- ('q13', 'p1', 'm2', 't4', 's9', 'SELF', 'CODE', 'MEDIUM',
--  'Create a simple class with attributes and methods.',
--  'Define class, fields, constructors, and methods.', 5.00, JSON_OBJECT("tags", "java, oops, class"), 1, TRUE, NOW(3), NOW(3)),

-- ('q14', 'p1', 'm2', 't4', 's9', 'ASSIGNMENT', 'CODE', 'HARD',
--  'Demonstrate inheritance and method overriding.',
--  'Use extends keyword and override parent method.', 6.00, JSON_OBJECT("tags", "java, inheritance, oops"), 1, TRUE, NOW(3), NOW(3)),

-- ('q15', 'p1', 'm3', 't5', 's11', 'SELF', 'CODE', 'EASY',
--  'Display all methods of Object class.',
--  'Use getClass().getMethods().', 4.00, JSON_OBJECT("tags", "java, reflection, objectclass"), 1, TRUE, NOW(3), NOW(3)),

-- ('q16', 'p1', 'm3', 't5', 's11', 'ASSIGNMENT', 'CODE', 'MEDIUM',
--  'Demonstrate the use of equals() and hashCode().',
--  'Override both in a custom class.', 5.00, JSON_OBJECT("tags", "java, objectclass, equals"), 1, TRUE, NOW(3), NOW(3)),

-- ('q17', 'p1', 'm3', 't7', 's12', 'SELF', 'CODE', 'MEDIUM',
--  'Implement a Singleton class.',
--  'Use private constructor and static instance.', 5.00, JSON_OBJECT("tags", "java, singleton, designpattern"), 1, TRUE, NOW(3), NOW(3)),

-- ('q18', 'p1', 'm3', 't7', 's12', 'ASSIGNMENT', 'CODE', 'HARD',
--  'Demonstrate Factory Pattern with multiple classes.',
--  'Use abstract class or interface with concrete implementations.', 7.00, JSON_OBJECT("tags", "java, factory, designpattern"), 1, TRUE, NOW(3), NOW(3)),

-- ('q19', 'p1', 'm3', 't9', 's13', 'SELF', 'CODE', 'MEDIUM',
--  'Create an inner class that accesses outer class variables.',
--  'Define inner class and demonstrate access.', 5.00, JSON_OBJECT("tags", "java, innerclass, advancedjava"), 1, TRUE, NOW(3), NOW(3)),

-- ('q20', 'p1', 'm3', 't9', 's13', 'ASSIGNMENT', 'CODE', 'HARD',
--  'Demonstrate static nested classes and anonymous classes.',
--  'Use static and anonymous inner class syntax.', 6.00, JSON_OBJECT("tags", "java, nestedclass, advancedjava"), 1, TRUE, NOW(3), NOW(3)),

-- ('q21', 'p1', 'm2', 't6', 's10', 'SELF', 'CODE', 'EASY',
--  'Find maximum element in an array.',
--  'Loop through array and track largest element.', 3.00, JSON_OBJECT("tags", "java, array, basics"), 1, TRUE, NOW(3), NOW(3)),

-- ('q22', 'p1', 'm2', 't6', 's10', 'ASSIGNMENT', 'CODE', 'MEDIUM',
--  'Sort an array without using sort().',
--  'Use bubble sort or selection sort algorithm.', 5.00, JSON_OBJECT("tags", "java, sorting, array"), 1, TRUE, NOW(3), NOW(3)),

-- ('q23', 'p1', 'm2', 't6', 's10', 'SELF', 'CODE', 'HARD',
--  'Implement binary search on sorted array.',
--  'Use mid-point comparison and recursion.', 6.00, JSON_OBJECT("tags", "java, binarysearch, array"), 1, TRUE, NOW(3), NOW(3)),

-- ('q24', 'p1', 'm3', 't5', 's11', 'SELF', 'CODE', 'EASY',
--  'Use toString() method in a class.',
--  'Override toString() and print details.', 3.00, JSON_OBJECT("tags", "java, tostring, objectclass"), 1, TRUE, NOW(3), NOW(3)),

-- ('q25', 'p1', 'm3', 't7', 's12', 'ASSIGNMENT', 'CODE', 'MEDIUM',
--  'Demonstrate the difference between interface and abstract class.',
--  'Implement both and show polymorphic behavior.', 6.00, JSON_OBJECT("tags", "java, abstraction, oops"), 1, TRUE, NOW(3), NOW(3)),

-- ('q26', 'p1', 'm1', 't2', 's4', 'SELF', 'CODE', 'MEDIUM',
--  'Check if a string is palindrome.',
--  'Reverse and compare with original.', 5.00, JSON_OBJECT("tags", "java, palindrome, strings"), 1, TRUE, NOW(3), NOW(3)),

-- ('q27', 'p1', 'm2', 't3', 's7', 'ASSIGNMENT', 'CODE', 'HARD',
--  'Generate Fibonacci series using while loop.',
--  'Iteratively print Fibonacci numbers.', 5.00, JSON_OBJECT("tags", "java, loops, fibonacci"), 1, TRUE, NOW(3), NOW(3)),

-- ('q28', 'p1', 'm2', 't4', 's9', 'SELF', 'CODE', 'EASY',
--  'Demonstrate constructor overloading.',
--  'Use multiple constructors with different params.', 4.00, JSON_OBJECT("tags", "java, constructor, overloading"), 1, TRUE, NOW(3), NOW(3)),

-- ('q29', 'p1', 'm3', 't7', 's12', 'ASSIGNMENT', 'CODE', 'HARD',
--  'Implement Observer Pattern.',
--  'Use interface to simulate listener notifications.', 7.00, JSON_OBJECT("tags", "java, observer, designpattern"), 1, TRUE, NOW(3), NOW(3)),

-- ('q30', 'p1', 'm3', 't9', 's13', 'SELF', 'CODE', 'MEDIUM',
--  'Use anonymous inner class for event handling.',
--  'Implement inline listener using anonymous class.', 5.00, JSON_OBJECT("tags", "java, anonymous, innerclass"), 1, TRUE, NOW(3), NOW(3)),

-- ('q31', 'p1', 'm2', 't8', 's12', 'ASSIGNMENT', 'CODE', 'MEDIUM',
--  'Create a multithreaded program using Thread class.',
--  'Extend Thread and override run().', 6.00, JSON_OBJECT("tags", "java, thread, concurrency"), 1, TRUE, NOW(3), NOW(3)),

-- ('q32', 'p1', 'm2', 't8', 's13', 'SELF', 'CODE', 'HARD',
--  'Demonstrate synchronization between threads.',
--  'Use synchronized methods or blocks.', 7.00, JSON_OBJECT("tags", "java, synchronization, threads"), 1, TRUE, NOW(3), NOW(3)),

-- ('q33', 'p1', 'm2', 't8', 's13', 'ASSIGNMENT', 'CODE', 'EASY',
--  'Demonstrate sleep() and join() methods.',
--  'Pause and wait for thread completion.', 4.00, JSON_OBJECT("tags", "java, multithreading, sleep"), 1, TRUE, NOW(3), NOW(3)),

-- ('q34', 'p1', 'm2', 't3', 's8', 'SELF', 'CODE', 'MEDIUM',
--  'Print pyramid pattern using nested loops.',
--  'Use nested for loops with spaces and stars.', 5.00, JSON_OBJECT("tags", "java, pattern, nested-loops"), 1, TRUE, NOW(3), NOW(3)),

-- ('q35', 'p1', 'm3', 't5', 's11', 'SELF', 'CODE', 'EASY',
--  'Compare two objects using equals().',
--  'Override equals() method for comparison.', 4.00, JSON_OBJECT("tags", "java, equals, objectclass"), 1, TRUE, NOW(3), NOW(3)),

-- ('q36', 'p1', 'm1', 't2', 's4', 'ASSIGNMENT', 'CODE', 'HARD',
--  'Find longest substring without repeating characters.',
--  'Use HashSet sliding window approach.', 7.00, JSON_OBJECT("tags", "java, string, algorithm"), 1, TRUE, NOW(3), NOW(3)),

-- ('q37', 'p1', 'm3', 't7', 's12', 'SELF', 'CODE', 'MEDIUM',
--  'Implement Strategy Pattern for sorting algorithms.',
--  'Define interface and concrete strategies.', 6.00, JSON_OBJECT("tags", "java, strategy, designpattern"), 1, TRUE, NOW(3), NOW(3)),

-- ('q38', 'p1', 'm1', 't2', 's3', 'SELF', 'CODE', 'EASY',
--  'Convert a string to uppercase manually.',
--  'Iterate and convert characters using Character.toUpperCase.', 3.00, JSON_OBJECT("tags", "java, string, uppercase"), 1, TRUE, NOW(3), NOW(3)),

-- ('q39', 'p1', 'm1', 't2', 's4', 'ASSIGNMENT', 'CODE', 'MEDIUM',
--  'Find index of first occurrence of substring.',
--  'Use indexOf() method.', 4.00, JSON_OBJECT("tags", "java, substring, indexOf"), 1, TRUE, NOW(3), NOW(3)),

-- ('q40', 'p1', 'm2', 't3', 's6', 'SELF', 'CODE', 'EASY',
--  'Check leap year using conditional statements.',
--  'Use nested if conditions.', 3.00, JSON_OBJECT("tags", "java, leapyear, conditional"), 1, TRUE, NOW(3), NOW(3)),

-- ('q41', 'p1', 'm3', 't9', 's13', 'ASSIGNMENT', 'CODE', 'HARD',
--  'Demonstrate use of local inner classes.',
--  'Create inner class inside method.', 6.00, JSON_OBJECT("tags", "java, localinner, advancedjava"), 1, TRUE, NOW(3), NOW(3)),

-- ('q42', 'p1', 'm1', 't2', 's3', 'SELF', 'CODE', 'EASY',
--  'Split a sentence into words.',
--  'Use split(" ") and print array.', 3.00, JSON_OBJECT("tags", "java, split, strings"), 1, TRUE, NOW(3), NOW(3)),

-- ('q43', 'p1', 'm3', 't7', 's12', 'SELF', 'CODE', 'MEDIUM',
--  'Demonstrate Decorator Pattern.',
--  'Wrap an object dynamically with extra functionality.', 6.00, JSON_OBJECT("tags", "java, decorator, oops"), 1, TRUE, NOW(3), NOW(3)),

-- ('q44', 'p1', 'm2', 't8', 's12', 'ASSIGNMENT', 'CODE', 'HARD',
--  'Implement thread communication using wait() and notify().',
--  'Use synchronized blocks for coordination.', 7.00, JSON_OBJECT("tags", "java, wait-notify, concurrency"), 1, TRUE, NOW(3), NOW(3)),

-- ('q45', 'p1', 'm3', 't9', 's13', 'SELF', 'CODE', 'MEDIUM',
--  'Demonstrate member inner class access rules.',
--  'Show private variable access from inner class.', 5.00, JSON_OBJECT("tags", "java, memberinner, innerclass"), 1, TRUE, NOW(3), NOW(3)),

-- ('q46', 'p1', 'm1', 't1', 's2', 'ASSIGNMENT', 'CODE', 'EASY',
--  'Merge multiple strings using StringBuilder append().',
--  'Use append() in a loop.', 4.00, JSON_OBJECT("tags", "java, stringbuilder, append"), 1, TRUE, NOW(3), NOW(3)),

-- ('q47', 'p1', 'm1', 't2', 's5', 'SELF', 'CODE', 'EASY',
--  'Find frequency of words in a sentence.',
--  'Split sentence and count using HashMap.', 4.00, JSON_OBJECT("tags", "java, hashmap, frequency"), 1, TRUE, NOW(3), NOW(3)),

-- ('q48', 'p1', 'm2', 't4', 's9', 'ASSIGNMENT', 'CODE', 'MEDIUM',
--  'Demonstrate polymorphism using method overriding.',
--  'Call overridden methods via base reference.', 5.00, JSON_OBJECT("tags", "java, polymorphism, oops"), 1, TRUE, NOW(3), NOW(3)),

-- ('q49', 'p1', 'm2', 't3', 's8', 'SELF', 'CODE', 'MEDIUM',
--  'Use nested while loops for pattern printing.',
--  'Combine loops with spacing logic.', 5.00, JSON_OBJECT("tags", "java, loops, nested"), 1, TRUE, NOW(3), NOW(3)),

-- ('q50', 'p1', 'm1', 't2', 's3', 'ASSIGNMENT', 'CODE', 'MEDIUM',
--  'Swap two strings without using a temporary variable.',
--  'Use concatenation and substring logic.', 5.00, JSON_OBJECT("tags", "java, swap, strings"), 1, TRUE, NOW(3), NOW(3)),

-- ('q51', 'p1', 'm2', 't8', 's3', 'SELF', 'CODE', 'HARD',
--  'Implement ExecutorService for multithreading.',
--  'Submit multiple runnable tasks.', 7.00, JSON_OBJECT("tags", "java, executors, concurrency"), 1, TRUE, NOW(3), NOW(3)),

-- ('q52', 'p1', 'm3', 't7', 's12', 'ASSIGNMENT', 'CODE', 'HARD',
--  'Implement Adapter Pattern example.',
--  'Convert one interface to another.', 6.00, JSON_OBJECT("tags", "java, adapter, designpattern"), 1, TRUE, NOW(3), NOW(3)),

-- ('q53', 'p1', 'm3', 't9', 's13', 'SELF', 'CODE', 'MEDIUM',
--  'Use nested interface within a class.',
--  'Define and implement nested interface.', 5.00, JSON_OBJECT("tags", "java, nestedinterface, innerclass"), 1, TRUE, NOW(3), NOW(3));

-- -- Insert one row into user_activity
-- INSERT INTO user_activity (id, user_id, session_start, session_end, duration_seconds, created_at)
-- VALUES (
--     'us-111',  -- id
--     'USER_1',                               -- user_id
--     1700317200,                               -- session_start (2025-11-18 09:00:00 UTC)
--     1700322600,                               -- session_end   (2025-11-18 10:30:00 UTC)
--     5400,                                     -- duration_seconds (1.5 hours)
--     NOW()                                     -- created_at
-- );

-- -- Insert one row into user_total_time
-- INSERT INTO user_total_time (user_id, total_time_spent)
-- VALUES (
--     'USER_1',   -- user_id
--     5400          -- total_time_spent in seconds
-- );


-- Arpit
INSERT INTO questions (
    id, programme_id, module_id, topic_id, subtopic_id,
    question_type, answer_type, difficulty,
    stem_md, solution_md, score_weight,
    metadata_json, version, is_current, created_at, updated_at
)
VALUES

('q101', 'p1', 'm1', 't1', 's1',
 'ASSIGNMENT', 'CODE', 'EASY',
 'A chat app needs to display the initials of a user for an avatar. Read a full name as a string and print the first and last character of the name on separate lines.',
 'Read the full name as a String, use charAt(0) for the first character and charAt(length-1) for the last character, then print both.',
 3.00, JSON_OBJECT("tags", "java, strings, accessing-characters, scenario"), 1, TRUE, NOW(3), NOW(3)),

('q102', 'p1', 'm1', 't1', 's2',
 'PRACTICE', 'CODE', 'EASY',
 'In an online ticket system, each booking id is formed by combining a city code and a numeric sequence (for example BLR + 1052 -> BLR1052). Write a program that reads the city code and the sequence number as separate inputs and combines them into one booking id without using the plus operator for string concatenation.',
 'Store the city code as a String and the sequence number as a String or convert it to String, then use String.concat or a StringBuilder append chain to produce the final booking id.',
 3.00, JSON_OBJECT("tags", "java, strings, concatenation, scenario"), 1, TRUE, NOW(3), NOW(3)),

('q103', 'p1', 'm1', 't2', 's3',
 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'A warehouse application stores product codes entered by staff with extra spaces and mixed case (for example "  ab-123  "). Write a program that reads a product code and normalises it by trimming spaces at both ends and converting the code to upper case before saving.',
 'Use String.trim to remove leading and trailing spaces and toUpperCase to convert the product code to upper case, then print or return the normalised value.',
 5.00, JSON_OBJECT("tags", "java, strings, trim, toUpperCase, data-cleaning"), 1, TRUE, NOW(3), NOW(3)),

('q104', 'p1', 'm1', 't2', 's4',
 'PRACTICE', 'CODE', 'MEDIUM',
 'In a log monitoring tool, each log line is represented as a string. Write a program that reads a single log line and checks whether it contains the word "ERROR". If present, print the starting index of the word; otherwise print a message that there is no error.',
 'Use indexOf("ERROR") on the log string. If the result is -1, print that there is no error; otherwise print the index value.',
 5.00, JSON_OBJECT("tags", "java, strings, searching, indexOf, logs"), 1, TRUE, NOW(3), NOW(3)),

('q105', 'p1', 'm1', 't2', 's5',
 'ASSIGNMENT', 'CODE', 'HARD',
 'A customer support team wants to analyse how often vowels appear in complaint messages. Write a program that reads a full complaint sentence and counts the total frequency of each vowel (a, e, i, o, u) ignoring case. Print the count for each vowel.',
 'Convert the string to lower case, iterate over all characters, and maintain five counters for a, e, i, o, u. Whenever a vowel is found, increment the relevant counter and finally print all counts.',
 8.00, JSON_OBJECT("tags", "java, strings, counting, frequency, vowels"), 1, TRUE, NOW(3), NOW(3)),

('q106', 'p1', 'm1', 't2', 's5',
 'PRACTICE', 'CODE', 'HARD',
 'Two different teams have generated coupon codes, and you want to check if two given coupon codes are anagrams of each other (they contain exactly the same characters in possibly different orders). Write a program that reads two strings and prints whether they are anagrams by comparing the frequency of each character.',
 'First check if the lengths match. If they do, either sort both strings and compare, or use an integer frequency array (for example of size 256 or 128) to count characters from the first string and subtract counts using the second string. If all counts are zero at the end, they are anagrams.',
 8.00, JSON_OBJECT("tags", "java, strings, anagram, frequency-count"), 1, TRUE, NOW(3), NOW(3)),

('q107', 'p1', 'm2', 't3', 's6',
 'ASSIGNMENT', 'CODE', 'EASY',
 'A cinema offers discounts on tickets based on age: below 12 is Child, 12 to 59 is Adult, and 60 or above is Senior. Read the age of a customer and print the category label using if else statements.',
 'Use an if else ladder: if age < 12 then print Child; else if age < 60 then print Adult; else print Senior.',
 3.00, JSON_OBJECT("tags", "java, control-flow, if-else, scenario"), 1, TRUE, NOW(3), NOW(3)),

('q108', 'p1', 'm2', 't3', 's7',
 'PRACTICE', 'CODE', 'EASY',
 'A learning portal wants to show a multiplication table for a chosen number to help students practise. Read an integer n and display the multiplication table from n x 1 up to n x 10 using a loop.',
 'Use a for loop from 1 to 10 and in each iteration print n, the current multiplier, and the product.',
 3.00, JSON_OBJECT("tags", "java, loops, for-loop, multiplication-table"), 1, TRUE, NOW(3), NOW(3)),

('q109', 'p1', 'm2', 't3', 's8',
 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'A school wants to print a progress chart showing stars for each student based on performance level per subject. For 3 students and 3 subjects, print rows where each row shows a student id and three groups of stars, one group per subject, using nested loops.',
 'Use an outer loop for students and an inner loop for subjects. For each subject, print a fixed or input based number of stars. Combine student labels and stars in a readable format.',
 5.00, JSON_OBJECT("tags", "java, nested-loops, patterns, scenario"), 1, TRUE, NOW(3), NOW(3)),

('q110', 'p1', 'm2', 't4', 's9',
 'PRACTICE', 'CODE', 'MEDIUM',
 'A bank needs a simple representation of an account for a console based prototype. Design a BankAccount class with fields accountNumber, accountHolderName, and balance. Provide methods to deposit and withdraw money and a method to print account details. In main, create one account, perform some operations, and print the final details.',
 'Create a BankAccount class with private fields, a constructor, and methods deposit, withdraw (which update balance), and printDetails. In the main method instantiate the class and call the methods to demonstrate usage.',
 5.00, JSON_OBJECT("tags", "java, oops, classes, objects, bank-account"), 1, TRUE, NOW(3), NOW(3)),

('q111', 'p1', 'm2', 't4', 's9',
 'ASSIGNMENT', 'CODE', 'HARD',
 'An e-commerce prototype needs an Order model. Create classes Customer (name, email) and Item (name, price, quantity) and an Order class that contains a Customer and an array of Item objects. Add a method in Order to calculate the total amount and another method to print an order summary. In main, build a sample order and display the summary.',
 'Model Customer and Item as separate classes. In the Order class, store a Customer reference and an array or list of Item. Implement a method that loops through all items, multiplies price by quantity, sums the values, and prints a formatted summary with customer and item details.',
 8.00, JSON_OBJECT("tags", "java, oops, composition, order-summary"), 1, TRUE, NOW(3), NOW(3)),

('q112', 'p1', 'm2', 't6', 's10',
 'PRACTICE', 'CODE', 'MEDIUM',
 'A retail store tracks daily sales for a week. Read 7 integer values representing sales for each day and store them in an array. Then calculate and print the total and average sales for the week.',
 'Declare an int array of size 7, fill it using a loop, then iterate again to compute the sum. The average is sum divided by 7. Print both sum and average.',
 5.00, JSON_OBJECT("tags", "java, arrays, sum, average, sales"), 1, TRUE, NOW(3), NOW(3)),

('q113', 'p1', 'm2', 't6', 's10',
 'ASSIGNMENT', 'CODE', 'HARD',
 'A performance dashboard collects response time data (in milliseconds) for an API. Read N response times into an array. Write a program to find and print the minimum, maximum, and median response time. Assume N is odd for simplicity.',
 'After reading N and the array, traverse once to find min and max. To get the median, sort the array using Arrays.sort and take the middle element at index N/2.',
 8.00, JSON_OBJECT("tags", "java, arrays, min-max, median, analytics"), 1, TRUE, NOW(3), NOW(3)),

('q114', 'p1', 'm3', 't5', 's11',
 'PRACTICE', 'CODE', 'EASY',
 'A logging system prints product details frequently, and you want readable text instead of the default class name and hash code. Create a Product class with id, name, and price fields and override the toString method so that printing an object directly shows a friendly description of the product.',
 'Define a Product class with fields and override toString to return a formatted string including id, name, and price. In main, create a Product instance and print it to verify the customised output.',
 3.00, JSON_OBJECT("tags", "java, object-class, toString, logging"), 1, TRUE, NOW(3), NOW(3)),

('q115', 'p1', 'm3', 't5', 's11',
 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'A university portal must prevent duplicate Student records in a HashSet based on rollNumber. Create a Student class with fields rollNumber and name and override equals and hashCode so that two Student objects with the same rollNumber are treated as duplicates in a HashSet.',
 'Implement Student with private fields and override equals to compare rollNumber and hashCode to generate a hash from rollNumber. Demonstrate behaviour by adding multiple students with the same rollNumber to a HashSet and showing that duplicates are not stored.',
 5.00, JSON_OBJECT("tags", "java, object-class, equals, hashCode, hashset"), 1, TRUE, NOW(3), NOW(3)),

('q116', 'p1', 'm3', 't7', 's12',
 'PRACTICE', 'CODE', 'MEDIUM',
 'An enterprise application needs only one configuration manager object throughout its lifecycle. Implement a Singleton class ConfigManager that returns the same instance on every call. Demonstrate its use in main by calling a getInstance method from multiple places and showing that references are identical.',
 'Create a class with a private static instance field, a private constructor, and a public static getInstance method that lazily initialises and returns the single object. In main, call getInstance multiple times and compare references with ==.',
 5.00, JSON_OBJECT("tags", "java, design-patterns, singleton, config-manager"), 1, TRUE, NOW(3), NOW(3)),

('q117', 'p1', 'm3', 't7', 's12',
 'ASSIGNMENT', 'CODE', 'HARD',
 'A notification service must send alerts through different channels such as Email, SMS, and Push. Implement a simple factory pattern with a Notification interface and concrete classes EmailNotification, SmsNotification, and PushNotification. Create a NotificationFactory that returns the correct implementation based on a type string, and demonstrate sending a sample message through each channel.',
 'Define a Notification interface with a send method. Implement three concrete classes for email, sms, and push. In NotificationFactory, write a static method that checks the type value and returns the appropriate implementation. In main, call the factory with different types and invoke send on the returned objects.',
 8.00, JSON_OBJECT("tags", "java, design-patterns, factory, notifications"), 1, TRUE, NOW(3), NOW(3)),

('q118', 'p1', 'm3', 't9', 's13',
 'PRACTICE', 'CODE', 'MEDIUM',
 'A desktop UI framework class Window wants to handle button click logic inside the Window itself so that it has direct access to its fields. Create a Window class with a title field and define a non static inner class ButtonHandler that has a handleClick method printing a message including the window title. In main, create a Window and use the inner class to simulate a click.',
 'Define Window with a String title and an inner class ButtonHandler that uses title inside handleClick. In main, create a Window object, then create ButtonHandler using window.new ButtonHandler and call handleClick.',
 5.00, JSON_OBJECT("tags", "java, inner-classes, ui-handler, scenario"), 1, TRUE, NOW(3), NOW(3)),

('q119', 'p1', 'm3', 't9', 's13',
 'ASSIGNMENT', 'CODE', 'HARD',
 'You are designing an immutable configuration object ApplicationConfig that may have many optional fields. Implement a static nested Builder class inside ApplicationConfig that follows the builder pattern, allowing chained methods to set different fields and a build method to create the final ApplicationConfig instance.',
 'Create ApplicationConfig with private final fields and a private constructor that accepts a Builder. Inside ApplicationConfig, implement a public static class Builder with mutable fields, setter style methods that return this, and a build method that returns a new ApplicationConfig using the builder state. Demonstrate chained calls in main.',
 8.00, JSON_OBJECT("tags", "java, nested-classes, builder-pattern, immutability"), 1, TRUE, NOW(3), NOW(3)),

('q120', 'p1', 'm3', 't7', 's12',
 'PRACTICE', 'CODE', 'HARD',
 'A shopping platform supports multiple payment strategies like CreditCardPayment, UpiPayment, and WalletPayment. Implement the strategy pattern with a PaymentStrategy interface and concrete classes for each payment type. Create an OrderProcessor class that accepts a PaymentStrategy at runtime and uses it to process payment for a given amount.',
 'Define PaymentStrategy with a pay method. Implement concrete strategies for credit card, UPI, and wallet. In OrderProcessor, keep a PaymentStrategy field set via constructor or setter and call pay in a processOrder method. In main, create OrderProcessor with different strategies to show how behaviour changes at runtime.',
 8.00, JSON_OBJECT("tags", "java, design-patterns, strategy, payments"), 1, TRUE, NOW(3), NOW(3));


--  sam
INSERT INTO questions (
    id, programme_id, module_id, topic_id, subtopic_id,
    question_type, answer_type, difficulty,
    stem_md, solution_md, score_weight,
    metadata_json, version, is_current, created_at, updated_at
)
VALUES
-- ===========================================
-- q1
-- ===========================================
('q1','p1','m1','t1','s1','ASSIGNMENT','CODE','MEDIUM',
'Your junior teammate is debugging an application where the username characters must be checked one-by-one. Write a program that prints each character of a string individually.',
'Use a loop with charAt() or convert to char array.',5.00,
JSON_OBJECT("scenario","debugging username validation"),1,TRUE,NOW(3),NOW(3)),

-- q2
('q2','p1','m1','t1','s2','PRACTICE','CODE','EASY',
'During onboarding, HR gives you two separate string values for first name and last name. Combine them into a single full name without using the + operator.',
'Use StringBuilder, concat(), or String.join().',3.00,
JSON_OBJECT("scenario","joining employee names"),1,TRUE,NOW(3),NOW(3)),

-- q3
('q3','p1','m2','t3','s6','ASSIGNMENT','CODE','MEDIUM',
'In a loan approval module, applicants are filtered using multiple conditions. Demonstrate conditional flows (if-else + switch) to process an applicant’s profile.',
'Combine multiple conditional checks and branching.',5.00,
JSON_OBJECT("scenario","loan approval logic"),1,TRUE,NOW(3),NOW(3)),

-- q4
('q4','p1','m2','t3','s7','PRACTICE','CODE','MEDIUM',
'Your team needs a basic module that prints different patterns and numeric sequences for a training dashboard. Write loops demonstrating for/while/do-while.',
'Show looping constructs for sequences.',5.00,
JSON_OBJECT("scenario","training dashboard loops"),1,TRUE,NOW(3),NOW(3)),

-- q5
('q5','p1','m1','t1','s1','PRACTICE','CODE','EASY',
'In a text-processing system, you need to extract the first and last visible characters of a given user input string.',
'Use charAt(0) and charAt(length-1).',3.00,
JSON_OBJECT("scenario","text processing utility"),1,TRUE,NOW(3),NOW(3)),

-- q6
('q6','p1','m1','t1','s2','ASSIGNMENT','CODE','MEDIUM',
'Marketing wants you to join an array of keywords into a single tagline. Write a program to merge all words into one sentence.',
'Use String.join() or StringBuilder.',4.00,
JSON_OBJECT("scenario","marketing tagline generator"),1,TRUE,NOW(3),NOW(3)),

-- q7
('q7','p1','m1','t2','s3','PRACTICE','CODE','EASY',
'A legacy API returns reversed IDs. You must restore their original form by reversing them back. Write a custom string reverse logic.',
'Reverse by iterating from end to start.',4.00,
JSON_OBJECT("scenario","reverse legacy IDs"),1,TRUE,NOW(3),NOW(3)),

-- q8
('q8','p1','m1','t2','s4','ASSIGNMENT','CODE','MEDIUM',
'A fraud detection system must check if a suspicious pattern exists in a message. Implement substring search.',
'Use contains() or indexOf().',5.00,
JSON_OBJECT("scenario","fraud pattern detection"),1,TRUE,NOW(3),NOW(3)),

-- q9
('q9','p1','m1','t2','s5','PRACTICE','CODE','EASY',
'An email spam analyzer counts character frequency in subject lines. Count occurrences of a given character.',
'Loop and match characters.',3.00,
JSON_OBJECT("scenario","spam analyzer frequency"),1,TRUE,NOW(3),NOW(3)),

-- q10
('q10','p1','m2','t3','s6','ASSIGNMENT','CODE','EASY',
'A billing system checks whether a reading is even or odd to assign consumption tier. Implement the logic.',
'Use modulus operator.',3.00,
JSON_OBJECT("scenario","billing tier classification"),1,TRUE,NOW(3),NOW(3)),

-- q11
('q11','p1','m2','t3','s7','PRACTICE','CODE','MEDIUM',
'Your batch-processing script needs to print multiplication tables for quick QA checks.',
'Use nested loops.',5.00,
JSON_OBJECT("scenario","QA batch checks"),1,TRUE,NOW(3),NOW(3)),

-- q12
('q12','p1','m2','t3','s8','ASSIGNMENT','CODE','HARD',
'Your UI template engine team wants star patterns for onboarding visuals. Generate complex patterns using nested loops.',
'Use nested loops.',6.00,
JSON_OBJECT("scenario","UI onboarding visual patterns"),1,TRUE,NOW(3),NOW(3)),

-- q13
('q13','p1','m2','t4','s9','PRACTICE','CODE','MEDIUM',
'You are asked to create a class representing an online order with attributes and methods. Implement fields and behaviors.',
'Define class, fields, constructor, methods.',5.00,
JSON_OBJECT("scenario","online order modelling"),1,TRUE,NOW(3),NOW(3)),

-- q14
('q14','p1','m2','t4','s9','ASSIGNMENT','CODE','HARD',
'You must extend a base Employee class into multiple specialized roles and override methods to show behavior differences.',
'Use inheritance and overriding.',6.00,
JSON_OBJECT("scenario","employee role hierarchy"),1,TRUE,NOW(3),NOW(3)),

-- q15
('q15','p1','m3','t5','s11','PRACTICE','CODE','EASY',
'A debugging tool prints all methods of a given class for inspection. Demonstrate retrieving method list from Object class.',
'Use getClass().getMethods().',4.00,
JSON_OBJECT("scenario","debugging class inspector"),1,TRUE,NOW(3),NOW(3)),

-- q16
('q16','p1','m3','t5','s11','ASSIGNMENT','CODE','MEDIUM',
'Two customer objects must be checked for equality so the CRM system does not create duplicates. Override equals() and hashCode().',
'Override both methods.',5.00,
JSON_OBJECT("scenario","duplicate customer prevention"),1,TRUE,NOW(3),NOW(3)),

-- q17
('q17','p1','m3','t7','s12','PRACTICE','CODE','MEDIUM',
'Your system should allow only one instance of ConfigService for the entire application. Implement Singleton.',
'Use private constructor + static instance.',5.00,
JSON_OBJECT("scenario","config service singleton"),1,TRUE,NOW(3),NOW(3)),

-- q18
('q18','p1','m3','t7','s12','ASSIGNMENT','CODE','HARD',
'Your product supports multiple file exporters. Implement a Factory Pattern to generate exporter objects.',
'Create interface + concrete classes.',7.00,
JSON_OBJECT("scenario","file exporter factory"),1,TRUE,NOW(3),NOW(3)),

-- q19
('q19','p1','m3','t9','s13','PRACTICE','CODE','MEDIUM',
'In an event-logging system, inner classes must access outer class event properties. Demonstrate inner class usage.',
'Define inner class accessing outer vars.',5.00,
JSON_OBJECT("scenario","event logging with inner class"),1,TRUE,NOW(3),NOW(3)),

-- q20
('q20','p1','m3','t9','s13','ASSIGNMENT','CODE','HARD',
'A UI framework needs nested classes for callbacks. Demonstrate static nested + anonymous classes.',
'Implement both types.',6.00,
JSON_OBJECT("scenario","UI callback handlers"),1,TRUE,NOW(3),NOW(3)),

-- q21
('q21','p1','m2','t6','s10','PRACTICE','CODE','EASY',
'An analytics engine processes arrays and must find max value. Implement logic to find largest element.',
'Loop & track largest.',3.00,
JSON_OBJECT("scenario","analytics max finder"),1,TRUE,NOW(3),NOW(3)),

-- q22
('q22','p1','m2','t6','s10','ASSIGNMENT','CODE','MEDIUM',
'Inventory records must be sorted without built-in sort logic. Implement bubble or selection sort.',
'Use manual sorting.',5.00,
JSON_OBJECT("scenario","inventory sorter"),1,TRUE,NOW(3),NOW(3)),

-- q23
('q23','p1','m2','t6','s10','PRACTICE','CODE','HARD',
'A search tool must locate items in sorted array quickly. Implement binary search.',
'Implement binary search.',6.00,
JSON_OBJECT("scenario","search tool optimization"),1,TRUE,NOW(3),NOW(3)),

-- q24
('q24','p1','m3','t5','s11','PRACTICE','CODE','EASY',
'Logging system must output object state for debugging. Override toString().',
'Implement toString().',3.00,
JSON_OBJECT("scenario","debug logging printer"),1,TRUE,NOW(3),NOW(3)),

-- q25
('q25','p1','m3','t7','s12','ASSIGNMENT','CODE','MEDIUM',
'You are designing a learning platform and must show difference between interface and abstract class.',
'Implement both and demo polymorphism.',6.00,
JSON_OBJECT("scenario","learning platform OOP module"),1,TRUE,NOW(3),NOW(3)),

-- q26
('q26','p1','m1','t2','s4','PRACTICE','CODE','MEDIUM',
'Customer IDs must be validated to check if they are palindromes. Implement palindrome logic.',
'Reverse and compare.',5.00,
JSON_OBJECT("scenario","customer id validator"),1,TRUE,NOW(3),NOW(3)),

-- q27
('q27','p1','m2','t3','s7','ASSIGNMENT','CODE','HARD',
'A dashboard requires Fibonacci sequence for visualization. Generate series using loops.',
'Implement Fibonacci.',5.00,
JSON_OBJECT("scenario","dashboard fibonacci widget"),1,TRUE,NOW(3),NOW(3)),

-- q28
('q28','p1','m2','t4','s9','PRACTICE','CODE','EASY',
'Your colleague wants to demonstrate constructor overloading in the user registration model.',
'Write multiple constructors.',4.00,
JSON_OBJECT("scenario","registration model constructors"),1,TRUE,NOW(3),NOW(3)),


-- q30
('q30','p1','m3','t9','s13','PRACTICE','CODE','MEDIUM',
'A GUI system uses anonymous classes for event handling. Demonstrate anonymous inner classes.',
'Implement anonymous classes.',5.00,
JSON_OBJECT("scenario","GUI event handlers"),1,TRUE,NOW(3),NOW(3));
