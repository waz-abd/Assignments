/**
 * Class representing command-line interface to compute 
 * yearly and daily compounded certificate of deposit.
 *  
 * @author 
 *
 */
public class BankCDApp {
	
	private BankCD bank;
	private InteractiveCLI cli;
	
	public BankCDApp() {
		
		cli = new InteractiveCLI();
	}
	
	public void run() {
		//TODO: add code here
	}

	public static void main(String[] args) {
		
		BankCDApp app = new BankCDApp();
		app.run();
		

	}

}
