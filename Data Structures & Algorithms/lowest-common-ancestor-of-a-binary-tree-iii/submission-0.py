
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        a = p
        b = q

        while a is not b:

            if a is None:
                a = q
            else:
                a = a.parent

            if b is None:
                b = p
            else:
                b = b.parent

        return a
