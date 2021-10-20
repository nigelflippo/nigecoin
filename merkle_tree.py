from typing import List
import hashlib

class Node:
    def __init__(self, left, right, value: str, content)-> None:
        self.left: Node = left
        self.right: Node = right
        self.value = value
        self.content = content
    
    @staticmethod
    def hash(val: str)-> str:
        return hashlib.sha256(val.encode('utf-8')).hexdigest()
    def __str__(self):
      return (str(self.value))
 
class MerkleTree:
    def __init__(self, values: List[str])-> None:
        self.__buildTree(values)
 
    def __buildTree(self, values: List[str])-> None:
 
        leaves: List[Node] = [Node(None, None, Node.hash(e),e) for e in values]
        if len(leaves) % 2 == 1:
            leaves.append(leaves[-1:][0])
        self.root: Node = self.__buildTreeRec(leaves) 
    
    def __buildTreeRec(self, nodes: List[Node])-> Node:
        half: int = len(nodes) // 2
 
        if len(nodes) == 2:
            return Node(nodes[0], nodes[1], Node.hash(nodes[0].value + nodes[1].value), nodes[0].content+"+"+nodes[1].content)
        
        left: Node = self.__buildTreeRec(nodes[:half])
        right: Node = self.__buildTreeRec(nodes[half:])
        value: str = Node.hash(left.value + right.value)
        content: str = self.__buildTreeRec(nodes[:half]).content+"+"+self.__buildTreeRec(nodes[half:]).content

        return Node(left, right, value,content)