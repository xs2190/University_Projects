package src.orders;

public class OrderQue(){
	private Order deque(){
		Order orderToDeliver = null;
		if(first != null){
			orderToDeliver = first;
			first = first.getNextOrder;
		}
		if(first == null) last = null;
		return orderToDeliver;
	}
	public void deliver( Order deliveredOrder){
		if(deliveredOrder = first){
			order thisOrder = deque();
			if(thisOrder = null){
				System.out.println("No deliveries pending");
			}
			deliveredOrder = null;
			System.out.print("Deliver a " + thisOrder.getType() + " with ");
			System.out.printl( thisOrder.getIngredients() + " to " + thisOrder.getAddr());
		}
		else System.out.println("Error, that order is not first in the que.");
	public void enqueue( Order newOrder){
		if(first == null){
		       	first = last = newOrder;
		}
		else last.setNextOrder(newOrder);
		last = newOrder;
	}
	public OrderQue(){
		first = last = null;
	}
	private Order first, last;
}
