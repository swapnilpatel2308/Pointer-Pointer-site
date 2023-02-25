import os

c = 276
def main():
    global c
    folder = r"DATA"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{str(c)}.jpg"
        src =f"{folder}/{filename}" 
        dst =f"{folder}/{dst}"
        os.rename(src, dst)
        c = c + 1
 
main()