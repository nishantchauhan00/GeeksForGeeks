class Solver:
    def __init__(self, words, n, inp, n1):
        self.out = ""
        self.words = words
        self.n1 = n1
        self.inp = inp

    # Recursion
    # slow, gives tle
    def helper(self, word, i):
        if (word in self.words) and (len(word) > len(self.out)):
            self.out = word
        if i == self.n1:
            return

        self.helper(word + self.inp[i], i + 1)
        self.helper(word, i + 1)

    # loop
    # instead of checking word in dictionary check dictionary in word
    def helper2(self):
        def check(word):
            i, j, n = 0, 0, len(word)
            while j < self.n1:
                if word[i] == self.inp[j]:
                    i += 1
                if i == n:
                    return True
                j += 1
            return False

        # if length of current output is less than length of current word to
        # check, then pass / continue / don't check it
        for word in self.words:
            if (len(word) > len(self.out)) and check(word):
                self.out = word


T = int(input())
for _ in range(T):
    n = int(input())
    words = input().split()
    inp = input()

    s = Solver(words, n, inp, len(inp))
    # s.helper("", 0)
    s.helper2()
    print(s.out)
