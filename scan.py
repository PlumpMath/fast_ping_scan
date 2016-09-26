from ping import do_one
from multiprocessing import Pool

def f(b, x):
  return do_one('%s.%d'%(b, x))

if __name__ == '__main__':
  from sys import argv
  from time import time
  t=time()
  with Pool(32) as pool:
    res = [pool.apply_async(f, (argv[1], i)) for i in range(2, 255)]#list(range(2,255))))
    res = [res.get(timeout=3) for res in res]
    for i in range(len(res)):
      if res[i]: print('%s.%d\t%f' % (argv[1], i+2, res[i]))
  print(time()-t, 'seconds')
