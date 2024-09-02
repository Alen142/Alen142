import string
punc=string.punctuation
str1='pyth%#@$%on pro&*(%$#gramming la@#$%^&%$nguage'
new=''
for i in str1:
    if i not in punc:
        new=new+i
print(new)