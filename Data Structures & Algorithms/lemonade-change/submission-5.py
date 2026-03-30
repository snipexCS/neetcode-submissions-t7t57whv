class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        FiveBiils = 0
        TenBiils = 0
        for money in bills:
            if money == 5:
                FiveBiils += 1 
            elif money == 10:
                if FiveBiils:
                    FiveBiils -= 1
                    TenBiils += 1 
                else:
                    return False 
            elif money == 20:
                if FiveBiils and TenBiils:
                    FiveBiils -= 1 
                    TenBiils -= 1 
                elif FiveBiils >= 3 :
                    FiveBiils -= 1
                    FiveBiils -= 1
                    FiveBiils -= 1
                else:
                    return False
                         
        
        return True

        