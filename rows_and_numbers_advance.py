a = input("Please tell me your name\n")
result = ""
for i, s in enumerate(a):
    if i % 2 == 0:
        result += s.upper()
    else:
        result += s
print(result)


print(result.strip())


b = f"hello {result} how are you?"
print(b.capitalize())


print(len(result.strip()))


print(result[::-1])
