def max_average_naive(a,k):
    best=float('-inf')
    for i in range(len(a)-k+1):
        s=0
        for j in range(i,i+k): s+=a[j]
        best=max(best,s)
    return best/k

def max_average_sliding_window(a,k):
    s=sum(a[:k]); best=s
    for right in range(k,len(a)):
        s += a[right]-a[right-k]
        best=max(best,s)
    return best/k

energy=[1,12,-5,-6,50,3]; k=4
print('----- Energy Drink Analyzer -----')
print('Energy readings:',energy); print('Window size:',k)
print('\nNaive Solution:'); print('Maximum average:',max_average_naive(energy,k))
print('\nSliding Window Solution:'); print('Maximum average:',max_average_sliding_window(energy,k))
print('\nComplexity:'); print('Naive: O(N*K) time, O(1) space'); print('Sliding Window: O(N) time, O(1) space')
