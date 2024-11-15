#include <iostream>
#include <conio.h>
#include <windows.h>

class Brain {
public:
    void learn() {
        // Learning algorithm
    }
};

class Runner {
public:
    Runner() : x(5), y(10), speed(1), punishment(0) {}

    void update() {
        brain.learn();
        x += speed;
        if (x > 75) {
            x = 0;
        }
        if (y > 20) {
            resetPosition();
        }
    }

    void display() {
        system("cls");
        for (int i = 0; i < y; ++i) {
            std::cout << std::endl;
        }
        for (int i = 0; i < x; ++i) {
            std::cout << " ";
        }
        std::cout << "O" << std::endl; // Head
        for (int i = 0; i < x; ++i) {
            std::cout << " ";
        }
        std::cout << "|" << std::endl; // Body
        for (int i = 0; i < x - 1; ++i) {
            std::cout << " ";
        }
        std::cout << "/|\\" << std::endl; // Arms
        for (int i = 0; i < x - 1; ++i) {
            std::cout << " ";
        }
        std::cout << "/ \\" << std::endl; // Legs

        std::cout << "Punishment: " << punishment << std::endl;
    }

    void resetPosition() {
        x = 5;
        y = 10;
        punishment++;
    }

private:
    int x, y;
    int speed;
    int punishment;
    Brain brain;
};

int main() {
    Runner runner;

    while (true) {
        runner.update();
        runner.display();
        Sleep(100); // Delay to slow down the animation
    }

    return 0;
}
