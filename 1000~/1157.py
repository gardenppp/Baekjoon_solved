word = input().lower() # baaa
word_list = list(set(word)) # [b,a]
cnt = [] # 각 알파벳의 갯수 리스트
for i in word_list:
    count = word.count(i)
    cnt.append(count) # cnt에 각 알파벳 갯수 추가 [1,3]
if cnt.count(max(cnt)) >=2:
    print('?')
else:
    print(word_list[(cnt.index(max(cnt)))].upper())