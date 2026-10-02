def longest_unique_signal(text):
    last_seen={}; left=0; best_len=0; best_start=0
    for right,ch in enumerate(text):
        if ch in last_seen and last_seen[ch]>=left:
            left=last_seen[ch]+1
        last_seen[ch]=right
        if right-left+1>best_len:
            best_len=right-left+1; best_start=left
    return text[best_start:best_start+best_len]

for signal in ['abcabcbb','bbbbb','pwwkew','abcdef']:
    result=longest_unique_signal(signal)
    print('Signal:',signal); print('Longest unique pattern:',result); print('Length:',len(result)); print()
print('Complexity:'); print('Time: O(N)'); print('Space: O(N)')
