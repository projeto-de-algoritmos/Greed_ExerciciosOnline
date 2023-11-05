import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=lambda x: x[1])
    
        currentDay = 0
        coursesQ = []
        totalDuration = 0

        for duration, deadline in courses:
            if currentDay + duration <= deadline:
                currentDay += duration
                totalDuration += duration
                heapq.heappush(coursesQ, -duration)
            elif coursesQ and -coursesQ[0] > duration:
                poppedDuration = heapq.heappop(coursesQ)
                currentDay += duration + poppedDuration
                totalDuration += duration - poppedDuration
                heapq.heappush(coursesQ, -duration)
        
        count = len(coursesQ)
        del coursesQ

        return count