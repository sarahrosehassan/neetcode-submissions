class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph dictionary (adjacency list from prereq input)
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        # Initialize visiting and claered sets
        visiting = set()
        cleared = set()

        def dfs (course):
            # check if the node you are on is in teh cleared set or the visting set
            if course in cleared:
                return True
            if course in visiting:
                return False
            # add current node to the visiting set
            visiting.add(course)
            # loop through prerequisites
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            # remove from visiting set and add to cleared set
            visiting.remove(course)
            cleared.add(course)
            # return true if no cycles deteced
            return True
            
        # call DFS on every course from 0 to num courses-1
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

            
        