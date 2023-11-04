class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Ordena a lista de intervalos com o segundo item(final) na lista de maneira crescente, pois sera pego o intervalo que acabar primeiro
        if len(intervals) == 0:
            return 0
        sort_by_finish_time = sorted(intervals, key = lambda lst: lst[1])
        
        # Inicia max_intervals que contem os intevalos compatíveis
        max_intervals = [sort_by_finish_time.pop(0)]
        
        # for para o resto dos items ordenados para achar intervalos compativeis
        for item in sort_by_finish_time:
            current = max_intervals[-1]
            if item[0] >= current[1]:
                max_intervals.append(item)

        # retorna a quantidade de intervalos que sobrepoem e devem ser removidos
        return len(intervals) - len(max_intervals)
    

#status saída: accepted runtime 990 ms, memory 59.74 mb
#Testes

sol = Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(sol.eraseOverlapIntervals([[1,2],[2,3]]))