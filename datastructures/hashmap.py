import copy
from math import sqrt
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets: Array[LinkedList[Tuple[KT, VT]]] = \
            Array(starting_sequence=[LinkedList(data_type=tuple) for _ in range(number_of_buckets)], \
                data_type=LinkedList)
        
        self._count: int = 0
        self._bucket_count = number_of_buckets
        self._load_factor: float = load_factor
        self._hash_function = custom_hash_function or self._default_hash_function

    def _get_bucket_index(self, key: KT, bucket_size: int):
        bucket_index = self._hash_function(key)
        return bucket_index % bucket_size

    def __getitem__(self, key: KT) -> VT:
        bucket_index = self._get_bucket_index(key, len(self._buckets))
        bucket_chain = self._buckets[bucket_index]

        for (k, v) in bucket_chain:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")


    def __setitem__(self, key: KT, value: VT) -> None:        
        bucket_index = self._get_bucket_index(key, len(self._buckets))
        bucket_chain = self._buckets[bucket_index]
        self._count += 1

        for (k, v) in bucket_chain:
            if k == key:
                bucket_chain.remove((key, v))
        bucket_chain.append((key, value))

        if self._count/self._bucket_count >= self._load_factor:
            self._resize()

    def _resize(self):
        old_hashmap = self._buckets
        self._bucket_count = self.next_prime(self._bucket_count*2)
        self.__init__(self._bucket_count, self._load_factor, self._hash_function)
        for bucket in old_hashmap:
            for (k, v) in bucket:
                self[k] = v
    
    def next_prime(self, n, num = 2):
        if n % 2 == 0:
            return self.next_prime(n = n + 1, num=num)
        elif num <= sqrt(n):
            if n % num == 0:
                return self.next_prime(n = n + 1, num=num)
            else:
                return self.next_prime(n, num+1)
        elif n % num == 0:
            return self.next_prime(n = n + 1, num=num)
        else:
            return n


    def keys(self) -> Iterator[KT]:
        for bucket in self._buckets:
            for (k, v) in bucket:
                yield k
    
    def values(self) -> Iterator[VT]:
        for bucket in self._buckets:
            for (k, v) in bucket:
                yield v

    def items(self) -> Iterator[Tuple[KT, VT]]:
        for bucket in self._buckets:
            for (k, v) in bucket:
                yield (k, v)
            
    def __delitem__(self, key: KT) -> None:
        bucket_index = self._get_bucket_index(key, len(self._buckets))
        bucket_chain = self._buckets[bucket_index]
        self._count -= 1

        for (k, v) in bucket_chain:
            if k == key:
                bucket_chain.remove((key, v))
                return None
        raise KeyError(f"Key '{key}' not found")
    
    def __contains__(self, key: KT) -> bool:
        bucket_index = self._get_bucket_index(key, len(self._buckets))
        bucket_chain = self._buckets[bucket_index]

        for (k, v) in bucket_chain:
            if k == key:
                return True
        return False
    
    
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        for bucket in self._buckets:
            for (k, v) in bucket:
                yield k                
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, HashMap):
            if self._count == other._count:
                for i in range(self._count):
                    if self._buckets[i] != other._buckets[i]:
                        return False
                return True
            else:
                return False
        else:
            return False

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)