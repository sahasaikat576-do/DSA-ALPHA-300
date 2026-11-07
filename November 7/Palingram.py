class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        letters = set()

        for ch in sentence:

            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
                letters.add(ch.lower())

        return len(letters) == 26
