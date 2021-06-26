N=int(input())

list1=list(map(int, input().split()))
list2=list(set(list1))
list3=[]

list2=sorted(list2)# 병합정렬 퀵정렬  등을 시도했을때 시간초과라 내장함수를 사용
#중복 없이 list1의 요소를 정렬함. 이렇게 되면 요소의 인덱스가 곧 압축 값이 됨

for i in range(0,len(list2)):
    list3.append((list2[i],i))

list3=dict(list3)# list2의 원소와 그 인덱스값을 딕셔너리로 처리
    
for key in list1: #list1(최초 input 리스트)를 압축값으로 변환
    print(list3[key], end=' ')
