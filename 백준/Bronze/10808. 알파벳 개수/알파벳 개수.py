#문제 포인트 alphabet.index(i), += 누적

s = list(input())
#단어 입력 :baekjoon
#print(word)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#입력한 단어 알파벳 포함 여부 확인용

alphabet_initial= [0 for _ in range(26)]
#알파벳 리스트 초기화(1로 채울용=>알파벳 갯수세기용)
#[0,0,0,0,0,0,0,0,0....]
#알파벳은 총 26개(인덱스0~26)

for i in s: #[b,a,e,k,j,o,o,n] #b/a/e/k/j/o/o/n 글자 하나씩
    if i in alphabet: #알파벳 리스트에 있니?
        #print(alphabet.index(i)) #있으면 어느 위치에 글자가 있니?
        # 문자열로 인덱스 찾는법
        a = alphabet.index(i) #새 변수에 넣어줘서 식 간편하게 만들고
        # 1,0,4,10,9,14,14,3 = 1의 자리, 0의 자리 ,,,
        alphabet_initial[a] = alphabet_initial[a]+ 1 #갯수 누적하기

for j in alphabet_initial:
     print(j,end=' ')