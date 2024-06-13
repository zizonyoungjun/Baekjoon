# 세로읽기
# 입력
# 총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다. 주어지는 글자는 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’ 중 하나이다. 각 줄의 시작과 마지막에 빈칸은 없다.

# 출력
# 영석이가 세로로 읽은 순서대로 글자들을 출력한다. 이때, 글자들을 공백 없이 연속해서 출력한다.

words = []
reversed_words = []
reversed_word = ''

for _ in range(5):
    word = input()
    if len(word) < 15:
        for _ in range(15-len(word)):
            word += ' '
    words.append(word)

for i in range(15):
    for w in words:
        reversed_word += w[i]
    reversed_words.append(reversed_word)
    reversed_word = ''

result = ''.join(reversed_words)
result = result.replace(' ', '')

print(result)
