import os,shutil
import time
import multiprocessing, threading
import matplotlib.pyplot as plt
import argparser
activethreads = threading.activeCount()
parser = argparse.ArgumentParser()
parser.add_argument('folder1')
parser.add_argument('folder2')
args=parser.parse_args()
path = args.folder1
path22 = args.folder2




def work(file_path, count, path22):
    f = open(file_path, 'r')
    path2 = os.path.join(path22, 'newfile{}'.format(count))
    secondfile = open(path2.format(count), 'w+')
    for line in f:
        secondfile.write(line.upper())
    f.close()
    secondfile.close()
    return None


if __name__ == '__main__':
    X=[]
    Y=[]
    for i in range(1,multiprocessing.cpu_count()+1):
        start = time.time()
        try:
            shutil.rmtree("{}".format(path22))
            os.mkdir(path22)
        except:
            os.mkdir(path22)

        count = 0
        pool = multiprocessing.Pool(i)
        for file in os.listdir(path):
            file_path = f"{path}/{file}"
            count += 1
            pool.apply_async(work, args=(file_path, count, path22,))
        
        pool.close()
        pool.join()
        print("Time taken for process count {} = {}".format(i,round(time.time() - start,4)))
        X.append(i)
        Y.append(round(time.time() - start,4))
    plt.plot(X,Y,color='red')
    plt.title("Time taken for different Process/Cpu count for a 6 Core 12 threaded i7 system")
    plt.ylabel("Time in seconds")
    plt.xlabel("No. of Cpu utilisation")
    plt.show()

