const obj = { a: 1, b: 2, c: 3 };

// Not iterable, can't use for...of or Array.from()
for (const key in obj) {
  console.log(key, obj[key]);
}

const map = new Map();
map.set('a', 1);
map.set('b', 2);
map.set('c', 3);

// Iterable, can use for...of or Array.from()
for (const [key, value] of map) {
  console.log(key, value);
}