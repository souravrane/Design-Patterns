let Color = Object.freeze({
  RED: 1,
  GREEN: 2,
  BLUE: 3,
});

let Size = Object.freeze({
  SMALL: 1,
  MEDIUM: 2,
  LARGE: 3,
});

class Product {
  constructor(name, color, size) {
    this.name = name;
    this.color = color;
    this.size = size;
  }
}

// OCP - objects are open for extension but closed for modification
class ProductFilter {
  filterByColor(products, color) {
    return products.filter((p) => p.color === color);
  }

  filterBySize(products, color) {
    return products.filter((p) => p.size === size);
  }

  filterBySizeAndColor(product, color, size) {}
  filterByBlablabla() {} // there will be so many such methods !! This will lead to state space explosion
}

// Specification
class ColorSpecification {
  constructor(color) {
    this.color = color;
  }

  isSatisfied(item) {
    return item.color === this.color;
  }
}

class SizeSpecification {
  constructor(size) {
    this.size = size;
  }

  isSatisfied(item) {
    return item.size === this.size;
  }
}

class AndSpecification {
  constructor(...specs) {
    this.specs = specs;
  }

  isSatisfied(item) {
    return this.specs.every((x) => x.isSatisfied(item));
  }
}

class BetterFilter {
  filter(items, spec) {
    return items.filter((x) => spec.isSatisfied(x));
  }
}

let apple = new Product("Apple", Color.GREEN, Size.SMALL);
let tree = new Product("Tree", Color.GREEN, Size.LARGE);
let house = new Product("House", Color.BLUE, Size.LARGE);

let products = [apple, tree, house];

//  without OCP
let pf = new ProductFilter();
console.log("Green products (old)");
for (let p of pf.filterByColor(products, Color.GREEN))
  console.log(`* ${p.name} is green`);

//   with OCP
let bf = new BetterFilter();
console.log("Green products (new)");
for (let p of bf.filter(products, new ColorSpecification(Color.GREEN))) {
  console.log(`* ${p.name} is green`);
}

console.log("Large and green products");
let spec = new AndSpecification(
  new ColorSpecification(Color.GREEN),
  new SizeSpecification(Size.LARGE)
);
for (let p of bf.filter(products, spec)) {
  console.log(`* ${p.name} is large and green`);
}
