#include <iostream>
#include <fstream>
using namespace std;

struct Row {
  int birth_year;
  int death_year;
};

int main(int argc, char** argv) {
  ifstream file("../presidents.csv");

  string str; 
  while (std::getline(file, str))
  {
    cout << str << endl;
  }
  file.close();

  return 0;
}

