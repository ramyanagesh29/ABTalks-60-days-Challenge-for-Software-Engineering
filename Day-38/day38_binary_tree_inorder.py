class Node:
    def __init__(self,data): self.data=data; self.left=None; self.right=None

def inorder_recursive(root,result):
    if root is None: return
    inorder_recursive(root.left,result); result.append(root.data); inorder_recursive(root.right,result)

def inorder_iterative(root):
    result=[]; stack=[]; current=root
    while current is not None or stack:
        while current is not None:
            stack.append(current); current=current.left
        current=stack.pop(); result.append(current.data); current=current.right
    return result

root=Node('King'); root.left=Node('Prince A'); root.right=Node('Prince B')
root.left.left=Node('Princess C'); root.left.right=Node('Princess D')
root.right.left=Node('Prince E'); root.right.right=Node('Princess F')
recursive=[]; inorder_recursive(root,recursive); iterative=inorder_iterative(root)
print('----- Ancient Kingdom Family Tree -----')
print('\nInorder Recursive:'); print(' -> '.join(recursive))
print('\nInorder Iterative:'); print(' -> '.join(iterative))
print('\nResults match:',recursive==iterative)
print('\nComplexity:'); print('Time: O(N)'); print('Recursive space: O(H) call stack'); print('Iterative space: O(H) explicit stack')
