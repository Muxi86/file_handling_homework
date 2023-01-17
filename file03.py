def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    ans = []
    for i in data:
        i.split(',')
        if i.isdigit():
            ans.append(i)
    return ans
    
# Read data from file
f = open('txt_file/data03.txt')
data = f.read()
print(main(data))