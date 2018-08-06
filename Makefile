greeting: 
	g++ -fPIC -shared Greeting/Greeting.cpp -o lib/libgreet.so

living: greeting
	g++ -fPIC -shared Living/Living.cpp -o lib/liblive.so

myapp: living 
	g++ MyApp/main.cpp -Llib -L/root/conan_demo/cpp_greetings/lib -llive -lgreet -o myapp 

