#include <cctype>
#include "studentData.h"
//DATE: OCTOBER 3, 2018
//PROJECT 6
using namespace std;

void displayMenu(char&);
void searchByMenu(int&, string&);


//SHOW THE AMOUNT OF ITERATIONS
int main(){
	const int ROWS = 20, COLUMNS = 5;
	char choice;
	int location, result;
	string searchID;
	StudentData myData(ROWS, COLUMNS, "studentInfo.txt");

	do{
		displayMenu(choice);
		if(choice == 'a'&& myData.getSize() > 0) myData.displayStudentData();
		else if(choice == 'b' && myData.getSize() > 0){
			searchByMenu(location, searchID);
			result = myData.searchData(0, ROWS, location,searchID);
			if(result == -1){
				cout << "User ID not found after " << myData.getTotalIters();
				cout << " iterations.\n\n";
				myData.resetIter();
			}
			else {
				cout << "\nThe user was found at location " << result + 1 << endl;
				cout << "It took " << myData.getTotalIters() << " iterations";
				cout << " to find the student\n\n";
				myData.resetIter();
			}
		}
		else if(choice == 'c') cout << "\n\n PROGRAM TERMINATING!\n";
	}while(choice != 'c');

return 0;
}

void displayMenu(char& choice){
	bool valid;
	do{
		cout << "Select from the following options: \n";
		cout << "--------------------------------------\n";
		cout << "--------------------------------------\n";
		cout << " a) Display the uploaded student data.\n";
		cout << " b) Search for a student.\n";
		cout << " c) End the program.\n";
		cin >> choice;
		choice = tolower(choice);

		// 97 == a, 101 == e
		// Validate the option
		if(choice > 96 && choice < 102) valid = true;
		else cout << "\nERROR! INVALID OPTION! TRY AGAIN!\n\n";
	}while(!valid);
}

void searchByMenu(int& location, string& str){
	bool valid;
	char choice;
	do{
		cout << "\nWhich of the following criteria would you like to search by?\n\n";
		cout << "------------------------------------------------------------\n";
		cout << "1) Search by ID.\n";
		cout << "2) Cancel Search.\n";
		cin >> choice;
		if(choice == '1'){
			location = 0;
			cout << "\nPlease enter the user ID you wish to find: \n";
			cin >> str;
			valid = true;
		}
		else if(choice == '2'){
			cout << "Search terminated, returning to main menu...\n\n";
			valid = true;
		}
		else cout << "INVALID OPTION! PLEASE CHOOSE A VALID OPTION!\n\n";
	}while(!valid);
}

