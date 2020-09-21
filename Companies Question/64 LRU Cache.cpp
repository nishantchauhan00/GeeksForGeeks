// https://www.geeksforgeeks.org/lru-cache-in-python-using-ordereddict/

// 
//
//  1
//
class LRUCache1
{
private:
    list<int> vkeys;
    unordered_map<int, int> hmap;
    int lru_size;

public:
    LRUCache(int cap)
    {
        lru_size = cap;
        hmap.clear();
        vkeys.clear();
    }

    int get(int key)
    {
        if (hmap.find(key) == hmap.end())
            return -1;
        else
        {
            vkeys.remove(key);
            vkeys.push_back(key);
            return hmap[key];
        }
    }

    void set(int key, int value)
    {
        if (hmap.find(key) != hmap.end())
            vkeys.remove(key);

        hmap[key] = value;
        vkeys.push_back(key);

        if (hmap.size() > lru_size)
        {
            hmap.erase(vkeys.front());
            vkeys.pop_front();
        }
    }
};




//
//
//  2
//
class LRUCache
{
private:
    int maxSize;
    list<pair<int,int>> dq;
    unordered_map<int, list<pair<int,int>> :: iterator> ma; 
public:
    LRUCache(int N)
    {
        maxSize = N;
        dq.clear();
        ma.clear();
    }
    
    int get(int x)
    {
        if(ma.find(x) == ma.end())
        {
            return -1;
        }
        auto it = ma.find(x);
        int d  = (*(it->second)).second;
        dq.erase(it->second);
        dq.push_front({x,d});
        ma[x] = dq.begin();
        return d;
    }
    
    void set(int x, int y)
    {
        if(ma.find(x) == ma.end())
        {
           if(dq.size() == maxSize)
           {
               int Lx = dq.back().first;
               int Ly = dq.back().second;
               dq.pop_back();
               dq.push_front({x,y});
               ma.erase(Lx);
               ma[x] =dq.begin();
           }
           else{
               dq.push_front({x,y});
          
                ma[x] = dq.begin();
           }
        }
        else{
            auto it = ma.find(x);
            dq.erase(it->second);
            dq.push_front({x,y});
       
            ma[x]=dq.begin();
        }
    }
};


/*
// using python
from collections import OrderedDict 

class LRUCache:
        
    def __init__(self, capacity: int): 
        self.cache = OrderedDict() 
        self.capacity = capacity 
  
    def get(self, key: int) -> int: 
        if key not in self.cache: 
            return -1
        else: 
            self.cache.move_to_end(key) 
            return self.cache[key] 
  
    def set(self, key: int, value: int) -> None: 
        self.cache[key] = value 
        self.cache.move_to_end(key) 
        if len(self.cache) > self.capacity: 
            self.cache.popitem(last = False) 
*/
