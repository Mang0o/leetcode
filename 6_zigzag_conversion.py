class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = (2*numRows-2)
        l = len(s)
        divisor = l//n

        remainder = l%n
        print(divisor,remainder,numRows,n)
        ret = ''
        for j in range(numRows):
            for i in range(divisor+1):
                if j == 0 or j == (numRows - 1):
                    print('========')
                    
                    if i*n+j <= l -1:
                        print(j,i,i*n+j,s[i*n+j])
                        ret+=s[i*n+j]
                else:
                    print('$$$$$$$$')
                    if i*n+j <= l -1:
                        print(j,i,i*n+j,(s[i*n+j]))
                        ret+=s[i*n+j]
                    if (i+1)*n-j <= l -1:
                        ret+=s[(i+1)*n-j]
                        print(j,i,(i+1)*n-j,(s[(i+1)*n-j]))
                    # print(j,i,(s[i*n+j]+s[i*(n+1)-j]))
                    # ret+=(s[i*n+j]+s[i*(n+1)-j])

        return ret

        

def main():
    s = Solution()
    # ss = 'PAYPALISHIRING'
    ss = "heltfchqssrwqgwanggkjlsownsdpoowubszfzratjwlpuldarnmehcbvuemiulcxdedcxfygbjyyxbyqqmvxoyukchszuxwxdbbagzjklhiikiyavvzltwwyfqxzpvwszxvfzerknbuxkszhoaujwqhbjecycyrbyoizucjhddgpxfynftxelehulktnkkqkaajucsdgxjvvoukvphzamjvxtomfacqaezwhuzntkkqagbvxkxywgtvbjjijnylsajzwioruaiujlrgvoguwzrzkbivogggiphgzvytygnhtfnovwkuvctidbdrkkaubhbddzwbhmkatzqqvbktdgbgjezvqzqshtxmutpbhzdcyvvwwhpbnqjxujunkmhtfehzzwchxhlydiubqjddbmcxxzkilrdrvlsvjvehcrfhabjqkmvnaykyxviimnbkyufirlpvcwdcxmsjaowaogandkxsybcwvjgouxjytobscvdclbfzkfonqmfqpjmksvaoslnoaqgelmhxnmyxtnllbsbqcocwjendparrsywdkfazrbxmoiyrczjgplfypseguvymvuphzshsteejoccsclzrwesnyytsttgppvwqpfikjpvztxsxirrgxlvvjpnckttaqqqivbshsogllylwrccopylypaabvwbomuwjxqspezcszpqtrsjgsvgjxhltdohrifchvvyawbuxqkskecszzzkyixrnmagwfiebfcdbfxbyjtipxcoybzxjyowkrcjwnpxstawbzxzisjysloqnpnyoevavzjrmarhutdvtcwdwfdoqsffhuexazyvajpnkiugbzdwdzazedowxvchrgeshephogwaosiqtlmwmowssmopjswayduhhkrxqnzhijxbulyiawauirjtjitk"

    print(ss,len(ss))

    print(ss[740],ss[742],ss[741],)
    # print(s.convert(ss,742))

    print('PAHNAPLSIIGYIR')

if __name__ == '__main__':
    main()