from os import system


print("""

pkg manager

Select options:

1.Update package
2.Install packages
3.Remove packages
4.Search Packages
""")

num = int(input('Enter options:'))
if (num==1):
   system("apt update && apt upgrade -y")
if (num==2):
   pkg = input('Enter app to install:')
   system(f"apt install -y {pkg}")
if (num==3):
   pkg = input('Enter app to remove:')
   system(f"apt remove {pkg} && apt autoremove")
if (num==4):
   pkg = input('What app do you want to search?:')
   system(f"apt search {pkg}")