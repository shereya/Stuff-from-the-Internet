//Passed 102 testcases out of 160
long long totalCost(int* costs, int costsSize, int k, int candidates){
    int tcosts = 0;
    int smallest = *(costs+0);
    int index = 0;
    for(int i=0;i<k;i++){
        if(i>0){
            if(*(costs+0)<1)
            {
                for(int j=0;j<costsSize;j++)
                {
                    if(*(costs+j)!=0){
                        smallest=(*(costs+j));
                        break;
                    }
                }
            }
            else{
                smallest=*(costs+0);
                index=0;
            }
        }
        for(int j=0;j<costsSize;j++)
        {
            if(*(costs+j)<smallest&&*(costs+j)!=0){
                smallest = *(costs+j);
            }
        }
        for(int j=0;j<costsSize;j++)
        {
            if(*(costs+j)==smallest)
            {
                *(costs+j)=0;
                break;
            }
        }
        tcosts=tcosts+smallest;
    }
    return tcosts;
}
