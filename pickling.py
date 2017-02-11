# pickling and unpickling

import pickle

outfile=open("pickle.dat","wb")
pickle.dump(45,outfile)
pickle.dump(26.5,outfile)
pickle.dump("NMAMIT Nitte",outfile)
pickle.dump([1,2,3,4],outfile)
pickle.dump({'name':'sandy','job':'hancker'},outfile)

outfile.close()
