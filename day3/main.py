from io import TextIOWrapper
import re 

# Part one no do and don't
def parse_input(file) -> int:
    res = 0
    valid_mul = None 

    if isinstance(file, TextIOWrapper):
        valid_mul = re.findall(r'mul\(\d+,\d+\)', file.read())
    else:
        valid_mul = re.findall(r'mul\(\d+,\d+\)', file)

    for valid in valid_mul:
        res += mul(int(valid[4:valid.find(",")]), 
                   int(valid[valid.find(",")+1:-1]))
    return res
# Part two do and don't
def enabled_input(file) -> int:
    valid_mul = re.sub(r"don't\(\).*?(do\(\))?", "", file.read()) 
    print(valid_mul)
    res = parse_input(valid_mul)



    return res 

def mul(num1: int, num2: int) -> int:
    return num1 * num2 

if __name__ == "__main__":
    f = open("test.txt")
    
    # res = parse_input(f)
    # print(res)

    res = enabled_input(f)
    print(res)
