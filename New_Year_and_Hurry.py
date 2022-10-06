def main():
    inp = input().split(" ")
    time = (4*60)-int(inp[1])
    result = 0 
    prob = 0
    x = 0
    all = int(inp[0])
    print(time)
    time = time-(time%5)
    print(time,"real")
    while(result < time):
            x+=1
            result = result+(5*x)
            print(result)
            prob+=1
    if(prob>all):
        print(all)
        return all
    else:
        print(prob)
        return prob
    
    

main()
# int time = (4*60)-190;
#        int prob = 0 ;
#        int result = 0;
#        int x=0;
#        int all = 4;
#        while(result < time){
#             x++;
#             result = result+(5*x);
#             prob++;
#        }
#        System.out.println(prob);
#        if(prob>all){
#         System.out.println(all);
#        }else{
#         System.out.println(prob);
#        }

#     }