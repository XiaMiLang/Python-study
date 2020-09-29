warning = "That is my car"
print(warning)

print("\\")     # 把\後面出現的符號跳脫，不做處理

print("deleted\b sign")     # \b means backspace character
# \n        newline
# \t        horizontal tabulation 
# \r        把\r後面出現的字通通移到最前並覆蓋
face = '\^_^/'
print(face)  # \^_^/
print(repr(face))  # '\\^_^/'
print("\\\\")