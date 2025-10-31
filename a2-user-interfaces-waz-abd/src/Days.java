
/**
 * 
 * TODO: add JavaDoc
 * 
 * @author 
 *
 */
public final class Days {
	
	public static int howManyDaysInMonth(int month) {
		
		if (month == 2) {
			return 28;
		}	
		
		if (month < 8) {
			if (month % 2 == 0) {
				return 30;
			}
			if (month % 2 == 1) {
				return 31;
			}
		}
		
		if (month == 12) {
			return 31;
		}
		
		
		if (month >= 8) {
			if (month % 2 == 0) {
				return 31;
			}
			if (month % 2 == 1) {
				return 30
			}
		}

	}
	
	/**
	 * Days cannot be instantiated, has static methods only.
	 */
	private Days() {}

}
