from  collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        prereqsLeft = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            prereqsLeft[course] += 1
        
        queue = deque(course for course in range(numCourses) if prereqsLeft[course] == 0)
        coursesTaken = 0

        # take every course with 0 prereqs left
        # then subtract a prereq from its postreqs and add those to the queue
        # if there are zero prereqs left
        while queue:
            course = queue.pop()
            coursesTaken += 1
            for nxt in graph[course]:
                prereqsLeft[nxt] -= 1
                if prereqsLeft[nxt] == 0:
                    queue.append(nxt)

        # return True iff the proper number of courses is taken
        return coursesTaken == numCourses
