#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <conio.h>
#include <stdlib.h>
using namespace std;

int main() {
    //produces random number(1-100)
    srand(time(0)); 
    int secret_num = (1 + (rand() % 100));
    int num_of_guesses = 0;
    int guess;
    bool running = true;
    
    while(running == true) {
        int guess;
        cout << "Try To Guess My Number! 1-100" << endl;
        cout << "Guesses Used: " << num_of_guesses << endl;
        cout << "#";
        cin >> guess;
        cout << endl;
        if(guess < secret_num) {
            system("CLS");
            cout << "Too Low, Try Again" << endl;
            num_of_guesses++;
        } else if(guess > secret_num) {
            system("CLS");
            cout << "Too High, Try Again" << endl;
            num_of_guesses++;
        } else if(guess == secret_num) {
            system("CLS");
            cout << "You Won! Good Job" <<endl;
            cout << "It Took You " << num_of_guesses << " Tries To Guess My Number" << endl << endl;
            num_of_guesses = 0;
            bool valid_input = false;
            while(valid_input == false) {
                cout << "Would You Like To Play Again?(Y or N)" << endl;
                cout << "#";
                string answer;
                cin >> answer;
                if(answer == "Y") {
                    running = true;
                    valid_input = true;
                } else if (answer == "N") {
                    running = false;
                    valid_input = true;
                }
                system("CLS");
            }
        }
    }
}