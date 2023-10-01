class Node {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }
  
  class LinkedListQueue {
    constructor() {
      this.head = null;
      this.tail = null;
      this.size = 0;
    }
  
    // Time complexity: O(1)
    enqueue(value) {
      const node = new Node(value);
      if (this.isEmpty()) {
        this.head = node;
        this.tail = node;
      } else {
        this.tail.next = node;
        this.tail = node;
      }
      this.size++;
    }
  
    // Time complexity: O(1)
    dequeue() {
      if (this.isEmpty()) {
        return null;
      }
      const value = this.head.value;
      this.head = this.head.next;
      this.size--;
      if (this.isEmpty()) {
        this.tail = null;
      }
      return value;
    }
  
    // Time complexity: O(1)
    peek() {
      if (this.isEmpty()) {
        return null;
      }
      return this.head.value;
    }
  
    // Time complexity: O(1)
    isEmpty() {
      return this.size === 0;
    }
  
    // Time complexity: O(1)
    getSize() {
      return this.size;
    }
  
    // Time complexity: O(N)
    print() {
      if (this.isEmpty()) {
        console.log("List is empty");
      } else {
        let curr = this.head;
        let list = "";
        while (curr) {
          list += `${curr.value}->`;
          curr = curr.next;
        }
        console.log(list);
      }
    }
  }
  
  const queue = new LinkedListQueue();
  console.log(queue.isEmpty());     //true
  queue.enqueue(10);                
  queue.enqueue(20);
  queue.enqueue(30);
  console.log(queue.getSize());     // 3
  queue.print();                    // 10->20->30->
  console.log(queue.dequeue());     // 10
  queue.print();                    // 20->30->
  console.log(queue.peek());        // 20
  