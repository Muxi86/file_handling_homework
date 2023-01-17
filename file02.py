def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    ans = 0
    for i in data:
        ans += 1
    return ans

# Read data from file
f = open('txt_file/data02.txt')
data = f.read()
print(main(data))