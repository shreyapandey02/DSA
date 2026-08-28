class Solution:
    def isSymmetric(self, root):
        
        def mirror(left, right):
            
            # Dono empty hain
            if left is None and right is None:
                return True
            
            # Sirf ek empty hai
            if left is None or right is None:
                return False
            
            # Values different hain
            if left.val != right.val:
                return False
            
            # Mirror positions compare karo
            return (mirror(left.left, right.right) and
                    mirror(left.right, right.left))
        
        return mirror(root.left, root.right)