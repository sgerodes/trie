class Trie:
    def __init__(self):
        self.edges = dict()
        self.matches = False
        self.word = None

    def is_in_dictionary(self, word):
        current_node = self
        for letter in word:
            if letter not in current_node.edges:
                return False
            current_node = current_node.edges[letter]
        return current_node.matches

    def get_dictionary(self):
        stack = [self]
        dictionary = list()
        while stack:
            curr = stack.pop()
            if curr.matches:
                dictionary.append(curr.word)
            stack.extend(curr.edges.values())
        return dictionary

    @staticmethod
    def create_from_dictionary(dictionary):
        root = Trie()
        for word in dictionary:
            current_node = root
            for letter in word:
                if letter in current_node.edges:
                    current_node = current_node.edges[letter]
                else:
                    current_node.edges[letter] = Trie()
                    current_node = current_node.edges[letter]
            current_node.matches = True
            current_node.word = word
        return root

    def __repr__(self):
        return f"{{'matches': {self.matches}, 'edges': {self.edges}}}"

