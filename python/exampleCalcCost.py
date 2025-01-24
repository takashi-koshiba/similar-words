
class CalcCostStr:
    @staticmethod
    def maxCost(length) :
        cost= (length * (length+ 1) ) / 2;
        return cost-length if length >3 else cost
	
	

    @staticmethod
    def getMaxCost(target,inputTotalCost,splitArr) :

        targetCost=CalcCostStr.maxCost(len(target));
		
        inputCountMatch=CalcCostStr.count_match(splitArr,target);
		
        inputMatchRatio=inputCountMatch/inputTotalCost;
        inputCost=inputMatchRatio*inputCountMatch;
		
        result=inputCost/targetCost;

		
		
        return result;
		
    @staticmethod
    def split_str(string, total_cost):
        
        arr = [total_cost] 
        str_len = len(string) 
        index = 0
    
        for i in range(str_len):
            for ii in range(i + 1, str_len + 1):
                sub_str = string[i:ii] 
                
               
                if str_len > 3 and len(sub_str) <= 1:
                    continue
                
                if index < len(arr):
                    arr[index] = sub_str
                else:
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
    cost=CalcCostStr()
    
    inputStr="ABCDEFG"
    targetStr="ABC"
    
    
    strCost=cost.maxCost(len(inputStr))
    splitStr=cost.split_str(inputStr,strCost)
    
    result = cost.getMaxCost(targetStr, strCost,splitStr)
    
    print(result)
