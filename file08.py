def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data = data.split('\n')
    maxi = len(data[0])
    for i in data:
        if i.isdigit():
            maxi = len(i)
            if maxi < len(i):
                maxi = len(i)
    return maxi

# Read data from file
f = open('txt_file/data08.txt')
data = f.read()
print(main(data))