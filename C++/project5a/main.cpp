#include <iostream>
#include <fstream>
#include <list>
//DATE: OCTOBER 3, 2018
//PROJECT 5-A

using namespace std;

string** createStudentArray(const int, const int);
bool compare_gpa(const string*, const string*);
list<string*> createList(string**, const int);
void displayStudentArray(string**, const int, const int);
void displayList(list<string*>&, const int);
void removeId(list<string*>&, string);

int main(){
    const int ROWS = 15, COLUMNS = 4;
    string** studentData = createStudentArray(ROWS, COLUMNS);
    displayStudentArray(studentData, ROWS, COLUMNS);
    list<string*> myList = createList(studentData, ROWS);
    myList.sort(compare_gpa);

    cout << "\n" << "--------------------------------------------";
    cout << "------------------------";
    cout << "\n\nSORTING THE LIST BY ID...\n\n";
    displayList(myList, COLUMNS);

    cout << "--------------------------------------------";
    cout << "------------------------";
    removeId(myList, studentData[14][0]);
    displayList(myList, COLUMNS);

    cout << "\n" << "--------------------------------------------";
    cout << "------------------------";
    cout << "\n\nADDING USER " << studentData[14][0];
    cout << " BACK INTO THE LIST...\n";
    myList.push_back(studentData[14]);
    myList.sort(compare_gpa);
    displayList(myList, COLUMNS);
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
            data[i][C - 1] = line;
            i += 1;
        }
        nameFile.close();
    }
    else{cout << "!!! ERROR NO DATA TO MANIPULATE !!!" << endl;}
    return data;
}

//Comparison function to use in the list container's sort function
bool compare_gpa(const string* first, const string* second){
    return (first[0] < second[0]);
}

list<string*> createList(string** students, const int R){
    list<string*> myList;
    for(int i = 0; i < R; i++) myList.push_back(students[i]);
    return myList;
}

void displayStudentArray(string** students, const int R, const int C){
	cout << "--------------------------------------------";
	cout << "------------------------" << endl;
	cout << "BELOW IS THE UNSORTED ARRAY OF STUDENT DATA." << endl;
	cout << "--------------------------------------------";
	cout << "------------------------" << "\n\n";
	for(int h = 0; h < R; h++){
		for(int i = 0; i < C; i++){
			cout << students[h][i] << "\t";
		}
		cout << endl;
	}
}

void displayList(list<string*>& aList, const int C){
    string* myStrPtr;
    cout << "\n" << "--------------------------------------------";
    cout << "------------------------" << "\n\n";
    for( auto it = aList.begin(); it != aList.end(); ++it){
	myStrPtr = *it;
    	for(int i = 0; i < C; i++){
		cout << myStrPtr[i] << "\t";
	}
	cout << "\n";
    }
}

void removeId(list<string*>& aList, string user){
    string* myStrPtr;
    string* userPtr;
    cout << "\n\nREMOVING USER " << user << " FROM THE LIST...\n\n";
    for( auto it = aList.begin(); it != aList.end(); ++it){
	myStrPtr = *it;
	if(myStrPtr[0] == user) userPtr = myStrPtr;
    }
    aList.remove(userPtr);
}
