n=int(input("Enter number of books:"))
books=[]
author=[]
for i in range(n):
    books.append(input("enter book name: "))
    author.append(input("Enter Author Name:"))
print("Book",' ','Author')
for i in range(n):
    print(books[i]," ",author[i],end="\n")