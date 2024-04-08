class Solution:
    def optimalStrategyOfGame(self, n, arr):
        self.memoize = [[-1 for _ in range(n)] for _ in range(n)]
        return self.maximumAmountHelper(arr, 0, n - 1)
        
        
    def maximumAmountHelper(self, arr, left_index, right_index):
        
        if left_index > right_index:
            return 0
        if left_index == right_index:
            return arr[left_index]

        if self.memoize[left_index][right_index] != -1:
            return self.memoize[left_index][right_index]

            
        # Else usual case
        take_left = arr[left_index] + min( self.maximumAmountHelper(arr, left_index+2, right_index), \
                                        self.maximumAmountHelper(arr, left_index+1, right_index-1) )
                                        
        take_right = arr[right_index] + min( self.maximumAmountHelper(arr, left_index, right_index-2), \
                                        self.maximumAmountHelper(arr, left_index+1, right_index-1) )
        
        best_move = max(take_left, take_right)
                                        
        if self.memoize[left_index][right_index] == -1:
            self.memoize[left_index][right_index] = best_move
        
        return best_move
