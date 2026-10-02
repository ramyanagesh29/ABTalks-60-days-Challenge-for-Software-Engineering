def max_area_brute_force(h):
    best=0
    for l in range(len(h)):
        for r in range(l+1,len(h)):
            best=max(best,(r-l)*min(h[l],h[r]))
    return best

def max_area_two_pointer(h):
    l=0; r=len(h)-1; best=0
    while l<r:
        best=max(best,(r-l)*min(h[l],h[r]))
        if h[l]<h[r]: l+=1
        else: r-=1
    return best

h=[1,8,6,2,5,4,8,3,7]
print('----- Water Reservoir Architect -----'); print('Wall heights:',h)
print('\nBrute Force:'); print('Maximum area:',max_area_brute_force(h))
print('\nTwo Pointer:'); print('Maximum area:',max_area_two_pointer(h))
print('\nComplexity:'); print('Brute Force: O(N^2) time, O(1) space'); print('Two Pointer: O(N) time, O(1) space')
