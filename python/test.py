import sys
class SimilarWards:
    @staticmethod
    def maxLength(length,isShort) :
        cost= (length * (length+ 1) ) / 2;
        return cost if isShort else cost-length
	
	

    @staticmethod
    def exec(target,inputTotalCost,splitArr,isShort) :

        targetCost=similarWards.maxLength(len(target),isShort);
        inputCountMatch=similarWards.count_match(splitArr,target);
		
        inputMatchRatio=inputCountMatch/inputTotalCost;
        inputCost=inputMatchRatio*inputCountMatch;
		
        result=inputCost/targetCost;

		
		
        return result;
		
    @staticmethod
    def split_str(string, total_cost,isShort):
        arr=[]
        
        

        str_len = len(string) 
        index = 0
    
        for i in range(str_len):
            for ii in range(i + 1, str_len + 1):
                sub_str = string[i:ii] 
                
               
                if not isShort and len(sub_str) <= 1:
                    continue
                
                arr.append(sub_str) 
                
                index += 1
        
        return arr

    @staticmethod
    def count_match(search_arr, target):
        count = 0
        for item in search_arr:
            if item in target: 
                count += 1
        return count

	

if __name__ == "__main__":
    similarWards=SimilarWards()
    
    args = sys.argv
    inputStr=args[1]
    targetStr=args[2]
    inputLen=len(inputStr)
    isShort=inputLen<4
    
    strMaxLen=similarWards.maxLength(inputLen,isShort)
    splitStr=similarWards.split_str(inputStr,strMaxLen,isShort)
    
    result = similarWards.exec(targetStr, strMaxLen,splitStr,isShort)
    
    print(result)
