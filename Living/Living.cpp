#include <iostream>
#include <string>
#include "Living.h"

using namespace std;

Living::Living() {

}

string Living::dit() {
  return "Humain dit " + greet.fr();
}

string Living::says() {
  return "Human says " + greet.en();
}

/*
int main() {
   Living liv;
   cout << liv.dit() << endl;
   cout << liv.says() << endl;
}
*/
