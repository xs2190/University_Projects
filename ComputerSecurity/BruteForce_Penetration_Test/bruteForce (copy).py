import subprocess
import time


#key 0x0000000000000b92d
def main():
	f = open("decypt_results2", "a") 
	
	num = 0x0000000000000001
	while num != 0x0000000000000b92e:
		result = subprocess.check_output(['./dec2', 'test.txt.enc2', hex(num)])
		result = str(result)
		result = result[2::] #remove extra 2 leading chars
		result = result[:-1:] #remove extra 1 trailing char
		result = str(result) + "\t\tkey: " + hex(num) + "\n"
		#print(result)
		f.write(result)
		num += 1
		
	print("--- %s seconds ---" % (time.time() - start_time))
	print(" %d keys attempted, 2 successful? Wonder why..." % num)
	f.close()
	
	
	
	
main()
	
