#include <iostream>
#include <map>

using namespace std;

class Node
{
public:
    int val;
    Node *next;
    Node *random;

    Node() {}

    Node(int _val)
    {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

Node *copyRandomList(Node *head)
{
    if (!head)
        return nullptr;

    Node *curr = head;

    while (curr)
    {
        Node *n = new Node(curr->val);
        n->next = curr->next;
        curr->next = n;
        curr = n->next;
    }

    Node *oldList = head;
    Node *newList = head;

    while (oldList)
    {
        if (oldList->random)
            oldList->next->random = oldList->random->next;
        oldList = oldList->next->next;
    }

    Node *original = head;
    Node *copy = head->next;
    Node *temp = copy;

    while (original && copy)
    {
        original->next = original->next ? original->next->next : original->next;
        copy->next = copy->next ? copy->next->next : copy->next;

        original = original->next;
        copy = copy->next;
    }
    return temp;
}

int main()
{
    return 0;
}