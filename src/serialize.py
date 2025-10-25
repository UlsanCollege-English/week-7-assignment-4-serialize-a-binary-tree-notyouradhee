class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    # TODO: preorder with '#' for None, space-separated
    # preorder traversal: node, left, right
    if root is None:
        return '#'

    tokens = []

    def visit(node):
        if node is None:
            tokens.append('#')
            return
        tokens.append(str(node.val))
        visit(node.left)
        visit(node.right)

    visit(root)
    return ' '.join(tokens)

def deserialize(s):
    # TODO: rebuild from tokens
    if s is None:
        return None

    s = s.strip()
    if s == '':
        return None

    tokens = iter(s.split())

    def is_int(tok):
        # integer includes optional leading -
        if tok.startswith('-'):
            return tok[1:].isdigit() and len(tok) > 1
        return tok.isdigit()

    def build():
        try:
            tok = next(tokens)
        except StopIteration:
            return None

        if tok == '#':
            return None

        val = int(tok) if is_int(tok) else tok
        node = Node(val)
        node.left = build()
        node.right = build()
        return node

    return build()
