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

INSERT INTO questions (
    id, programme_id, module_id, topic_id, subtopic_id,
    question_type, answer_type, difficulty,
    stem_md, solution_md, score_weight,
    metadata_json, version, is_current, created_at, updated_at
)
VALUES
('q5', 'p1', 'm1', 't1', 's1', 'SELF', 'CODE', 'EASY',
 'Find the first and last character of a string.',
 'Use charAt(0) and charAt(length-1).', 3.00, JSON_OBJECT("tags", "java, strings, basics"), 1, TRUE, NOW(3), NOW(3)),

('q6', 'p1', 'm1', 't1', 's2', 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'Join an array of words into a single sentence.',
 'Use String.join() or StringBuilder.', 4.00, JSON_OBJECT("tags", "java, stringbuilder, join"), 1, TRUE, NOW(3), NOW(3)),

('q7', 'p1', 'm1', 't2', 's3', 'SELF', 'CODE', 'EASY',
 'Reverse a string without using built-in reverse().',
 'Iterate from end to start and append characters.', 4.00, JSON_OBJECT("tags", "java, reverse, strings"), 1, TRUE, NOW(3), NOW(3)),

('q8', 'p1', 'm1', 't2', 's4', 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'Check if a string contains a particular substring.',
 'Use contains() or indexOf().', 5.00, JSON_OBJECT("tags", "java, substring, search"), 1, TRUE, NOW(3), NOW(3)),

('q9', 'p1', 'm1', 't2', 's5', 'SELF', 'CODE', 'EASY',
 'Count occurrences of a character in a string.',
 'Loop through and increment counter for matches.', 3.00, JSON_OBJECT("tags", "java, counting, loops"), 1, TRUE, NOW(3), NOW(3)),

('q10', 'p1', 'm2', 't3', 's6', 'ASSIGNMENT', 'CODE', 'EASY',
 'Check if a number is even or odd using if-else.',
 'Use modulus operator (%).', 3.00, JSON_OBJECT("tags", "java, conditional, basics"), 1, TRUE, NOW(3), NOW(3)),

('q11', 'p1', 'm2', 't3', 's7', 'SELF', 'CODE', 'MEDIUM',
 'Print multiplication table using for loop.',
 'Use nested loops for multiple tables.', 5.00, JSON_OBJECT("tags", "java, loops, core"), 1, TRUE, NOW(3), NOW(3)),

('q12', 'p1', 'm2', 't3', 's8', 'ASSIGNMENT', 'CODE', 'HARD',
 'Implement a pattern program using nested loops.',
 'Use nested for loops and string concatenation.', 6.00, JSON_OBJECT("tags", "java, patterns, nested-loops"), 1, TRUE, NOW(3), NOW(3)),

('q13', 'p1', 'm2', 't4', 's9', 'SELF', 'CODE', 'MEDIUM',
 'Create a simple class with attributes and methods.',
 'Define class, fields, constructors, and methods.', 5.00, JSON_OBJECT("tags", "java, oops, class"), 1, TRUE, NOW(3), NOW(3)),

('q14', 'p1', 'm2', 't4', 's9', 'ASSIGNMENT', 'CODE', 'HARD',
 'Demonstrate inheritance and method overriding.',
 'Use extends keyword and override parent method.', 6.00, JSON_OBJECT("tags", "java, inheritance, oops"), 1, TRUE, NOW(3), NOW(3)),

('q15', 'p1', 'm3', 't5', 's11', 'SELF', 'CODE', 'EASY',
 'Display all methods of Object class.',
 'Use getClass().getMethods().', 4.00, JSON_OBJECT("tags", "java, reflection, objectclass"), 1, TRUE, NOW(3), NOW(3)),

('q16', 'p1', 'm3', 't5', 's11', 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'Demonstrate the use of equals() and hashCode().',
 'Override both in a custom class.', 5.00, JSON_OBJECT("tags", "java, objectclass, equals"), 1, TRUE, NOW(3), NOW(3)),

('q17', 'p1', 'm3', 't7', 's12', 'SELF', 'CODE', 'MEDIUM',
 'Implement a Singleton class.',
 'Use private constructor and static instance.', 5.00, JSON_OBJECT("tags", "java, singleton, designpattern"), 1, TRUE, NOW(3), NOW(3)),

('q18', 'p1', 'm3', 't7', 's12', 'ASSIGNMENT', 'CODE', 'HARD',
 'Demonstrate Factory Pattern with multiple classes.',
 'Use abstract class or interface with concrete implementations.', 7.00, JSON_OBJECT("tags", "java, factory, designpattern"), 1, TRUE, NOW(3), NOW(3)),

('q19', 'p1', 'm3', 't9', 's13', 'SELF', 'CODE', 'MEDIUM',
 'Create an inner class that accesses outer class variables.',
 'Define inner class and demonstrate access.', 5.00, JSON_OBJECT("tags", "java, innerclass, advancedjava"), 1, TRUE, NOW(3), NOW(3)),

('q20', 'p1', 'm3', 't9', 's13', 'ASSIGNMENT', 'CODE', 'HARD',
 'Demonstrate static nested classes and anonymous classes.',
 'Use static and anonymous inner class syntax.', 6.00, JSON_OBJECT("tags", "java, nestedclass, advancedjava"), 1, TRUE, NOW(3), NOW(3)),

('q21', 'p1', 'm2', 't6', 's10', 'SELF', 'CODE', 'EASY',
 'Find maximum element in an array.',
 'Loop through array and track largest element.', 3.00, JSON_OBJECT("tags", "java, array, basics"), 1, TRUE, NOW(3), NOW(3)),

('q22', 'p1', 'm2', 't6', 's10', 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'Sort an array without using sort().',
 'Use bubble sort or selection sort algorithm.', 5.00, JSON_OBJECT("tags", "java, sorting, array"), 1, TRUE, NOW(3), NOW(3)),

('q23', 'p1', 'm2', 't6', 's10', 'SELF', 'CODE', 'HARD',
 'Implement binary search on sorted array.',
 'Use mid-point comparison and recursion.', 6.00, JSON_OBJECT("tags", "java, binarysearch, array"), 1, TRUE, NOW(3), NOW(3)),

('q24', 'p1', 'm3', 't5', 's11', 'SELF', 'CODE', 'EASY',
 'Use toString() method in a class.',
 'Override toString() and print details.', 3.00, JSON_OBJECT("tags", "java, tostring, objectclass"), 1, TRUE, NOW(3), NOW(3)),

('q25', 'p1', 'm3', 't7', 's12', 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'Demonstrate the difference between interface and abstract class.',
 'Implement both and show polymorphic behavior.', 6.00, JSON_OBJECT("tags", "java, abstraction, oops"), 1, TRUE, NOW(3), NOW(3)),

('q26', 'p1', 'm1', 't2', 's4', 'SELF', 'CODE', 'MEDIUM',
 'Check if a string is palindrome.',
 'Reverse and compare with original.', 5.00, JSON_OBJECT("tags", "java, palindrome, strings"), 1, TRUE, NOW(3), NOW(3)),

('q27', 'p1', 'm2', 't3', 's7', 'ASSIGNMENT', 'CODE', 'HARD',
 'Generate Fibonacci series using while loop.',
 'Iteratively print Fibonacci numbers.', 5.00, JSON_OBJECT("tags", "java, loops, fibonacci"), 1, TRUE, NOW(3), NOW(3)),

('q28', 'p1', 'm2', 't4', 's9', 'SELF', 'CODE', 'EASY',
 'Demonstrate constructor overloading.',
 'Use multiple constructors with different params.', 4.00, JSON_OBJECT("tags", "java, constructor, overloading"), 1, TRUE, NOW(3), NOW(3)),

('q29', 'p1', 'm3', 't7', 's12', 'ASSIGNMENT', 'CODE', 'HARD',
 'Implement Observer Pattern.',
 'Use interface to simulate listener notifications.', 7.00, JSON_OBJECT("tags", "java, observer, designpattern"), 1, TRUE, NOW(3), NOW(3)),

('q30', 'p1', 'm3', 't9', 's13', 'SELF', 'CODE', 'MEDIUM',
 'Use anonymous inner class for event handling.',
 'Implement inline listener using anonymous class.', 5.00, JSON_OBJECT("tags", "java, anonymous, innerclass"), 1, TRUE, NOW(3), NOW(3)),

('q31', 'p1', 'm2', 't8', 's12', 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'Create a multithreaded program using Thread class.',
 'Extend Thread and override run().', 6.00, JSON_OBJECT("tags", "java, thread, concurrency"), 1, TRUE, NOW(3), NOW(3)),

('q32', 'p1', 'm2', 't8', 's13', 'SELF', 'CODE', 'HARD',
 'Demonstrate synchronization between threads.',
 'Use synchronized methods or blocks.', 7.00, JSON_OBJECT("tags", "java, synchronization, threads"), 1, TRUE, NOW(3), NOW(3)),

('q33', 'p1', 'm2', 't8', 's13', 'ASSIGNMENT', 'CODE', 'EASY',
 'Demonstrate sleep() and join() methods.',
 'Pause and wait for thread completion.', 4.00, JSON_OBJECT("tags", "java, multithreading, sleep"), 1, TRUE, NOW(3), NOW(3)),

('q34', 'p1', 'm2', 't3', 's8', 'SELF', 'CODE', 'MEDIUM',
 'Print pyramid pattern using nested loops.',
 'Use nested for loops with spaces and stars.', 5.00, JSON_OBJECT("tags", "java, pattern, nested-loops"), 1, TRUE, NOW(3), NOW(3)),

('q35', 'p1', 'm3', 't5', 's11', 'SELF', 'CODE', 'EASY',
 'Compare two objects using equals().',
 'Override equals() method for comparison.', 4.00, JSON_OBJECT("tags", "java, equals, objectclass"), 1, TRUE, NOW(3), NOW(3)),

('q36', 'p1', 'm1', 't2', 's4', 'ASSIGNMENT', 'CODE', 'HARD',
 'Find longest substring without repeating characters.',
 'Use HashSet sliding window approach.', 7.00, JSON_OBJECT("tags", "java, string, algorithm"), 1, TRUE, NOW(3), NOW(3)),

('q37', 'p1', 'm3', 't7', 's12', 'SELF', 'CODE', 'MEDIUM',
 'Implement Strategy Pattern for sorting algorithms.',
 'Define interface and concrete strategies.', 6.00, JSON_OBJECT("tags", "java, strategy, designpattern"), 1, TRUE, NOW(3), NOW(3)),

('q38', 'p1', 'm1', 't2', 's3', 'SELF', 'CODE', 'EASY',
 'Convert a string to uppercase manually.',
 'Iterate and convert characters using Character.toUpperCase.', 3.00, JSON_OBJECT("tags", "java, string, uppercase"), 1, TRUE, NOW(3), NOW(3)),

('q39', 'p1', 'm1', 't2', 's4', 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'Find index of first occurrence of substring.',
 'Use indexOf() method.', 4.00, JSON_OBJECT("tags", "java, substring, indexOf"), 1, TRUE, NOW(3), NOW(3)),

('q40', 'p1', 'm2', 't3', 's6', 'SELF', 'CODE', 'EASY',
 'Check leap year using conditional statements.',
 'Use nested if conditions.', 3.00, JSON_OBJECT("tags", "java, leapyear, conditional"), 1, TRUE, NOW(3), NOW(3)),

('q41', 'p1', 'm3', 't9', 's13', 'ASSIGNMENT', 'CODE', 'HARD',
 'Demonstrate use of local inner classes.',
 'Create inner class inside method.', 6.00, JSON_OBJECT("tags", "java, localinner, advancedjava"), 1, TRUE, NOW(3), NOW(3)),

('q42', 'p1', 'm1', 't2', 's3', 'SELF', 'CODE', 'EASY',
 'Split a sentence into words.',
 'Use split(" ") and print array.', 3.00, JSON_OBJECT("tags", "java, split, strings"), 1, TRUE, NOW(3), NOW(3)),

('q43', 'p1', 'm3', 't7', 's12', 'SELF', 'CODE', 'MEDIUM',
 'Demonstrate Decorator Pattern.',
 'Wrap an object dynamically with extra functionality.', 6.00, JSON_OBJECT("tags", "java, decorator, oops"), 1, TRUE, NOW(3), NOW(3)),

('q44', 'p1', 'm2', 't8', 's12', 'ASSIGNMENT', 'CODE', 'HARD',
 'Implement thread communication using wait() and notify().',
 'Use synchronized blocks for coordination.', 7.00, JSON_OBJECT("tags", "java, wait-notify, concurrency"), 1, TRUE, NOW(3), NOW(3)),

('q45', 'p1', 'm3', 't9', 's13', 'SELF', 'CODE', 'MEDIUM',
 'Demonstrate member inner class access rules.',
 'Show private variable access from inner class.', 5.00, JSON_OBJECT("tags", "java, memberinner, innerclass"), 1, TRUE, NOW(3), NOW(3)),

('q46', 'p1', 'm1', 't1', 's2', 'ASSIGNMENT', 'CODE', 'EASY',
 'Merge multiple strings using StringBuilder append().',
 'Use append() in a loop.', 4.00, JSON_OBJECT("tags", "java, stringbuilder, append"), 1, TRUE, NOW(3), NOW(3)),

('q47', 'p1', 'm1', 't2', 's5', 'SELF', 'CODE', 'EASY',
 'Find frequency of words in a sentence.',
 'Split sentence and count using HashMap.', 4.00, JSON_OBJECT("tags", "java, hashmap, frequency"), 1, TRUE, NOW(3), NOW(3)),

('q48', 'p1', 'm2', 't4', 's9', 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'Demonstrate polymorphism using method overriding.',
 'Call overridden methods via base reference.', 5.00, JSON_OBJECT("tags", "java, polymorphism, oops"), 1, TRUE, NOW(3), NOW(3)),

('q49', 'p1', 'm2', 't3', 's8', 'SELF', 'CODE', 'MEDIUM',
 'Use nested while loops for pattern printing.',
 'Combine loops with spacing logic.', 5.00, JSON_OBJECT("tags", "java, loops, nested"), 1, TRUE, NOW(3), NOW(3)),

('q50', 'p1', 'm1', 't2', 's3', 'ASSIGNMENT', 'CODE', 'MEDIUM',
 'Swap two strings without using a temporary variable.',
 'Use concatenation and substring logic.', 5.00, JSON_OBJECT("tags", "java, swap, strings"), 1, TRUE, NOW(3), NOW(3)),

('q51', 'p1', 'm2', 't8', 's3', 'SELF', 'CODE', 'HARD',
 'Implement ExecutorService for multithreading.',
 'Submit multiple runnable tasks.', 7.00, JSON_OBJECT("tags", "java, executors, concurrency"), 1, TRUE, NOW(3), NOW(3)),

('q52', 'p1', 'm3', 't7', 's12', 'ASSIGNMENT', 'CODE', 'HARD',
 'Implement Adapter Pattern example.',
 'Convert one interface to another.', 6.00, JSON_OBJECT("tags", "java, adapter, designpattern"), 1, TRUE, NOW(3), NOW(3)),

('q53', 'p1', 'm3', 't9', 's13', 'SELF', 'CODE', 'MEDIUM',
 'Use nested interface within a class.',
 'Define and implement nested interface.', 5.00, JSON_OBJECT("tags", "java, nestedinterface, innerclass"), 1, TRUE, NOW(3), NOW(3));

-- Insert one row into user_activity
INSERT INTO user_activity (id, user_id, session_start, session_end, duration_seconds, created_at)
VALUES (
    'us-111',  -- id
    'USER_1',                               -- user_id
    1700317200,                               -- session_start (2025-11-18 09:00:00 UTC)
    1700322600,                               -- session_end   (2025-11-18 10:30:00 UTC)
    5400,                                     -- duration_seconds (1.5 hours)
    NOW()                                     -- created_at
);

-- Insert one row into user_total_time
INSERT INTO user_total_time (user_id, total_time_spent)
VALUES (
    'USER_1',   -- user_id
    5400          -- total_time_spent in seconds
);
