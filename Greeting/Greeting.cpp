#include <iostream>
#include <string>
#include "Greeting.h"

using namespace std;

Greeting::Greeting() {
}

string Greeting::fr() {
  return "Bonjour !";
  
}

string Greeting::en() {
  return "Hello !";
}

/*
int main() {
   Greeting greet;
   cout << greet.fr() << endl;
   cout << greet.en() << endl;
}
*/
