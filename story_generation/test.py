files = ['test1.txt', 'test2.txt', 'test.txt', 'content.txt', 'stor5.txt']
storyNames = 'test'
name = files[4]

print(name[4:-4])
print(len(name) >= len(storyNames) + 5 and name[:len(storyNames)] == storyNames and name[4:-4].isnumeric())
print(int(name[4:-4]) if len(name) >= len(storyNames) + 5 and name[:len(storyNames)] == storyNames and name[4:-4].isnumeric() else 0)



print(max([int(name[4:-4]) if len(name) >= len(storyNames) + 5 and name[:len(storyNames)] == storyNames and name[4:-4].isnumeric() else 0 for name in files]) + 1)