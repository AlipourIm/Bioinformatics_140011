def edit_distance_allignment(s, t):
    # Since I did not come up with a better way of finding s' and t' other than using a matrix and dynamic_prgramming, I chose this method.
    m = len(t)
    n = len(s)
    edit_distance = [[0 for j in range(m + 1)] for i in range(n + 1)]   # We first construct a n+1*n+1 matrix, that +1 is for indels

    for i in range(1, n + 1):   # For first coloumn we set values to other strings current length(till this step)
        edit_distance[i][0] = i
    for i in range(1, m + 1):   # For first row we set values to other strings current length(till this step)
        edit_distance[0][i] = i
    for i in range(1, n + 1):   # Now we construct forward pass to find best path from (0, 0) to (n, m)
        for j in range(1, m + 1):
            if s[i-1] == t[j-1]:
                cost = 0
            else:
                cost = 1
            edit_distance[i][j] = min(edit_distance[i-1][j] + 1, edit_distance[i][j-1] + 1, edit_distance[i-1][j-1] + cost) # As mentioned in the class, we take the minimum of these possibilities

    s_prim = '' # Make s' and t' by inintializing them to empty strings, now compute them with back tracking
    t_prim = ''

    i = n   # Our 2 counters for looping over the whole array
    j = m

    while i*j != 0: # We perform back_tracking to find best path and construct s' and t' (another way for this was to keep a pointer for U(down), D(diag), R(right) in forward pass, since that was mentiond in class I performed another idea :) )
        if edit_distance[i][j] == edit_distance[i-1][j-1] + hamming_distance(s[i-1], t[j-1]):
            s_prim = s[i-1] + s_prim
            t_prim = t[j-1] + t_prim
            i -= 1
            j -= 1
        elif i > 0 and edit_distance[i][j] == edit_distance[i-1][j] + 1:
            s_prim = s[i-1] + s_prim
            t_prim = '-' + t_prim
            i -= 1
        else:
            t_prim = t[j-1] + t_prim
            s_prim = '-' + s_prim
            j -= 1
    return s_prim, t_prim

def hamming_distance(s, t): 
    # Computes hamming distance of two given strings(same length) by performing a loop over one of the strings and counting the matches.
    counter = 0
    count = 0
 
    while(counter < len(s)):
        if(s[counter] != t[counter]):
            count += 1
        counter += 1
    return count

# Test
s = 'PQNDFHWLLVTDRKQFWTMMFWLHGGFSTYVQCIWKNNEPISHHGCKSPLWNNFRAEHCMQFPMIHSMTCTKPIEVFHMIKQYGQVRQIQDGVEGMHRKRERMSANFYLTNAIIMPFRHFMFLMSNFIDMKRVNMPLNGYDWFFDRFLTNDIWTYPFFKPIINFALEWGIGTIFWSAQWCLNPANKLVLAKRWGWKTEWSERNIKWDVDCKAHNCKKQTRPQYLTVKPSRFDMFQLVDCDMKAAPPARTCVMMYNPGATKKEACPSHPKREEDRNLEYEFVCGFWLFSTVLIKVQCGTEFPANRGKEKLTLMFCLVHFGSSPMQVQVTLIPPTKMKGGHRPVFSMAYDYQDNQLWLLVVHFFPAIHSILRGCILWTSLYIGTMQDQMDGHPEDEWLMEEPIEHKKWCSQISKFQKSIPLYQRGSIKPCICVQHGQFPIQPPANCMTMWAFNAQVLSFCMEMHDCTYLFAMVGHHMDCWRWGCISDSGILNPDPAFAVFIPAEQSHGKNAADWDWHADMFQKPQEAFPPNLDMSTMNDYIRRWVWANWLRFWLNVLDHIQRADMGPYGPDIYSGRYVKYGCGSLTWDNYQGGGICHFRSRCWDDYYRGRFTEICWLQPRRQWCYSTNPGVDTGWCHWLFMQPMVMMRSRTGNTTMHFCTSVKITGYAGIPNLYGSAVDWECQYIFHVMGGGKMGKRIGATTGSKQMCSKIMLERLKYPNGLG'
t = 'PQNDFHIAWEWSMWCSTCPQPWTMMFWLHGGFGMWKNNSKSPLWNNFRAEHCMWFPMLHSSDKAMHNCTTQYITIEVFHMVLGPHPKQYGDWSYVPAGGEMYYNSEGHRYPVWDKNFYLTNLIIMPCKCRSRHFMFLMIDWVMSLLSHKRVNMIWLGYDWFFDRFLTHFFKPGIGTIFPSTEHMGKQPEEFSWNAYCYDLAKRWGWKTEWIHTHEERCPKNDVDAHNCKFWTHPSRFYMCLWKQLVDCDMKAAPPARTCVMMKKEAAPVHPEEDINLYEFVCGFWLFSTVPHLVIKVQCGTEFPENRGKEKLTLMFCLNHFGSSPNQAALWPPTKMKGGHRPVFSMAYDRQDNQLWTPILVKLFFPAIHSILRGCILWTSLYIGTMQDQTDGHPGDEWLMEEPIEHKKWCDQISKYQKSIPLYQRGSIKPCICVTFSDTQAHSDSQMAMCPQFPIQPANCMHMWSLSEYWMMEMHDCTSIYCFAMVGHHMQCWDSKYFILNPDPAWVHSNMQAVFIPAEISHGKNAADWDWEQIPQPPNLYQKPYDPCNESTMNCYIRRWVWANWGCFWLNVLYHIQRADMGPYGNAHRIYSVDRHVFRLSKLPAHWDNYQGGGICHFRSRCWDDYYRGRFSEPRRQWCYSTNPGVDTWKGVKALEMMRSRTGNTTMHFCTSVKINFTMELSGLYGSAVDWECQYILHVMGGGKMGKRIGATTGSKHMCSKIMLERLKYPNGLG'

s_prim, t_prim = edit_distance_allignment(s, t) # First find s' and t'
ans = hamming_distance(s_prim, t_prim)  # Now compute hamming distance between s' and t' to find edit_distance
print(ans)
print(s_prim)
print(t_prim)