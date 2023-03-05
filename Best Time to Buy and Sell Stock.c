int maxProfit(int* prices, int pricesSize){
    int maxprofit=0;
    for(int i=0;i<pricesSize;i++)
    {
        for(int j=i+1;j<pricesSize;j++)
        {
            if((*(data+j)-*(data+i))>maxprofit)
            {
                maxprofit=*(data+j)-*(data+i);
            }
        }
    }
    return maxprofit;
}
