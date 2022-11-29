package src.orders;

public class Pizza extends Order{
	public Pizza( String ing, String addr){
		delivAddr = addr;
		ingredients = ing;
		orderType = "pizza";
	}
}
