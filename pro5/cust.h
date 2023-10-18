#ifndef CUST_H
#define CUST_H

#include <string>
using namespace std;

class Cust {
    public:
    Cust(
        string name,
        bool isRobber,
        int arrival_time,
        int item_count,
        int SHOP_TIME_PER_ITEM,
        int CHECKOUT_TIME_PER_ITEM,
        int ROB_TIME);
    string getName();
    bool getIsRobber();
    int getArrivalTime();
    int getItemCount();
    int getShopDone();
    int getCheckoutStartTime();
    int getTimeNeededForCheckout();
    void print(ostream &os);

    private:
    string name;
    bool isRobber;
    int arrival_time;
    int item_count;
    int shopDone;
    int checkoutStartTime;
    int timeNeededForCheckout;
};

#endif