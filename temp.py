from collections import deque

q = {
    '1' : 'qwe',
    '2' : '23ew',
    '3' : 'cxvc'
}
 
w = ['q', 'wer']
e = deque(w)

# w = ['q', 'wer']
if '2' in q:
    print('Yeah') 
e.popleft()
print(e)
print(e[0])