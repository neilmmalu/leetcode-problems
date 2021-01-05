#include <iostream>
#include <unordered_map>
using namespace std;

class LRUCache
{
    class DLLNode
    {
    public:
        int val;
        int key;
        DLLNode *next;
        DLLNode *prev;

        DLLNode() {}

        DLLNode(int k, int v)
        {
            key = k;
            val = v;
        }
    };

    DLLNode *head = new DLLNode();
    DLLNode *tail = new DLLNode();

    int capacity;
    int size = 0;
    unordered_map<int, DLLNode *> cache;

public:
    LRUCache(int capacity)
    {
        this->capacity = capacity;
        head->next = tail;
        tail->prev = head;
    }

    void moveToHead(DLLNode *node)
    {
        removeNode(node);
        addToFront(node);
    }

    void removeNode(DLLNode *node)
    {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void addToFront(DLLNode *node)
    {
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
        node->prev = head;
    }

    void removeFromTail()
    {
        DLLNode *target = tail->prev;
        removeNode(target);
        --size;
        cache.erase(target->key);
        delete target;
    }

    int get(int key)
    {
        DLLNode *node = cache[key];
        moveToHead(node);
        return node->val;
    }

    void put(int key, int value)
    {
        DLLNode *node = cache[key];

        if (cache.find(key) == cache.end())
        {
            DLLNode *newNode = new DLLNode(key, value);
            addToFront(newNode);

            cache[key] = newNode;

            ++size;

            if (size > capacity)
            {
                removeFromTail();
            }
        }
        else
        {
            DLLNode *node = cache[key];
            node->val = value;
            moveToHead(node);
        }
    }
};