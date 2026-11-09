class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Problem restated: Find a rectangle with the maximum area

        Edge cases:
        - All heights are 0
        - All heights but one are 0

        Pattern: Two pointers

        Solution O(n^2):
            Start L at 0, R at 1
            1. Calculate the area
            2. Update max area
            3. Increment R
            4. Repeat from 1 until R is at the end
            5. Increment L and start at 1

        Solution O(n)
            Start L at start, R at end
            1. Calculate the area and update the max
            2. Increment/Decrement the pointer with the shortest height value
            3. Repeat until pointers cross or out of bounds

            Step 2 is the trick to getting it efficient
        """
        # Solution O(n)
        m_area, l, r = 0, 0, len(heights)-1
        while l<r and l < len(heights) and r < len(heights):
            m_area = max(
                m_area, 
                (r-l) * min( heights[l], heights[r] )
            )
            if heights[l]<heights[r]: l+=1
            else: r-=1 # heights[l]<=heights[r]

        return m_area

        # Solution O(n^2)
        m_area = 0
        for l in range(len(heights)):
            for r in range(l+1,len(heights)):
                m_area = max(
                    m_area, 
                    (r-l) * min( heights[l], heights[r] )
                )

        return m_area