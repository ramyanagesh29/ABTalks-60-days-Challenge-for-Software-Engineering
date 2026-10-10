from collections import deque

def can_finish_courses(num_courses, prerequisites):
    # [course, prerequisite] means prerequisite must be done first.
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1

    queue = deque(i for i in range(num_courses) if indegree[i] == 0)
    order = []
    while queue:
        course = queue.popleft()
        order.append(course)
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return len(order) == num_courses, order

if __name__ == "__main__":
    possible, order = can_finish_courses(4, [[1,0], [2,0], [3,1], [3,2]])
    print("University Course Planner")
    print("Can finish all courses:", possible)
    print("Valid course order:", order)
    possible, _ = can_finish_courses(3, [[1,0], [2,1], [0,2]])
    print("Cycle test - can finish all courses:", possible)
