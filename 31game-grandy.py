def main() :
    s = input("s?(カンマ区切り)").split(",")
    s = [int(s) for s in s]
    s_len = len(s)
    
    n = int(input("n?"))
    
    grandy = [0] * n
    
    
    #print("0, 0q")
    
    for i in range(1, n) :
        g = list(range(i+1))
        
        for j in s :
            
            if i-j >= 0 :
                if grandy[i-j] in g :
                    g.remove(grandy[i-j])

        #print(i, g)
        
        grandy[i] = min(g)
            
    print(grandy)
    
if __name__ == "__main__" :
    main()
