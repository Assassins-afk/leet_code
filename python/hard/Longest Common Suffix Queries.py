class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.min_len = float("inf")
                self.idx = float("inf")

        class Trie:# данный класс реализует префиксное дерево (trie) для хранения слов в обратном порядке с отслеживанием кратчайшего слова
            def __init__(self):
                self.root = TrieNode()

            def insert(self, s: str, idx: int):# метод вставки перевернутого слова s с индексом idx, обновляющий min_len и idx во всех пройденных узлах
                node = self.root
                if len(s) < node.min_len:
                    node.min_len = len(s)
                    node.idx = idx

                for ch in s:# проходим по каждому символу перевернутого слова от последнего к первому
                    if ch not in node.children:
                        node.children[ch] = TrieNode()
                    node = node.children[ch]

                    if len(s) < node.min_len:
                        node.min_len = len(s)
                        node.idx = idx

        trie = Trie()
        for i, word in enumerate(wordsContainer):# итерируемся по списку слов-контейнеров с их индексами
            trie.insert(word[::-1], i)

        ans = []
        for query in wordsQuery:# проходим по каждому слову-запросу из списка wordsQuery
            node = trie.root
            for ch in query[::-1]:# итерируемся по символам перевернутого запроса (ищем совпадение суффиксов)
                if ch in node.children:# если текущий символ есть среди дочерних узлов
                    node = node.children[ch]
                else:# если символ не найден - дальнейшее совпадение суффикса невозможно
                    break
            ans.append(node.idx)
        return ans