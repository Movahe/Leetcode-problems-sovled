"""
Time complexity:
building Trie: O(N*len(s)) where N = len(strs) and s is the longest word in strs
finding longest prefix: O(M) where M is the length of LCP (which is in the range of 0 and
the length of shortest string)
"""


class TrieNode:
    def __init__(self, letter=''):
        self.letter = letter
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode(letter)
            node = node.children[letter]
        node.end = True

    def get_prefix(self, node):
        prefix = node.letter
        while node:
            if node.end or len(node.children) > 1:
                return prefix, node
            child = list(node.children)[0]
            prefix += child
            node = node.children[child]
        return prefix, node

    def print_tree(self, node=None, indent='', mid='└'):
        prefix, node = self.get_prefix(node or self.root)
        if prefix:
            print('{}{}{}'.format(indent, mid if indent else '', prefix))
        for child_node in node.children.values():
            self.print_tree(child_node, indent + (' ' * (len(prefix) - 1)), mid=mid)

    def get_longest_prefix(self):
        longest = ''
        for node in self.root.children.values():
            prefix, _ = self.get_prefix(node)
            if len(prefix) > len(longest):
                longest = prefix
        return str(longest)


def main():
    trie = Trie()
    trie.add_word('flight')
    trie.add_word('flow')
    trie.add_word('flower')
    print(trie.get_longest_prefix())
    trie.print_tree()


if __name__ == '__main__':
    main()