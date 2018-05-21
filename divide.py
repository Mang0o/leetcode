

def divide(numerator,denominator):
    if denominator == 0:
        return 'Divide by zero!'

    if numerator == 0:
        return '0'

    sign = (numerator/abs(numerator))*(denominator/abs(denominator))

    numerator = abs(numerator)
    denominator = abs(denominator)
    record = []
    
    if numerator > denominator:
        ret = helper(numerator,denominator,record)
    else:
        ret = '0' + helper(numerator,denominator,record)

    if not len(str(numerator//denominator)) == len(ret):
        ret = ret[:len(str(numerator//denominator))]+'.'+ret[len(str(numerator//denominator)):]

    # print(record,len(str(numerator//denominator)),len(ret))
    if record:
        first = record[-1]
        count = 0
        flag = False
        for i in record[::-1][1:]:
            count += 1
            if i == first:
                flag = True
                break
        if flag:
            ret = ret[:-count] + '('+ret[-count:]+')'

    if sign == -1:
        ret = '-'+ret
    return ret

def helper(numerator,denominator,record):
    if numerator == 0:
        return ''
    if numerator < denominator:
        if numerator in record:
            record.append(numerator)
            return ''
        record.append(numerator)
        if numerator*10 >= denominator:
            return helper(numerator*10,denominator,record)
        else:
            return '0' + helper(numerator*10,denominator,record)
    else:
        return str(numerator//denominator)+helper(numerator%denominator,denominator,record)


if __name__ == '__main__':
    print(divide(-1,2))
