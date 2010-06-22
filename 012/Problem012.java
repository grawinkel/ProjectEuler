public class Problem012 {

	public static int[] primes;
	public static long triangleCnt = 1;
	public static long triangle = 0;
	
	public static void main(String[] args) {
		initPrimes(1000000);
		
		int cnt = 0;
		long t = 0;
		while (cnt < 500){
			t = getNextTriangle();
			cnt = getCnt(t);

			//System.out.printf("t=%d, cnt=%d\n",t,cnt);	

			
		}
		System.out.println("result = " + t);
		
	}
	
	public static int getCnt(long n){
		int cnt = 1;
		long tt = 0;
		int prime = 0;
		for ( int i=0; i < primes.length; i++){
		
			prime = primes[i];
			if (prime > n){
				break;
			}
			tt = n;
			int exp = 0;
			while (tt % prime == 0 ){
				tt = tt / prime;
				exp++;
				if (tt == 1){
					break;
				}
			}
			
			if (exp > 0){
				cnt = cnt * (exp+1);
			}
			
		}	
		return cnt;
	}
	
	public static long getNextTriangle(){
		return triangle += triangleCnt++;
	}
	
	private static void initPrimes(int max){
		long start = System.currentTimeMillis();
		
		boolean[] tmp = new boolean[max];
		
		for (int i=2 ; i< max;i++ ){
			tmp[i] = true;
		}

		tmp[0] = false;
		tmp[1] = false;
		
		int x = 0;
		for (int i = 2; i < max; i++){
			if( tmp[i]){
				x = i;
				for(;;){
					x += i;
					if (x < max){
						tmp[x] = false;
					}else{
						break;
					}
				}
			}
		}
		
		int cnt = 0;
		for (int i = 0; i < max; i++){
			if( tmp[i]){
				cnt++;
			}
		}
		
		primes = new int[cnt];
		
		int j = 0;
		for (int i = 0; i < max; i++){
			if( tmp[i]){
				primes[j++] = i;
			}
		}
		
		
		long end = System.currentTimeMillis();
		System.out.printf("generated %d primes in %d ms\n", cnt, (end-start));
	}
}