package src.orders;

public class Order{
	public void getAddr(){
		return deliveryAddr;
	}
	public void setNextOrder(Order next){
		nextOrder = next;
	}
	public Order getNextOrder(){
		return nextOrder;
	}
	public getIngredients(){
		return ingredients;
	}
	public getType(){
		return orderType;
	}
	public Order(){
		nextOrder = null;
	}
	private String deliveryAddr, ingredients, orderType;
	private Order nextOrder;
}
