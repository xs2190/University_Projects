#include <iostream>
#include <fstream>
#include <stack>
//AUTHOR: SHELBY JORDAN
//DATE: OCTOBER 3, 2018
//PROJECT 5-B
using namespace std;

string** createStudentArray(const int, const int);
void displayStudentArray(string**, const int, const int);
stack<string*> createStack(string**&, const int);
void displayStack(stack<string*>, const int);
void popSpecificNum(stack<string*>&, int, const int);

int main(){
	const int ROWS = 15, COLUMNS = 5;
	int num = 5;
	string** studentData = createStudentArray(ROWS, COLUMNS);
	displayStudentArray(studentData, ROWS, COLUMNS);

	cout << "\n\nADDING THE ARRAY TO THE STACK...\n";
	stack<string*> studentStack = createStack(studentData, ROWS);
	displayStack(studentStack, COLUMNS);

	cout << "\n\nREMOVING 5 ITEMS FROM THE STACK...\n";
	popSpecificNum(studentStack, num, COLUMNS);
	displayStack(studentStack, COLUMNS);


return 0;
}

string** createStudentArray(const int R, const int C){
    fstream nameFile;
    string** data;
    string line;

    nameFile.open("studentInfo.txt", ios::in);
    if (nameFile){
        data = new string*[R];
        for(int h = 0; h < R; h++){
            data[h] = new string[C];
        }

        int i = 0;
        while(!nameFile.eof() && i < R){
            for(int j = 0; j < C - 1; j++){
            getline(nameFile, line, ',');
            data[i][j] = line;
            }
            getline(nameFile, line);
            data[i][4] = line;
            i += 1;
        }
        nameFile.close();
    }
    else{cout << "!!! ERROR NO DATA TO MANIPULATE !!!" << endl;}
    return data;
}

void displayStudentArray(string** students, const int R, const int C){
	cout << "--------------------------------------------";
	cout << "------------------------" << endl;
	cout << "BELOW IS THE UNSORTED ARRAY OF STUDENT DATA" << endl;
	cout << "--------------------------------------------";
	cout << "------------------------" << "\n\n";
	for(int h = 0; h < R; h++){
		for(int i = 0; i < C; i++){
			cout << students[h][i] << "\t";
		}
		cout << endl;
	}
}

stack<string*> createStack(string**& student, const int R){
	stack<string*> myStack;
	for(int i = 0; i < R; i++) myStack.push(student[i]);
	return myStack;
}

void displayStack(stack<string*> aStack, const int C){
	stack<string*> tempStack = aStack;
	string* myPtr;
	cout << "\nBELOW IS THE STACK'S CONTENTS\n\n\n";
	while(!tempStack.empty()){
		myPtr = tempStack.top();
		for(int j = 0; j < C; j++){
			cout << myPtr[j] << "\t";
		}
		tempStack.pop();
		cout << "\n";
	}	
}

void popSpecificNum(stack<string*>& aStack, int amount, const int C){
	string* tempPtr;
	for(int i = 0; i < amount; i++){
		tempPtr = aStack.top();
		cout << "\nPOPPING...\n";
		for(int j = 0; j < C; j++){
			cout << tempPtr[j] << "\t";
		}
		aStack.pop();
		cout << "\n****************************************";
		cout << "******************************************";
		cout << "******************************************";
		cout << "******************\n";
	}
}
