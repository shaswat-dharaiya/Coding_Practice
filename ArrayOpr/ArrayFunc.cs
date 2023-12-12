using System;
public class ArrayFunc {
    public bool ContainsDuplicate(int[] nums) {
        Dictionary<int,bool> dict = new Dictionary<int,bool>();
        foreach(var val in nums)
        {
            if(dict.TryGetValue(val, out var valbool))
                return true;
            dict[val] = true;
        }

        return false;
    }
        
}