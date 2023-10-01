class Queue {
    constructor() {
      this.items = [];
    }
  
    // Time complexity: O(1)
    enqueue(element) {
      this.items.push(element);
    }
  
    // Time complexity: O(N)
    dequeue() {
      return this.items.shift();
    }
  
    // Time complexity: O(1)
    peek() {
      if (!this.isEmpty()) {
        return this.items[0];
      }
      return null;
    }
  
    // Time complexity: O(1)
    isEmpty() {
      return this.items.length === 0;
    }
  
    // Time complexity: O(1)
    size() {
      return this.items.length;
    }
  
    // Time complexity: O(N)
    print() {
      console.log(this.items.toString());
    }
  }
  
  const queue = new Queue();
  console.log(queue.isEmpty());
  queue.enqueue(10);
  queue.enqueue(20);
  queue.enqueue(30);
  console.log(queue.size());
  queue.print();
  console.log(queue.dequeue());
  console.log(queue.peek());
  queue.print();
  