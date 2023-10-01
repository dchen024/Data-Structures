class Node {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }
  
  class Stack {
    constructor() {
      this.top = null;
      this.size = 0;
    }
  
    // Time complexity: O(1)
    push(item) {
      const newNode = new Node(item);
      newNode.next = this.top;
      this.top = newNode;
      this.size++;
    }
  
    // Time complexity: O(1)
    pop() {
      if (!this.top) {
        return null; // Stack is empty
      }
      const removedNode = this.top;
      this.top = this.top.next;
      this.size--;
      return removedNode.value;
    }
  
    // Time complexity: O(1)
    getSize() {
      return this.size;
    }
  
    // Time complexity: O(1)
    peek() {
      if (!this.top) {
        return null; // Stack is empty
      }
      return this.top.value;
    }
  }
  
  const stack = new Stack();
  stack.push(5);              // Time complexity: O(1)
  stack.push(12);             // Time complexity: O(1)
  stack.push(5);              // Time complexity: O(1)
  console.log(stack.peek());  // Time complexity: O(1)
  console.log(stack.pop());   // Time complexity: O(1)
  console.log(stack.peek());  // Time complexity: O(1)
  console.log(stack.getSize());// Time complexity: O(1)
  