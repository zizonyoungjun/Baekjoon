n = int(input())
cnt = 0

for _ in range(n):
    alphabet_counts = [0] * 26
    word = input()
    checker = False
    past_word = ''
    for i in range(len(word)):
        index = ord(word[i]) - ord('a')
        if word[i] != past_word and alphabet_counts[index] != 0:
            checker = True
            break
        alphabet_counts[index] += 1
        past_word = word[i]
    if checker == True:
        continue
    cnt += 1

print(cnt)
