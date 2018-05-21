def reverse(s):
    return ' '.join([i[::-1] for i in s.split()[::-1]])
    

if __name__ == '__main__':
    print(reverse('abc def ghij klmn opq'))
    print('abc def ghij klmn opq'[::-1])