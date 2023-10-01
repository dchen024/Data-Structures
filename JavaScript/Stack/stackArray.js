class Stack {
    constructor() {
      // We can also use a linked list here
      this.items = [];
    }
  
    // Time complexity: O(1)
    push(item) {
      this.items.push(item);
    }
  
    // Time complexity: O(1)
    pop() {
      return this.items.pop();
    }
  
    // Time complexity: O(1)
    size() {
      return this.items.length;
    }
  
    // Time complexity: O(1)
    peek() {
      return this.items[this.items.length - 1];
    }
  }
  
  const stack = new Stack();
  stack.push(5);              // Time complexity: O(1)
  stack.push(12);             // Time complexity: O(1)
  stack.push(5);              // Time complexity: O(1)
  console.log(stack.peek());  // Time complexity: O(1)
  console.log(stack.pop());   // Time complexity: O(1)
  console.log(stack.peek());  // Time complexity: O(1)
  console.log(stack.size());  // Time complexity: O(1)
  