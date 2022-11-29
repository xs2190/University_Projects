import subprocess
import time


#key for test file: 0x0000000000000b92d
def main():
	print("Brute force attempt for 10 minutes...")
	f = open("decypt_results2", "a") 
	start_time = time.time()
	end_time = 600
	
	num = 0x0000000000000001
	while (time.time() - start_time) < end_time:
		result = subprocess.check_output(['./dec2', 'test.txt.enc2', hex(num)])
		result = str(result)
		result = result[2::] #remove extra 2 leading chars
		result = result[:-1:] #remove extra trailing char
		result = str(result) + "\t\tkey: " + hex(num) + "\n"
		f.write(result)
		num += 1
		
	#print("--- %s seconds ---" % current_time)
	print(" %d keys attempted in 10 minutes" % num)
	f.close()
	
main()
	
