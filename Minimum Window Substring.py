class Solution:
    def areEqual(self, req, curr):
        for i in req.keys():
            if curr[i]<req[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        len_s = len(s)
        min_len = len(s)
        answer = ""
        i, j = 0, 0
        req = {x:t.count(x) for x in set(t)}
        curr = {x:0 for x in set(t)}
        while (i<=len_s):
            while (j<=len_s):
                substr = s[i:j]
                len_substr = len(substr)
                if (self.areEqual(req, curr) and len_substr<=min_len):
                    min_len = len_substr
                    answer = substr
                    try:
                        curr[s[i]] -= 1
                    except:
                        pass
                    i += 1
                try:
                    if (curr[s[i]] > req[s[i]]):
                        curr[s[i]] -= 1
                        i = i+1
                except:
                    pass     
                if (self.areEqual(req, curr) == False):
                    if (j-i < min_len):
                        if (j != len_s):
                            try:
                                curr[s[j]] += 1
                            except:
                                pass
                            j = j+1
                        else:
                            if (i != len_s):
                                try:
                                    curr[s[i]] -= 1
                                except:
                                    pass     
                                i += 1     
                            else:
                                break                        
                    else:
                        try:
                            curr[s[i]] -= 1
                        except:
                            pass     
                        i += 1                   
            try:
                curr[s[i]] -= 1
            except:
                pass
            i += 1
        return(answer)
