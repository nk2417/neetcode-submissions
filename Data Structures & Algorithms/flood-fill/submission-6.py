class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]
        if start_color == color:
            return image

        def dfs(r, c):
            # 1. STOP if off the map
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            # 2. STOP if not the original color (also covers "already visited")
            if image[r][c] != start_color:
                return
            # 3. MARK
            image[r][c] = color
            # 4. SPREAD
            for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                dfs(r + dr, c + dc)

        dfs(sr, sc)
        return image