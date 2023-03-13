def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    lst = []
    for i in data:
        i.split('\n')
        if i.isdigit():
            lst.append(i)
    return max(lst)

# Read data from file
f = open('txt_file/data08.txt')
data = f.read()
print(main(data))