import shutil

for i in range(100):
    shutil.copy2('textfile1.txt','/users/shashwateshtripathi/PycharmProjects/AI_1/test1folder/textfile{}.txt'.format(i))

