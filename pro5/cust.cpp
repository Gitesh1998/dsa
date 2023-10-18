#include <iostream>
using namespace std;
#include "cust.h"

Cust::Cust(string name,
           bool isRobber,
           int arrival_time,
           int item_count,
           int SHOP_TIME_PER_ITEM,
           int CHECKOUT_TIME_PER_ITEM,
           int ROB_TIME)
{
    this->name = name;
    this->isRobber = isRobber;
    this->arrival_time = arrival_time;
    this->item_count = item_count;
    // get shopping complete time
    this->shopDone = arrival_time + (item_count * SHOP_TIME_PER_ITEM);
    // get checkout start time
    this->checkoutStartTime = this->shopDone + 1;
    // check customer is robber or not
    // if robber then assign time needed for robbing 
    if (isRobber)
    {
        this->timeNeededForCheckout = ROB_TIME;
    }
    else
    {
        this->timeNeededForCheckout = item_count * CHECKOUT_TIME_PER_ITEM;
    }
}

string Cust::getName() {
    return this->name;
}

bool Cust::getIsRobber()
{
    return this->isRobber;
}

int Cust::getArrivalTime()
{
    return this->arrival_time;
}

int Cust::getItemCount()
{
    return this->item_count;
}

int Cust::getShopDone()
{
    return this->shopDone;
}

int Cust::getCheckoutStartTime()
{
    return this->checkoutStartTime;
}

int Cust::getTimeNeededForCheckout()
{
    return this->timeNeededForCheckout;
}

void Cust::print(ostream &os)
{
    os << this->name << " " << (this->isRobber ? "robber" : "shopper") << " " << this->arrival_time << " " << this->item_count << endl;
}