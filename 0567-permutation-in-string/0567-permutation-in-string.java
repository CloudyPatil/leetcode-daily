class Solution {
    public boolean checkInclusion(String s1, String s2) {
        HashMap<Character, Integer> need = new HashMap<>();
        HashMap<Character, Integer> window = new HashMap<>();
        int left = 0;
        for(char ch: s1.toCharArray())
        {
            need.put(ch, need.getOrDefault(ch, 0) + 1);
        }
        for(int right=0; right<s2.length(); right++)
        {
            char rightChar = s2.charAt(right);
            window.put(rightChar, window.getOrDefault(rightChar, 0) + 1);

            if(right - left + 1 > s1.length())
            {
                char leftChar = s2.charAt(left);
                window.put(leftChar, window.get(leftChar) - 1);
                if(window.get(leftChar)==0)
                {
                    window.remove(leftChar);
                }
                left ++;
            }
            if(need.equals(window))
            {
                return true;
            }

        }
        return false;
    }
}