if __name__ == "__main__":
    
    inp = open("high_security.txt")
    output = open("output.txt", 'w+')
    
    T = int(inp.readline())
    for i in range(0, T):
        N = int(inp.readline())
        G1 = inp.readline()
        G2 = inp.readline()
        
        
                
        segment_len1 = [0] * N
        segment_len2 = [0] * N
        new_segment_1 = True
        new_segment_2 = True
        guards = 0
        
        for j in range(0, N):            
            if G1[j] == '.':
                if new_segment_1:
                    guards += 1
                    new_segment_1 = False
                segment_len1[j] = 1 if j == 0 else segment_len1[j-1] + 1
            else:
                segment_len1[j] = 0
                new_segment_1 = True
                
            if G2[j] == '.':
                if new_segment_2:
                    guards += 1
                    new_segment_2 = False                
                segment_len2[j] = 1 if j == 0 else segment_len2[j-1] + 1
            else:
                segment_len2[j] = 0
                new_segment_2 = True
                
        for j in range(0, N):
            k = N - 1 - j
            if(k < N - 1 and segment_len1[k] > 0 and segment_len1[k + 1] > 0):
                segment_len1[k] = segment_len1[k + 1]
            if(k < N - 1 and segment_len2[k] > 0 and segment_len2[k + 1] > 0):
                segment_len2[k] = segment_len2[k + 1]
        
        wait_reset1 = False
        wait_reset2 = False
        for j in range(0, N):
            if(segment_len1[j] == 0):
                wait_reset1 = False
                
            if(segment_len2[j] == 0):
                wait_reset2 = False
                    
            if(segment_len1[j] == 1 and segment_len2[j] > 0) or (segment_len2[j] == 1 and segment_len1[j] > 0):
                if not wait_reset1 and not wait_reset2:
                    guards -= 1
                    wait_reset1 = True
                    wait_reset2 = True
        
        output.write("Case #{0}: {1}\n".format(i + 1, guards))
