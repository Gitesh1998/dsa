#include <assert.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#include "cust.h"
#include "pqueue.h"

struct Checker
{
    int m_cash;
    int m_done_time;
    Cust *m_cust;
};

const int COST_PER_ITEM = 3;
const int SHOP_TIME_PER_ITEM = 2;
const int CHECKOUT_TIME_PER_ITEM = 1;
const int ROB_TIME = 7;
const int STARTING_CHECKER_CASH = 250;

void read_input(ifstream &ifile, PQueue &arrivalPQueue)
{
    string buffer;
    // get single line till last line of file
    while (getline(ifile, buffer, '\n'))
    {
        istringstream iss(buffer);
        vector<string> tokens;
        string token;
        // create string vector by spliting using spaces
        while (iss >> token)
        {
            tokens.push_back(token);
        }
        string name = tokens[0];
        bool isRobber = true;
        if ((tokens[1] != "shopper") && (tokens[1] != "robber"))
            exit(-1);

        if (tokens[1] == "shopper")
            isRobber = false;

        int arrivalTime = 0;
        int itemCount = 0;
        // try to convert string num to integer and assign to appropriate variable
        arrivalTime = stoi(tokens[2]);
        itemCount = stoi(tokens[3]);

        // create cust object and push into arrival queue
        Cust *cust = new Cust(
            name, isRobber, arrivalTime,
            itemCount, SHOP_TIME_PER_ITEM,
            CHECKOUT_TIME_PER_ITEM, ROB_TIME);
        arrivalPQueue.enqueue(cust, arrivalTime);
    }
}

// check string is made of digits
// input string as reference
// return true if all char is digit otherwise false
bool isInteger(const string &str)
{
    for (char c : str)
    {
        if (!isdigit(c))
        {
            return false;
        }
    }
    return true;
}

// set arg variable to specified variable
// input totalCheckers, checkerBreakTime, input file, outfile and cmd arguments as reference
// and also check that cmd arguments are correct or not
void setArgvEle(int &totalCheckers, int &checkerBreakTime,
                ifstream &inputFile, ofstream &outputFile, char *argv[])
{
    // if cmd argument is integer then convert into string otherwise throw error and exit
    if (isInteger(argv[1]))
    {
        totalCheckers = stoi(argv[1]);
        if (totalCheckers < 1)
        {
            cerr << "Error: invalid number of checkers specified." << endl;
            exit(1);
        }
    }
    else
    {
        cerr << "Error: invalid number of checkers specified." << endl;
        exit(1);
    }

    // if cmd argument is integer then convert into string otherwise throw error and exit
    if (isInteger(argv[2]))
    {
        checkerBreakTime = stoi(argv[2]);
        if (checkerBreakTime < 0)
        {
            cerr << "Error: invalid number of checkers specified." << endl;
            exit(1);
        }
    }
    else
    {
        cerr << "Error: invalid checker break duration specified." << endl;
        exit(1);
    }
    // check that we can open file or not and throw error if file could not open for read
    if (!inputFile)
    {
        cerr << "Error: could not open input file <" << argv[3] << ">." << endl;
        exit(1);
    }
    // check that we can open file or not and throw error if file could not open for write
    if (!outputFile)
    {
        {
            cerr << "Error: could not open input file <" << argv[3] << ">." << endl;
            exit(1);
        }
    }
}

// business logic of function
// input checker count, arrival queue as reference, checker break duration and output stream for logging
void run_simulation(int checker_count, PQueue &arrivalPQueue, int checker_break_duration, ostream &os)
{
    Checker checkers[checker_count];
    PQueue checkerQueue, shoppingQueue;
    int busyChecker = 0;
    for (int i = 0; i < checker_count; i++)
    {
        checkers[i].m_cash = 250;
        checkers[i].m_done_time = 0;
        checkers[i].m_cust = NULL;
    }
    int timer = 0;
    while (true)
    {
        // push customer from arrival queue to shopping queue according to its time to enter
        while (true)
        {
            Cust *shoppingComplete;
            int arrivalPQueueTime;
            arrivalPQueue.getFirstPriority(arrivalPQueueTime);
            // check that customer ready to enter the shop for shopping
            if (!arrivalPQueue.isEmpty() && arrivalPQueueTime == timer)
            {
                arrivalPQueue.dequeue(shoppingComplete);
                shoppingQueue.enqueue(shoppingComplete, shoppingComplete->getShopDone());
                os << timer << ": " << shoppingComplete->getName() << " entered store" << endl;
            }
            // if no customer found then continue to next process
            else
            {
                break;
            }
        }

        // push customer from shopping queue to checkers queue according to its time to ready for checkout
        while (true)
        {
            int shoppingQueueTime;
            shoppingQueue.getFirstPriority(shoppingQueueTime);
            // check that customer completed shopping to he can enter to checker queue
            if (!shoppingQueue.isEmpty() && (shoppingQueueTime <= timer))
            {
                Cust *firstChecker;
                shoppingQueue.dequeue(firstChecker);
                os << timer << ": " << firstChecker->getName() << " done shopping" << endl;
                checkerQueue.enqueue(firstChecker, 0);
            }
            // if no customer ready so continue to next process
            else
            {
                break;
            }
        }

        // check if checker done with its customer so checker can server new customer
        if (busyChecker > 0)
        {
            for (int i = 0; i < checker_count; i++)
            {
                // if checker done with customer or break time
                if (timer == checkers[i].m_done_time)
                {
                    // check that checker is done with break time
                    if (checkers[i].m_cust == NULL)
                    {
                        --busyChecker;
                        checkers[i].m_done_time = 0;
                        continue;
                    }
                    // creat string for item as its singular or plural
                    string itemString = "item";
                    if (checkers[i].m_cust->getItemCount() > 1)
                        itemString = "items";

                    // check that customer is robber or not
                    if (checkers[i].m_cust->getIsRobber())
                    {
                        os << timer << ": " << checkers[i].m_cust->getName() << " stole $" << checkers[i].m_cash << " and " << checkers[i].m_cust->getItemCount() << " " << itemString << " from checker " << i << endl;
                        checkers[i].m_cash = 0;
                        if (checker_break_duration == 0)
                        {
                            checkers[i].m_done_time = 0;
                            --busyChecker;
                        }
                        else
                        {
                            checkers[i].m_done_time = timer + checker_break_duration;
                        }
                    }
                    else
                    {
                        os << timer << ": " << checkers[i].m_cust->getName() << " paid $" << checkers[i].m_cust->getItemCount() * COST_PER_ITEM << " for " << checkers[i].m_cust->getItemCount() << " " << itemString << " to checker " << i << endl;
                        checkers[i].m_done_time = 0;
                        --busyChecker;
                    }
                    checkers[i].m_cust = NULL;
                }
            }
        }

        // check if checker is free for server its customer
        while (true)
        {
            if (busyChecker < checker_count)
            {
                Cust *temp = NULL;
                checkerQueue.dequeue(temp);
                // check that customer available for enter in checkout
                if (temp != NULL)
                {
                    for (int i = 0; i < checker_count; i++)
                    {
                        // if customer available then check that checker is available or not
                        if (checkers[i].m_done_time == 0)
                        {
                            if (!temp->getIsRobber())
                            {
                                checkers[i].m_cash += (temp->getItemCount() * COST_PER_ITEM);
                            }
                            checkers[i].m_done_time = timer + temp->getTimeNeededForCheckout();
                            checkers[i].m_cust = temp;
                            os << timer << ": " << temp->getName() << " started checkout with checker " << i << endl;
                            busyChecker++;
                            break;
                        }
                    }
                }
                else
                {
                    break;
                }
            }
            else
            {
                break;
            }
        }

        // check that all customer are server so we exit the loop
        if (checkerQueue.isEmpty() && shoppingQueue.isEmpty() && arrivalPQueue.isEmpty())
        {
            // check if all checker done with customer
            if (busyChecker == 0)
            {
                break;
            }
            bool shouldBreak = true;
            for (int i = 0; i < checker_count; i++)
            {
                if (checkers[i].m_cust != NULL)
                    shouldBreak = false;
            }
            if (shouldBreak)
            {
                break;
            }
        }

        timer++;
    }

    // print checkers cash
    for (int i = 0; i < checker_count; i++)
    {
        os << "registers[" << i << "] = $" << checkers[i].m_cash << endl;
    }
    // print timer
    os << "time = " << timer + 1 << endl;
}

// main function where program start execution
// get command line argument
// return 0 if working correct other wise return 1 as error
int main(int argc, char *argv[])
{
    PQueue arrivalPQueue;
    if (argc != 5)
    {
        cerr << "Error: invalid number of command line arguments." << endl;
        exit(1);
    }
    int totalCheckers;
    int checkerBreakTime;
    ifstream inputFile(argv[3]);
    ofstream outputFile(argv[4]);
    // set cmd argument to variable
    setArgvEle(totalCheckers, checkerBreakTime, inputFile, outputFile, argv);
    // read input from file and create arrival queue
    read_input(inputFile, arrivalPQueue);
    // run business login
    run_simulation(totalCheckers, arrivalPQueue, checkerBreakTime, outputFile);
    return 0;
}