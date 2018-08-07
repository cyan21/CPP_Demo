#ifndef LIVING_H__
#define LIVING_H__

#include <string>
#include "Greeting.h"

using namespace std;

class Living {
   private :
	    Greeting greet;
   public:
            Living();
            string dit();
            string says();
};
#endif
